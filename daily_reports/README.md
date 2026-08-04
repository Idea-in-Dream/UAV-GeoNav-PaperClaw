# UAV GeoNav Daily Reports

此目录由流水线自动维护。新仓库从 `20260804` 起生成面向无人机定位与地图匹配的日报：

```text
daily_reports/YYYYMM/YYYYMMDD.md
```

首次成功运行 `python3 scripts/cli.py run --date YYYYMMDD --no-notify` 后，本页会自动替换为最近三天日报。

上游 RS-PaperClaw 的历史日报文件仍保留在 Git 历史与现有目录中用于追溯，但 GitHub Pages 只展示本项目部署日期之后的新日报。
