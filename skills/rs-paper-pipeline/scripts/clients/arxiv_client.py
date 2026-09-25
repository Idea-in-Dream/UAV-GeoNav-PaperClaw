#!/usr/bin/env python3
from __future__ import annotations

import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from html.parser import HTMLParser
from urllib.error import HTTPError
from pathlib import Path

from pipeline_config import install_urllib_proxy, load_config
from services.filter_assets import (
    load_arxiv_categories,
    load_candidate_limit_per_day,
    load_candidate_priority_patterns,
    load_rs_context_query_terms,
    load_rs_query_terms,
    load_rs_signal_patterns,
)


CONFIG = load_config()
install_urllib_proxy()
RS_QUERY_TERMS = load_rs_query_terms()
RS_CONTEXT_QUERY_TERMS = load_rs_context_query_terms()
ARXIV_CATEGORIES = load_arxiv_categories()
RS_KEYWORDS = RS_QUERY_TERMS
RS_MATCH_PATTERNS = load_rs_signal_patterns()
CANDIDATE_PRIORITY_PATTERNS = load_candidate_priority_patterns()
CANDIDATE_LIMIT_PER_DAY = load_candidate_limit_per_day()
ATOM_NAMESPACE = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


class _ArxivSearchHTMLParser(HTMLParser):
    """Extract the metadata exposed by arXiv's advanced-search result page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.current: dict[str, object] | None = None
        self.result_depth: int | None = None
        self.captures: list[dict[str, object]] = []
        self.results: list[dict[str, object]] = []

    @staticmethod
    def _classes(attrs: dict[str, str | None]) -> set[str]:
        return set((attrs.get("class") or "").split())

    def _start_capture(self, key: str, tag: str) -> None:
        self.captures.append({"key": key, "tag": tag, "depth": self.depth, "parts": []})

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        attrs = dict(attrs_list)
        classes = self._classes(attrs)

        if tag == "li" and "arxiv-result" in classes and self.current is None:
            self.current = {"categories": []}
            self.result_depth = self.depth

        if self.current is None:
            return

        if tag == "a" and not self.current.get("base_id"):
            match = re.search(r"/abs/([^?#]+)", attrs.get("href") or "")
            if match:
                self.current["base_id"] = match.group(1).strip("/")

        if tag == "p" and "title" in classes:
            self._start_capture("title", tag)
        elif tag == "span" and "abstract-full" in classes:
            self._start_capture("abstract", tag)
            version_match = re.fullmatch(r"(.+v\d+)-abstract-full", attrs.get("id") or "")
            if version_match:
                self.current["arxiv_id"] = version_match.group(1)
        elif tag == "p" and "is-size-7" in classes and "comments" not in classes:
            self._start_capture("submitted_text", tag)
        elif tag == "span" and {"tag", "is-small"}.issubset(classes):
            self._start_capture("category", tag)

    def handle_data(self, data: str) -> None:
        for capture in self.captures:
            parts = capture["parts"]
            assert isinstance(parts, list)
            parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.current is not None:
            completed = [
                capture
                for capture in self.captures
                if capture["tag"] == tag and capture["depth"] == self.depth
            ]
            for capture in completed:
                parts = capture["parts"]
                assert isinstance(parts, list)
                value = " ".join("".join(parts).split())
                key = str(capture["key"])
                if key == "category":
                    categories = self.current["categories"]
                    assert isinstance(categories, list)
                    categories.append(value)
                else:
                    self.current[key] = value
                self.captures.remove(capture)

            if tag == "li" and self.result_depth == self.depth:
                self.results.append(self.current)
                self.current = None
                self.result_depth = None
                self.captures.clear()

        self.depth -= 1


def has_remote_sensing_signal(text: str) -> bool:
    return any(pattern.search(text) for pattern in RS_MATCH_PATTERNS)


def candidate_priority_score(text: str) -> int:
    return sum(1 for pattern in CANDIDATE_PRIORITY_PATTERNS if pattern.search(text))


def limit_candidates_per_day(items: list[dict[str, str]], per_day_limit: int) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    day_order: list[str] = []
    for item in items:
        day = item["published"]
        if day not in grouped:
            grouped[day] = []
            day_order.append(day)
        grouped[day].append(item)

    limited: list[dict[str, str]] = []
    for day in day_order:
        ranked = sorted(
            grouped[day],
            key=lambda item: -candidate_priority_score(f"{item['title']}\n{item['abstract']}"),
        )
        limited.extend(ranked[:per_day_limit])
    return limited


def build_terms_query(terms: list[str]) -> str:
    parts = []
    for term in terms:
        if " " in term:
            parts.append(f'all:"{term}"')
        else:
            parts.append(f"all:{term}")
    return " OR ".join(parts)


def _retry_after_seconds(headers) -> int | None:
    retry_after = headers.get("Retry-After") if headers else None
    if retry_after and retry_after.isdigit():
        return int(retry_after)
    return None


def build_arxiv_proxy_url(url: str, proxy_prefix: str | None) -> str | None:
    if not proxy_prefix:
        return None
    return f"{proxy_prefix}{urllib.parse.quote(url, safe='')}"


def build_arxiv_direct_fallback_url(url: str) -> str | None:
    """Switch between the two official arXiv API hostnames."""
    parsed = urllib.parse.urlsplit(url)
    hostname = (parsed.hostname or "").lower()
    if hostname == "export.arxiv.org":
        fallback_host = "arxiv.org"
    elif hostname == "arxiv.org":
        fallback_host = "export.arxiv.org"
    else:
        return None

    return urllib.parse.urlunsplit(
        (parsed.scheme or "https", fallback_host, parsed.path, parsed.query, parsed.fragment)
    )


def _arxiv_fetch_urls(url: str) -> list[str]:
    proxy_url = build_arxiv_proxy_url(url, CONFIG.arxiv_api_proxy_prefix)
    if CONFIG.arxiv_api_force_proxy and proxy_url:
        return [proxy_url]

    urls = [url]
    direct_fallback = build_arxiv_direct_fallback_url(url)
    if direct_fallback and direct_fallback not in urls:
        urls.append(direct_fallback)
    if proxy_url and proxy_url not in urls:
        urls.append(proxy_url)
    return urls


def fetch_url_with_retry(url: str, retries: int = 6, timeout: int = 90) -> str:
    backoff = [5, 15, 30, 60, 120, 240]
    rate_limit_backoff = [60, 120, 240, 360, 600, 900]
    last_err = None
    fetch_urls = _arxiv_fetch_urls(url)
    for i in range(retries):
        active_url = fetch_urls[i % len(fetch_urls)]
        try:
            req = urllib.request.Request(active_url, headers={"User-Agent": CONFIG.arxiv_user_agent})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="ignore")
        except HTTPError as exc:
            last_err = exc
            if exc.code in (429, 503):
                wait_s = max(
                    _retry_after_seconds(exc.headers) or 0,
                    rate_limit_backoff[min(i, len(rate_limit_backoff) - 1)],
                )
            else:
                wait_s = backoff[min(i, len(backoff) - 1)]
        except Exception as exc:
            last_err = exc
            wait_s = backoff[min(i, len(backoff) - 1)]

        if i == retries - 1:
            break

        next_url = fetch_urls[(i + 1) % len(fetch_urls)]
        if len(fetch_urls) > 1 and (i + 1) % len(fetch_urls) != 0:
            print(
                f"  [arXiv] {last_err.__class__.__name__}, switching endpoint to "
                f"{urllib.parse.urlsplit(next_url).netloc}"
            )
            continue

        print(f"  [arXiv] retry {i+1}/{retries} in {wait_s}s")
        time.sleep(wait_s)
    raise last_err


def _build_search_term(terms: list[str]) -> str:
    return " OR ".join(f'"{term}"' if " " in term else term for term in terms)


def _original_submission_date(submitted_text: str) -> datetime | None:
    match = re.search(r"\bv1 submitted\s+(\d{1,2} [A-Za-z]+, \d{4})", submitted_text)
    if not match:
        match = re.search(r"\bSubmitted\s+(\d{1,2} [A-Za-z]+, \d{4})", submitted_text)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%d %B, %Y")
    except ValueError:
        return None


def _fetch_target_date_from_search(
    target_date: str,
    max_results: int,
    per_day_limit: int,
) -> list[dict[str, str]]:
    """Use arXiv's search frontend when the legacy Atom API is unavailable."""
    target_day = datetime.strptime(target_date, "%Y%m%d").date()
    next_day = target_day + timedelta(days=1)
    page_size = min(max_results, 200)
    items: list[dict[str, str]] = []
    seen: set[str] = set()

    for start in range(0, max_results, page_size):
        if start > 0:
            time.sleep(5)
        params = {
            "advanced": "1",
            "terms-0-term": _build_search_term(RS_CONTEXT_QUERY_TERMS),
            "terms-0-field": "all",
            "classification-include_cross_list": "include",
            "date-filter_by": "date_range",
            "date-from_date": target_day.isoformat(),
            # The search form rejects an equal start/end date. Results are
            # filtered back to target_day below.
            "date-to_date": next_day.isoformat(),
            "date-date_type": "submitted_date_first",
            "abstracts": "show",
            "size": str(page_size),
            "order": "-submitted_date",
            "start": str(start),
        }
        if any(category.startswith("cs.") for category in ARXIV_CATEGORIES):
            params["classification-computer_science"] = "y"
        if any(category.startswith("eess.") for category in ARXIV_CATEGORIES):
            params["classification-eess"] = "y"

        url = f"https://arxiv.org/search/advanced?{urllib.parse.urlencode(params)}"
        html_text = fetch_url_with_retry(url, retries=3, timeout=35)
        parser = _ArxivSearchHTMLParser()
        parser.feed(html_text)
        page_results = parser.results

        for result in page_results:
            base_id = str(result.get("base_id") or "")
            arxiv_id = str(result.get("arxiv_id") or base_id)
            title = str(result.get("title") or "")
            abstract = re.sub(r"\s*[△▲]\s*Less\s*$", "", str(result.get("abstract") or ""))
            submitted_at = _original_submission_date(str(result.get("submitted_text") or ""))
            categories = set(result.get("categories") or [])

            if not arxiv_id or not title or not abstract or not submitted_at:
                continue
            if submitted_at.date() != target_day:
                continue
            if not categories.intersection(ARXIV_CATEGORIES):
                continue
            if arxiv_id in seen:
                continue
            seen.add(arxiv_id)

            text = f"{title}\n{abstract}"
            if not has_remote_sensing_signal(text):
                continue
            items.append(
                {
                    "arxiv_id": arxiv_id,
                    "title": title,
                    "abstract": abstract,
                    "published": target_day.isoformat(),
                }
            )

        if len(page_results) < page_size:
            break

    return limit_candidates_per_day(items, per_day_limit)


