#!/usr/bin/env python3
# 🪝 MessageDisplay — 🗣️🔤👀 → 📜 ↔️ + 😾hisss! 🏷️   (🚫🎭📜 ; 🔗✅ ; 📺-🪞 ; 📜+🤖👀 🚫🎭)
# 📚 https://code.claude.com/docs/en/hooks
# 📥 stdin  {"delta": "…"}  →  📤 stdout  {"hookSpecificOutput": {"hookEventName", "displayContent"}}
import json
import re
import sys

# 🙈  `⌨️` , 🔗 , 📁/
𓁹𓅂 = re.compile(
    r"`[^`\n]*`|(?i:\b[a-z][a-z0-9+.\-]*://\S+)|(?i:\bwww\.\S+)|\S*/\S*"
)

# 🗣️🔤  (A-z + À-ž)
𓊖 = re.compile(r"[A-Za-zÀ-ÖØ-öø-ɏ]+")

# 🐈✅  meow mew miaou mrrr prrr purr hisss nyan grrr
𓃠𓊍 = re.compile(
    r"(?i)^(?:m+e+o+w+|m+e+w+|m+i+a+(?:[ou]+w*|w+)|m+r{2,}|p+u*r{2,}|h+i+s{2,}|n+y+a+n*|g*r{2,})$"
)

# 🏷️  📄🔚
𓅱 = "  😾hisss!"


def 𓁹(𓋍: str) -> bool:
    # 🗣️❓   (🙈 → 🔍)
    𓋎 = 𓁹𓅂.sub(" ", 𓋍)
    return any(not 𓃠𓊍.match(𓊍) for 𓊍 in 𓊖.findall(𓋎))


def 𓁐(𓆼: str) -> str:
    # 📜 → 📜🏷️   (📄-wise ; 📜 ↔️ ; 🔗✅)
    return "\n".join(
        𓋍 + 𓅱 if 𓁹(𓋍) else 𓋍
        for 𓋍 in 𓆼.split("\n")
    )


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
