#!/usr/bin/env python3
# 🪝 `MessageDisplay` — 🗣️🔤👀 → 📜 ↔️ + 😾hisss! 🏷️   (🚫🎭📜 ; 🔗✅ ; 📺-🪞 ; 📜+🤖👀 🚫🎭)
# ➕ 🈲🗣️ (🇨🇳🇭🇰🇵🇱🇲🇻🇳🇴🇺🇬) → 🙊 + 🏷️ ‼️‼️   (🚫🚫🚫 — `⌨️`🔗📁 🚫🙈)
# 📜 `🙊📜.md` — 🚧📜
# 📚 https://code.claude.com/docs/en/hooks
# 📥 `stdin`  `{"delta": "…"}`  →  📤 `stdout`  `{"hookSpecificOutput": {"hookEventName", "displayContent"}}`
import json
import re
import sys

# 🙈  `⌨️` , 🔗 , 📁/
𓁹𓅂 = re.compile(
    r"`[^`\n]*`|(?i:\b[a-z][a-z0-9+.\-]*://\S+)|(?i:\bwww\.\S+)|\S*/\S*"
)

# 🗣️🔤  (`A-z` + U+00C0-024F)
𓊖 = re.compile(r"[A-Za-z\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u024f]+")

# 🈲 🗣️  🚫🚫🚫  →  🙊❌   (📜 🙊📜.md)
#   🇨🇳🇭🇰 U+3400-4DBF U+4E00-9FFF U+F900-FAFF U+20000-2EBEF
#   🇵🇱 U+0104-0107 U+0118-0119 U+0141-0144 U+015A-015B U+0179-017C
#   🇲🇻 U+0780-07BF  ·  🇳🇴 U+00C5 U+00C6 U+00D8 U+00E5 U+00E6 U+00F8  ·  🇺🇬 U+014A-014B
𓉗 = re.compile(
    r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002ebef"
    r"\u0780-\u07bf"
    r"\u0104-\u0107\u0118\u0119\u0141-\u0144\u015a\u015b\u0179-\u017c"
    r"\u00c5\u00c6\u00d8\u00e5\u00e6\u00f8"
    r"\u014a\u014b]"
)
𓉗𓅱 = "  🙊❌😾😾‼️‼️"

# 🐈✅  meow mew miaou mrrr prrr purr hisss nyan grrr
𓃠𓊍 = re.compile(
    r"(?i)^(?:m+e+o+w+|m+e+w+|m+i+a+(?:[ou]+w*|w+)|m+r{2,}|p+u*r{2,}|h+i+s{2,}|n+y+a+n*|g*r{2,})$"
)

# 🏷️  📄🔚   😾 ⬆️⬆️⬆️ → 📢
def 𓅱(𓈖: int) -> str:
    if 𓈖 >= 6:
        return "  📢😾😾😾HISSSSSS‼️"     # ⬆️⬆️⬆️ 📢
    if 𓈖 >= 3:
        return "  😾😾hisssss!!"           # ⬆️⬆️
    return "  😾hisss!"                    # ⬆️


def 𓁹(𓋍: str) -> int:
    # 🗣️🔢   (🙈 → 🔍)
    𓋎 = 𓁹𓅂.sub(" ", 𓋍)
    return sum(1 for 𓊍 in 𓊖.findall(𓋎) if not 𓃠𓊍.match(𓊍))


def 𓁐(𓆼: str) -> str:
    # 📜 → 📜🏷️   (/📄 ; 📜 ↔️ ; 🔗✅ ; 🗣️🔢 → 🔊🪜 ; 🈲 → 🙊❌ ‼️‼️)
    𓂏 = []
    for 𓋍 in 𓆼.split("\n"):
        if 𓉗.search(𓋍):
            𓂏.append(𓉗.sub("🙊", 𓋍) + 𓉗𓅱)      # 🈲 🚫🚫🚫 — 🚫🙈
            continue
        𓈖 = 𓁹(𓋍)
        𓂏.append(𓋍 + 𓅱(𓈖) if 𓈖 else 𓋍)
    return "\n".join(𓂏)


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
