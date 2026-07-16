#!/usr/bin/env python3
# 🪝 `MessageDisplay` — 🗣️🔤👀 → 📜 ↔️ + 😾hisss! 🏷️   (🚫🎭📜 ; 🔗✅ ; 📺-🪞 ; 📜+🤖👀 🚫🎭)
# ➕ 🈲 ∀🏳️🌐 ¬🇺🇲🇬🇧 → 🙊 + 🏷️ ‼️‼️   (🚫🚫🚫 — `⌨️`🔗📁 🚫🙈 ; ⬜📜 : ASCII + 𓂀 + 😺)
# 📜 `🙊📜.md` — 🚧📜
# 📚 https://code.claude.com/docs/en/hooks
# 📥 `stdin`  `{"delta": "…"}`  →  📤 `stdout`  `{"hookSpecificOutput": {"hookEventName", "displayContent"}}`
import json
import re
import sys
import unicodedata

# 🙈  `⌨️` , 🔗 , 📁/
𓁹𓅂 = re.compile(
    r"`[^`\n]*`|(?i:\b[a-z][a-z0-9+.\-]*://\S+)|(?i:\bwww\.\S+)|\S*/\S*"
)

# 🗣️🔤  (`A-z` ASCII ☝️ — ¬ASCII 🔤 → 𓉗𓏤 🙊 👇)
𓊖 = re.compile(r"[A-Za-z]+")

# 🈲 ∀🏳️🌐 ¬🇺🇲🇬🇧  🚫🚫🚫  →  🙊❌   (⬜📜 ; 📜 🙊📜.md ; 🪞 `.github/𓊪𓂀𓅓.py`)
#   ✅ : ASCII U+0000-007F (😾🪜 👇) · 𓂀 U+13000-1342F · 😺🧷 U+200D U+FE0E U+FE0F U+20E3
#        · 😺🔣 ¬`L*` ¬`M*` ¬`Nl`  (② → — 0-9 … ✅)
#   🙊 : ∀🔤 `L*`/`M*`/`Nl`  (🇰🇷🇯🇵🇨🇳🇬🇷🇷🇺🇵🇱🇳🇴 … ∀🏳️) + 🪦👅 🤪😹 :
#        U+10000-12FFF (U+12000-1254F , U+10900 …) · U+1D000-1D0FF · U+1D200-1D24F
𓉗𓄤 = frozenset({0x200D, 0xFE0E, 0xFE0F, 0x20E3})
𓉗𓋆 = ((0x10000, 0x12FFF), (0x1D000, 0x1D0FF), (0x1D200, 0x1D24F))


def 𓉗𓏤(𓋁: str) -> bool:
    # ❓ 🈲🔣   (⬜📜 : ✅ → False)
    𓈙 = ord(𓋁)
    if 𓈙 <= 0x7F or 0x13000 <= 𓈙 <= 0x1342F or 𓈙 in 𓉗𓄤:
        return False                                # 🇺🇲🔤 · 𓂀 · 😺🧷
    if any(𓄿 <= 𓈙 <= 𓃀 for 𓄿, 𓃀 in 𓉗𓋆):
        return True                                 # 🪦👅
    𓊍 = unicodedata.category(𓋁)
    return 𓊍[0] in "LM" or 𓊍 == "Nl"               # ∀🏳️🌐 🔤 → 🙊


def 𓉗𓆛(𓆼: str) -> list:
    # 🈲🔣 🔍 → [🔣]   (🪝⛔ `𓊗𓆓.py` 🤝)
    return [𓋁 for 𓋁 in 𓆼 if 𓉗𓏤(𓋁)]


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
        𓋎 = "".join("🙊" if 𓉗𓏤(𓋁) else 𓋁 for 𓋁 in 𓋍)
        if 𓋎 != 𓋍:
            𓂏.append(𓋎 + 𓉗𓅱)                    # 🈲 🚫🚫🚫 — 🚫🙈
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
