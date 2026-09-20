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


def main() -> int:
    defaults = {"retries": 3, "timeout": 30}
    cfg = merge(defaults, load_config("config.json"))
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