def fetch_recent_candidates(
    max_results: int = 500,
    days_back: int = 2,
    target_date: str | None = None,
    candidate_limit_per_day: int | None = None,
) -> list[dict[str, str]]:
    per_day_limit = CANDIDATE_LIMIT_PER_DAY if candidate_limit_per_day is None else candidate_limit_per_day
    if per_day_limit <= 0:
        raise ValueError("candidate_limit_per_day must be positive")
    base_query = build_terms_query(RS_QUERY_TERMS)
    namespace = {"atom": "http://www.w3.org/2005/Atom"}

    if target_date:
        valid_days = {datetime.strptime(target_date, "%Y%m%d").date()}
    else:
        today = datetime.now().date()
        valid_days = {today - timedelta(days=i) for i in range(days_back)}

    def run_query(query: str, max_scan: int, page_size: int) -> list[dict[str, str]]:
        items: list[dict[str, str]] = []
        seen: set[str] = set()

        for start in range(0, max_scan, page_size):
            if start > 0:
                time.sleep(20 if target_date else 10)
            params = {
                "search_query": query,
                "start": start,
                "max_results": page_size,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
            url = f"{CONFIG.arxiv_api}?{urllib.parse.urlencode(params)}"
            xml_text = fetch_url_with_retry(
                url,
                retries=2 if target_date else 4,
                timeout=20 if target_date else 45,
            )

            root = ET.fromstring(xml_text)
            entries = root.findall("atom:entry", namespace)
            if not entries:
                break

            min_page_date = None
            for entry in entries:
                arxiv_id = (entry.find("atom:id", namespace).text or "").strip().split("/")[-1]
                if arxiv_id in seen:
                    continue
                seen.add(arxiv_id)

                title = (entry.find("atom:title", namespace).text or "").strip().replace("\n", " ")
                abstract = (entry.find("atom:summary", namespace).text or "").strip().replace("\n", " ")
                published = (entry.find("atom:published", namespace).text or "").strip()
                try:
                    published_date = datetime.strptime(published[:10], "%Y-%m-%d").date()
                except Exception:
                    continue

                if min_page_date is None or published_date < min_page_date:
                    min_page_date = published_date

                if published_date not in valid_days:
                    continue

                text = f"{title}\n{abstract}"
                if not has_remote_sensing_signal(text):
                    continue

                items.append(
                    {
                        "arxiv_id": arxiv_id,
                        "title": title,
                        "abstract": abstract,
                        "published": published[:10],
                    }
                )
            if target_date and min_page_date and min_page_date < next(iter(valid_days)):
                break

        return limit_candidates_per_day(items, per_day_limit)

    if target_date:
        category_query = " OR ".join(f"cat:{category}" for category in ARXIV_CATEGORIES)
        context_query = build_terms_query(RS_CONTEXT_QUERY_TERMS)
        scoped_query = (
            f"({category_query}) AND ({context_query}) "
            f"AND submittedDate:[{target_date}0000 TO {target_date}2359]"
        )
        try:
            return run_query(scoped_query, max_scan=max_results, page_size=min(max_results, 200))
        except Exception as exc:
            print(
                f"  [arXiv] Atom API failed ({exc.__class__.__name__}: {exc}); "
                "falling back to advanced search"
            )
            return _fetch_target_date_from_search(target_date, max_results, per_day_limit)

    return run_query(base_query, max_scan=3000, page_size=min(max_results, 200))


def download_pdf(arxiv_id: str) -> tuple[Path | None, bool]:
    CONFIG.temp_dir.mkdir(parents=True, exist_ok=True)
    output = CONFIG.temp_dir / f"{arxiv_id}.pdf"
    mirrors = [
        f"https://arxiv.org/pdf/{arxiv_id}.pdf",
        f"https://export.arxiv.org/pdf/{arxiv_id}.pdf",
        f"https://ar5iv.org/pdf/{arxiv_id}",
    ]

    def threaded_download(url: str, parts: int = 4) -> bool:
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": CONFIG.arxiv_user_agent})
            with urllib.request.urlopen(req, timeout=20) as response:
                headers = {key.lower(): value for key, value in response.getheaders()}
            length = int(headers.get("content-length", "0"))
            accept_ranges = headers.get("accept-ranges", "")
            if length <= 0 or "bytes" not in accept_ranges.lower():
                return False

            chunk = length // parts
            ranges = []
            for i in range(parts):
                start = i * chunk
                end = (length - 1) if i == parts - 1 else ((i + 1) * chunk - 1)
                ranges.append((i, start, end))

            data_parts = [b""] * parts

            def fetch_part(idx: int, start: int, end: int):
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": CONFIG.arxiv_user_agent, "Range": f"bytes={start}-{end}"},
                )
                with urllib.request.urlopen(req, timeout=60) as response:
                    return idx, response.read()

            with ThreadPoolExecutor(max_workers=parts) as executor:
                futures = [executor.submit(fetch_part, i, start, end) for i, start, end in ranges]
                for future in as_completed(futures):
                    idx, part = future.result()
                    data_parts[idx] = part

            output.write_bytes(b"".join(data_parts))
            return output.exists() and output.stat().st_size > 0
        except Exception:
            return False

    for url in mirrors:
        try:
            if threaded_download(url, parts=4):
                return output, True
            with urllib.request.urlopen(url, timeout=60) as response:
                output.write_bytes(response.read())
            if output.exists() and output.stat().st_size > 0:
                return output, True
        except Exception:
            continue

    return None, False


