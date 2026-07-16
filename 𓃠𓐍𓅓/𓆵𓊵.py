# 🗺️ 🧱🏭  —  🌲📚 · 🏜️🤏 · 🏔️🌀   →   🧱 set  ( 🔗✅ 🐈↔️🐭 )
#   ( 📤 𓋁 🀫 : 🚫 import 𓉔 → 🕳️🔁 🙈 ;  𓋁.𓊃 · 𓋁.𓃰 · 𓋁.𓁉 · 𓋁.𓃠 🤝 )
from __future__ import annotations

from .𓐍𓊵 import 𓈖𓊪, 𓈖𓏏, 𓎘
from .𓊞𓊵 import 𓆵𓊙


def 𓆵𓅓(𓋁, 𓈖: int, 𓆵𓉏: str | None) -> None:
    # 🗺️ 🧱🏭 :  🀫 → 🎯🔢 (×⚖️) + 📜  ( 🌲🎲📚 · 🏜️🎲🤏 · 🏔️🌀📍 )
    #            🔗✅ ‼️ : 𓋁.𓁉 ∈ 𓋁.𓃰(𓋁.𓃠) 🔒  ∨  ∅ ↩️ 🛡️  ( 🗿 ↩️🅾️ )
    𓆶 = max(0, round(𓈖 * 𓆵𓊙.get(𓆵𓉏, 1.0)))
    if 𓆵𓉏 == "🏔️":
        𓆵𓊱(𓋁, 𓆶)                       # 🌀-🥞 📍  ( ⭕→⭕ , 📚 ⊥ 🎲 )
    else:
        𓆵𓊰(𓋁, 𓆶)                       # 🎲 📍🌫️  ( 🌲 / 🏜️ / 🗿 ∅ )


def 𓆵𓊰(𓋁, 𓆶: int) -> None:
    # 🎲🧱 :  🀫📜 🔀 → 🧱 ≤ 𓆶 , 🔗✅ (🐈↔️🐭)  ∨  ∅ ↩️   ( 🗿 𓆵 🪞 )
    𓆖 = [(𓊪, 𓏏) for 𓊪 in range(𓈖𓊪) for 𓏏 in range(𓈖𓏏)]
    for _ in range(60):
        𓆗 = list(𓆖)
        𓋁.𓊃.shuffle(𓆗)
        𓆘: set[tuple[int, int]] = set()
        for 𓅘 in 𓆗:
            if len(𓆘) >= 𓆶:
                break
            if 𓅘 in (𓋁.𓃠, 𓋁.𓁉):        # 🐈🐭 🚫 🧱
                continue
            𓆘.add(𓅘)
        𓋁.𓊵 = 𓆘
        if 𓋁.𓁉 in 𓋁.𓃰(𓋁.𓃠):          # 🔗❓
            return
    𓋁.𓊵 = set()                          # 🏳️ ↩️🅾️


def 𓆵𓊱(𓋁, 𓆶: int) -> None:
    # 🏔️ 🌀-🥞 :  🧱 ↕️ 🥞 ( ⭕→⭕ , 📚 ⊥ 🎲 📍🌫️ ) , 🔗✅ (🐈↔️🐭)  ∨  ∅ ↩️
    for _ in range(60):
        𓆘: set[tuple[int, int]] = set()
        𓆙 = 0
        while len(𓆘) < 𓆶 and 𓆙 < 400:
            𓆙 += 1
            𓊪 = 𓋁.𓊃.randrange(𓈖𓊪)
            𓏏 = 𓋁.𓊃.randrange(𓈖𓏏)
            𓅬 = 𓋁.𓊃.randint(1, 3)         # 🥞 📏  ( 🌀 ↕️ )
            for 𓆚 in range(𓅬):
                if len(𓆘) >= 𓆶:
                    break
                𓅘 = (𓊪, 𓎘(𓏏 + 𓆚, 𓈖𓏏))
                if 𓅘 in (𓋁.𓃠, 𓋁.𓁉):    # 🐈🐭 🚫 🧱
                    continue
                𓆘.add(𓅘)
        𓋁.𓊵 = 𓆘
        if 𓋁.𓁉 in 𓋁.𓃰(𓋁.𓃠):          # 🔗❓
            return
    𓋁.𓊵 = set()                          # 🏳️ ↩️🅾️
