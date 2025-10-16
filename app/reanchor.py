from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, time, timedelta, timezone
import argparse
import sys
import yaml
from pathlib import Path


@dataclass
class ReanchorConfig:
    re_anchor: bool
    dfr: bool
    anchor_time: time


def parse_time_str(value: str) -> time:
    try:
        hour, minute = [int(p) for p in value.split(":", 1)]
        if not (0 <= hour < 24 and 0 <= minute < 60):
            raise ValueError
        return time(hour=hour, minute=minute)
    except Exception as exc:  # noqa: BLE001
        raise argparse.ArgumentTypeError(
            f"Invalid time '{value}', expected HH:MM"
        ) from exc


def load_config(config_path: Path) -> ReanchorConfig:
    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    re_anchor = bool(data.get("re_anchor", False))
    dfr = bool(data.get("dfr", False))
    anchor_time_str = str(data.get("anchor_time", "17:00"))
    return ReanchorConfig(re_anchor=re_anchor, dfr=dfr, anchor_time=parse_time_str(anchor_time_str))


def compute_next_anchor(now: datetime, anchor_at: time) -> datetime:
    today_anchor = datetime.combine(now.date(), anchor_at, tzinfo=now.tzinfo)
    if now <= today_anchor:
        return today_anchor
    return today_anchor + timedelta(days=1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Re-anchor CLI")
    parser.add_argument("--config", type=Path, default=Path("config.yaml"))
    parser.add_argument("--now", type=str, help="Override current time in ISO format", default=None)
    parser.add_argument("--tz", type=int, help="Override timezone offset minutes (e.g., 0, 330)", default=None)
    args = parser.parse_args(argv)

    config = load_config(args.config)

    tzinfo = None
    if args.tz is not None:
        tzinfo = timezone(timedelta(minutes=int(args.tz)))

    now = datetime.now(tz=tzinfo)
    if args.now:
        now = datetime.fromisoformat(args.now)
        if tzinfo is not None and now.tzinfo is None:
            now = now.replace(tzinfo=tzinfo)

    if not config.re_anchor:
        print("re_anchor disabled")
        return 0

    next_anchor = compute_next_anchor(now, config.anchor_time)

    result = {
        "re_anchor": config.re_anchor,
        "dfr": config.dfr,
        "anchor_time": config.anchor_time.strftime("%H:%M"),
        "now": now.isoformat(),
        "next_anchor": next_anchor.isoformat(),
    }

    print(yaml.safe_dump(result, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