def download_source(arxiv_id: str) -> Path | None:
    CONFIG.temp_dir.mkdir(parents=True, exist_ok=True)
    output = CONFIG.temp_dir / f"{arxiv_id}.src"
    urls = [
        f"https://arxiv.org/e-print/{arxiv_id}",
        f"https://export.arxiv.org/e-print/{arxiv_id}",
    ]

    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": CONFIG.arxiv_user_agent})
            with urllib.request.urlopen(req, timeout=60) as response:
                output.write_bytes(response.read())
            if output.exists() and output.stat().st_size > 0:
                return output
        except Exception:
            continue

    return None


def fetch_arxiv_html(arxiv_id: str) -> str:
    """Fetch the public HTML rendering used as an affiliation fallback."""
    urls = [
        f"https://arxiv.org/html/{arxiv_id}",
        f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}",
    ]
    for url in urls:
        try:
            return fetch_url_with_retry(url, retries=2, timeout=60)
        except Exception:
            continue
    return ""


def normalize_author_name(name: str) -> str:
    normalized = re.sub(r"\s+", " ", name or "").strip()
    if not normalized:
        return ""

    parts = normalized.split()
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return normalized


def format_authors(authors: list[str]) -> str:
    clean_authors = [author for author in (normalize_author_name(name) for name in authors) if author]
    if not clean_authors:
        return "待提取"
    if len(clean_authors) <= 20:
        return ", ".join(clean_authors)
    return ", ".join(clean_authors[:19] + ["..."] + [clean_authors[-1]])


