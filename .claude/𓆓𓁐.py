#!/usr/bin/env python3
# 🪝 MessageDisplay — 🗣️🔤 → 😾 hisss   (📺🎭 ; 📜 + 🤖👀 🚫🎭)
# 📚 https://code.claude.com/docs/en/hooks
# 📥 stdin  {"delta": "…"}  →  📤 stdout  {"hookSpecificOutput": {"hookEventName", "displayContent"}}
import json
import re
import sys

# 🗣️🔤  (A-z + À-ž)
𓊖 = re.compile(r"[A-Za-zÀ-ÖØ-öø-ɏ]+")

# 🐈✅  meow mew miaou mrrr prrr purr hisss nyan grrr
𓃠𓊍 = re.compile(
    r"(?i)^(?:m+e+o+w+|m+e+w+|m+i+a+(?:[ou]+w*|w+)|m+r{2,}|p+u*r{2,}|h+i+s{2,}|n+y+a+n*|g*r{2,})$"
)


def 𓆓(𓊍: str) -> str:
    # 🗣️ → hisss   (📏 ↔️, Aa ↔️)
    if 𓃠𓊍.match(𓊍):
        return 𓊍                       # 🐈✅ prrr
    𓈖 = max(4, len(𓊍))
    𓉻 = "hi" + "s" * (𓈖 - 2)
    if 𓊍.isupper() and len(𓊍) > 1:
        return 𓉻.upper()               # 😾‼️
    if 𓊍[:1].isupper():
        return 𓉻.capitalize()
    return 𓉻


def 𓁐(𓆼: str) -> str:
    # 📜 → 📜😾   (🔤→hisss ; 🐾🖼️𓂀🔢 ↔️)
    return 𓊖.sub(lambda 𓅘: 𓆓(𓅘.group(0)), 𓆼)


def 𓋹() -> None:
    try:
        𓂭 = json.load(sys.stdin)
        𓆼 = 𓂭.get("delta") or ""
    except Exception:
        return                          # 🙀 → 📺 🅾️
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "MessageDisplay",
            "displayContent": 𓁐(𓆼),
        }
    }))


if __name__ == "__main__":
    𓋹()
