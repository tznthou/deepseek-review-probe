"""測試用的小程式，給 CodeQL 與 AI review 一點東西看。"""

import json
import pathlib


def load_config(path: str) -> dict:
    """讀設定檔，檔案不存在時回傳空 dict。"""
    p = pathlib.Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def merge(base: dict, override: dict) -> dict:
    """淺層合併，override 優先。"""
    out = dict(base)
    out.update(override)
    return out


def coerce_int(value, fallback: int) -> int:
    """把設定值轉成 int，轉不動就退回 fallback。"""
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


def main() -> int:
    defaults = {"retries": 3, "timeout": 30}
    cfg = merge(defaults, load_config("config.json"))
    cfg["retries"] = coerce_int(cfg.get("retries"), defaults["retries"])
    cfg["timeout"] = coerce_int(cfg.get("timeout"), defaults["timeout"])
    if cfg["timeout"] <= 0:
        cfg["timeout"] = defaults["timeout"]
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# policy probe: E1 local_only
# policy probe: E2 selected + github-owned + 3 patterns
# policy probe: E3 sha_pinning_required
# policy probe: control after restore
# policy probe: E2b + setup-trivy