def format_affiliations(affiliations: list[str]) -> str:
    unique_affiliations: list[str] = []
    seen: set[str] = set()

    for affiliation in affiliations:
        normalized = re.sub(r"\s+", " ", affiliation or "").strip(" ,;")
        if not normalized:
            continue
        dedupe_key = normalized.casefold()
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        unique_affiliations.append(normalized)

    if not unique_affiliations:
        return "待提取"
    if len(unique_affiliations) <= 10:
        return "；".join(unique_affiliations)
    return "；".join(unique_affiliations[:9] + ["..."] + [unique_affiliations[-1]])


def fetch_paper_metadata(arxiv_id: str) -> tuple[list[str], list[str], str, str, str] | None:
    params = {"id_list": arxiv_id}
    url = f"{CONFIG.arxiv_api}?{urllib.parse.urlencode(params)}"
    xml_text = fetch_url_with_retry(url, retries=4, timeout=90)
    root = ET.fromstring(xml_text)
    entry = root.find("atom:entry", ATOM_NAMESPACE)
    if entry is None:
        return None

    title = (entry.findtext("atom:title", default="", namespaces=ATOM_NAMESPACE) or "").replace("\n", " ").strip()
    abstract_en = (
        (entry.findtext("atom:summary", default="", namespaces=ATOM_NAMESPACE) or "")
        .replace("\n", " ")
        .strip()
    )
    published = (entry.findtext("atom:published", default="", namespaces=ATOM_NAMESPACE) or "").strip()

    authors: list[str] = []
    affiliations: list[str] = []
    for author_node in entry.findall("atom:author", ATOM_NAMESPACE):
        name = author_node.findtext("atom:name", default="", namespaces=ATOM_NAMESPACE)
        if name and name.strip():
            authors.append(name.strip())

        affiliation = author_node.findtext("arxiv:affiliation", default="", namespaces=ATOM_NAMESPACE)
        if affiliation and affiliation.strip():
            affiliations.append(affiliation.strip())

    return authors, affiliations, title, abstract_en, published


def extract_abs_info(arxiv_id: str) -> dict[str, str]:
    try:
        api_metadata = fetch_paper_metadata(arxiv_id)
        if api_metadata is None:
            raise RuntimeError("arXiv API entry not found")

        authors, affiliations, title, abstract_en, published = api_metadata
        try:
            date = datetime.strptime(published[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
        except Exception:
            date = datetime.now().strftime("%Y-%m-%d")

        return {
            "title": title or "Unknown",
            "authors": format_authors(authors),
            "institutions": format_affiliations(affiliations),
            "abstract_en": abstract_en,
            "date": date,
        }
    except Exception as exc:
        print(f"    ❌ 提取失败: {exc}")
        return {
            "title": "Unknown",
            "authors": "待提取",
            "institutions": "待提取",
            "abstract_en": "",
            "date": datetime.now().strftime("%Y-%m-%d"),
        }
