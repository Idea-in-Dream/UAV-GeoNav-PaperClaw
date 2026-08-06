# UAV-GeoNav-PaperClaw

An automated arXiv tracker for UAV geo-localization, map matching, map-aided visual-inertial navigation, and GNSS-denied navigation.

The project is adapted from [thinson/RS-PaperClaw](https://github.com/thinson/RS-PaperClaw) and preserves its Python pipeline, GitHub Issue workflow, daily Markdown digests, and GitHub Pages frontend. The upstream license is retained at [`skills/rs-paper-pipeline/LICENSE`](./skills/rs-paper-pipeline/LICENSE).

The tracker covers:

- UAV-to-satellite and cross-view geo-localization;
- orthophoto, TDOM, DSM, and DEM registration;
- 3D map, 3DGS, and NeRF localization;
- map-aided VIO/SLAM and GNSS-denied navigation;
- UAV ego localization and target geolocation;
- thermal UAV cross-modal localization;
- directly relevant datasets and benchmarks.

Each retained paper becomes a structured Chinese GitHub Issue containing its map type, sensors, localization output, method, accuracy, runtime/hardware, VIO/IMU integration, reproducibility, relation to GeoVINS/NGPS/PiLoT v2, and project value.

## Deployment

1. Create or fork a repository named `UAV-GeoNav-PaperClaw`.
2. Enable Issues and allow GitHub Actions read/write access.
3. Configure the `LLM_API_KEY` Actions secret.
4. Optionally configure `UAV_GITHUB_TOKEN` when the built-in token cannot write Issues or contents.
5. Set GitHub Pages source to **GitHub Actions**.
6. Run the `UAV GeoNav PaperClaw Manual` workflow with `run_no_notify`.

The scheduled workflow runs seven days a week at 00:00 UTC (08:00 Asia/Shanghai) and processes the previous calendar day. GitHub Actions may start slightly later when runners are queued.

## Local validation

```bash
cd skills/rs-paper-pipeline
./bootstrap.sh
cp .env.example .env

python3 scripts/cli.py doctor
python3 scripts/cli.py filter --dry-run --date YYYYMMDD
python3 scripts/cli.py run --date YYYYMMDD --no-notify
python3 -m unittest discover -s tests -v
```

See the Chinese [`README.md`](./README.md) for the full Secrets, Variables, scheduling, filtering, and customization guide.
