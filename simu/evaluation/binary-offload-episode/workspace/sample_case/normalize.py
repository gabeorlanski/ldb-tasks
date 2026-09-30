from __future__ import annotations

from typing import Any

FLOAT_DIGITS = 9


def normalize(value: Any) -> Any:
    if isinstance(value, float):
        rounded = round(value, FLOAT_DIGITS)
        return 0.0 if rounded == -0.0 else rounded
    if isinstance(value, int) or value is None or isinstance(value, str) or isinstance(value, bool):
        return value
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if isinstance(value, dict):
        item = dict(value)
        if "execution" in item:
            item["execution"] = str(item["execution"]).lower()
        for records_key in ("reference_records", "action_records"):
            if isinstance(item.get(records_key), list):
                item[records_key] = sorted(item[records_key], key=lambda record: record.get("task_id"))
        return {key: normalize(item[key]) for key in sorted(item)}
    return value
