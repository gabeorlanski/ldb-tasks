#!/usr/bin/env python3
"""Normalize client round-trip JSONL for visible comparison."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def normalize_value(value: Any) -> Any:
    """Normalize incidental formatting while preserving schema-owned structure."""
    if isinstance(value, dict):
        if "errors" in value and isinstance(value["errors"], list):
            value = {
                **value,
                "errors": [
                    {"loc": error.get("loc")}
                    for error in value["errors"]
                    if isinstance(error, dict)
                ],
            }
        return {str(key): normalize_value(value[key]) for key in sorted(value)}
    if isinstance(value, list):
        return [normalize_value(item) for item in value]
    if isinstance(value, float):
        return round(value, 9)
    return value


def normalize_line(line: str) -> str:
    """Normalize one JSONL line to canonical JSON text."""
    value = json.loads(line)
    return json.dumps(normalize_value(value), sort_keys=True, separators=(",", ":"))


def main() -> None:
    """Normalize each non-empty line in a JSONL file."""
    path = Path(sys.argv[1])
    for line in path.read_text().splitlines():
        if line.strip():
            print(normalize_line(line))


if __name__ == "__main__":
    main()
