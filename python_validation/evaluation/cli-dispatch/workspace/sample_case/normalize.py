#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

STABLE_PATHS = [
    "request_id",
    "query",
    "mode",
    "channels",
    "limit",
    "confidence",
    "target_url",
    "trace_id",
    "submitted_at",
    "context.language",
    "context.country",
    "context.tags",
    "batch_id",
    "items.0",
    "items.0.scope",
    "items.0.vendor_id",
    "$schema",
    "pass",
    "from",
    "dash-key",
    "payload.claim_type",
    "job_id",
    "priority",
]


def normalize_value(value: Any) -> Any:
    if isinstance(value, dict):
        if value.get("success") is False and isinstance(value.get("error"), str):
            error = value["error"]
            lowered = error.lower()
            if "invalid request payload for" in lowered:
                match = re.search(r"Invalid request payload for ([A-Za-z0-9_]+)", error)
                return {
                    "success": False,
                    "invalid_for": match.group(1) if match else None,
                    "paths": sorted(path for path in STABLE_PATHS if path in error),
                }
            if "unknown" in lowered:
                return {
                    "success": False,
                    "unknown_tool": "missing_tool" in error,
                    "mentions_available": "constrained_search" in error,
                }
            return {"success": False, "error": error}
        return {key: normalize_value(value[key]) for key in sorted(value)}
    if isinstance(value, list):
        return [normalize_value(item) for item in value]
    if isinstance(value, float):
        return round(value, 9)
    return value


def normalize_line(line: str) -> str:
    value = json.loads(line)
    return json.dumps(normalize_value(value), sort_keys=True, separators=(",", ":"))


def main() -> None:
    path = Path(sys.argv[1])
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            print(normalize_line(line))


if __name__ == "__main__":
    main()
