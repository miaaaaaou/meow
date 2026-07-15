# 🐈🎮🐭 — 𓃠 𓆲 𓅓 𓐍  ✨  🧱🗺️ + 🧭 BFS + 🐕😾 + 🐦🕊️ + 🕳️🌀
# ⬆️⬇️⬅️➡️ 🐾 … 🐈💨🐭 … 🐕💨🐈 … 🐦🕊️ … 🕳️🌀 … 🧱 … 🎯 → 😻😹😼
#
# 𓉻 𓐁 𓂀:  𓊪↔️  𓏏↕️  𓃠🐈  𓁉🐭  𓃥🐕  𓅱🐦  𓇬🧀  𓊵🧱  𓊟😿  𓅮🕊️  𓎛🕳️
from __future__ import annotations
import sys
import json
import random
from collections import deque

# ─────────── 💾🏆 📜🔝 ───────────
𓎋𓊪 = "🏆📜.json"    # 💾 default 🛤️  (🏁 classic)
𓎋𓊪𓋃 = "🏆📜⏳.json"  # 💾 ⏱️ time-attack 🛤️  (🏁 mode → own 📜🔝)
𓎋𓈖 = 10             # 📜🔝 keep top-N


def 𓎋(𓊪𓉏: str = 𓎋𓊪) -> list[dict]:
    # 📥  load 📜🔝  (🙀💔 → 📜🕳️)
    try:
        with open(𓊪𓉏, encoding="utf-8") as 𓆑:
            𓂭 = json.load(𓆑)
        if isinstance(𓂭, list):
            return [𓅘 for 𓅘 in 𓂭 if isinstance(𓅘, dict)]
    except (OSError, ValueError):
        pass
    return []


def 𓎌(𓆳: dict, 𓊪𓉏: str = 𓎋𓊪, 𓈖: int = 𓎋𓈖) -> list[dict]:
    # 📤  add 🆕 → sort 🔽🏆 (tie → 🔼⏱️) → ✂️ top-N → 💾
    𓂏 = 𓎋(𓊪𓉏)
    𓂏.append(𓆳)
    𓂏.sort(key=lambda 𓅘: (-𓅘.get("🏆", 0), 𓅘.get("⏱️", 0)))
    𓂏 = 𓂏[:𓈖]
    with open(𓊪𓉏, "w", encoding="utf-8") as 𓆑:
        json.dump(𓂏, 𓆑, ensure_ascii=False)
    return 𓂏


def 𓎍(𓂏: list[dict]) -> str:
    # 🖼️  📜🔝 render
    if not 𓂏:
        return "📜🕳️"
    𓂐 = ["🏆📜🔝"]
    for 𓇋, 𓆳 in enumerate(𓂏, 1):
        𓋏 = f"  ⏳{𓆳['⏳']}" if "⏳" in 𓆳 else ""   # ⏱️ 🏁 → ⏳ leftover
        𓂐.append(
            f"{𓇋}. 🏆{𓆳.get('🏆', 0)}  🎚️{𓆳.get('🎚️', 1)}  ⏱️{𓆳.get('⏱️', 0)}"
            f"  🐟{𓆳.get('🐟', 0)}  🥛{𓆳.get('🥛', 0)}"
            f"  🐦{𓆳.get('🐦', 0)}  😿{𓆳.get('😿', 0)}{𓋏}"
        )
    return "\n".join(𓂐)

# 🗺️ 📐
𓈖𓊪 = 11   # ↔️
𓈖𓏏 = 8    # ↕️

# 🧭  ⬆️⬇️⬅️➡️🐾
𓂃 = {
    "⬆️": (0, -1),
    "⬇️": (0, +1),
    "⬅️": (-1, 0),
    "➡️": (+1, 0),
    "🐾": (0, 0),
}

# 🔄  Δ → 🧭
𓂊𓈎 = {(0, -1): "⬆️", (0, +1): "⬇️", (-1, 0): "⬅️", (+1, 0): "➡️", (0, 0): "🐾"}


def 𓎘(𓆼: int, 𓊝: int) -> int:
    # 🚧  0 … 𓊝-1
    return max(0, min(𓊝 - 1, 𓆼))


def 𓐍(𓄿: tuple[int, int], 𓃀: tuple[int, int]) -> int:
    # 📏  (|Δ↔️| + |Δ↕️|)   (manhattan)
    return abs(𓄿[0] - 𓃀[0]) + abs(𓄿[1] - 𓃀[1])


def 𓎉(𓄿: tuple[int, int], 𓃀: tuple[int, int]) -> int:
    # 📐  max(|Δ↔️| , |Δ↕️|)   (chebyshev — 🕊️ 8🧭)
    return max(abs(𓄿[0] - 𓃀[0]), abs(𓄿[1] - 𓃀[1]))


class 𓉔:
    # 🏠🎮  🐈💨🐭  🧱
    # 👀  🐈 near → 🐭😱
    𓋴 = 3
    # 💨💨💨 → 💤  (🐭 stamina)
    𓎿 = 4
    # 🥛⚡  pounce ⏳ turns
    𓋨 = 4
    # 🥛⚡  pounce 📏 reach  (🐈🎯🐭 from afar)
    𓋩 = 2
    # 🐕  spawn 📏 ≥ from 🐈  (fair start)
    𓃥𓊞 = 5
    # 🐕💨  half-speed  (🐈🏃 head-start)  →  moves every 2️⃣ turns
    𓃥𓎿 = 2
    # 🐦🏆  bonus  (🐈🕊️😋 → +🏆)
    𓅯 = 7
    # 🧶  distract ⏳ turns  (🐕💨🎾 not 🐈)
    𓋬 = 3
    # 🧶  🐕👀🎾 sight 📐 (chebyshev) range
    𓋫 = 4
    # 🐾9️⃣  ❤️ start lives  (😿 bonk −1 , 0 → 🎮🔚)
    𓋹𓈖 = 9
    # 😻🔥  combo streak 🧢 cap  (🏆 ×min(🔥,5))
    𓋻𓈎 = 5
    # 🐭🐭  🎯 base 🏆 → 🔥 combo tally  (per 🐭 caught)
    𓁉𓊙 = 5
    # ⏱️  time-attack : ⏳ = 𓋃𓊞 + 𓋃𓎿 × 🌊   (opt-in ⚑)
    𓋃𓊞 = 40
    𓋃𓎿 = 8
    # ⏱️  ⏳ ≤ this → 🟥 flash  (🖼️ HUD)
    𓋃𓈎 = 5

    def __init__(𓋁, 𓊃: random.Random | None = None, 𓊵𓈖: int = 9,
                 𓃥𓁋: bool = True, 𓅱𓁋: bool = True, 𓎛𓁋: bool = True,
                 𓋃𓁋: bool = False):
        𓋁.𓊃 = 𓊃 or random.Random()
        𓋁.𓃠 = (0, 0)                        # 🐈
        𓋁.𓁉𓂋 = [(𓈖𓊪 - 1, 𓈖𓏏 - 1)]        # 🐭🐭 pack  (📍 list)
        𓋁.𓊚𓂋 = [0]                         # 😮‍💨 per 🐭  (fatigue)
        𓋁.𓁍 = 𓋁.𓁉𓂋[0]                   # 📍 last 🐭  (∀ 🎯 → 🖼️)
        𓋁.𓊵: set[tuple[int, int]] = set()   # 🧱
        𓋁.𓆵(𓊵𓈖)                            # 🧱🎲
        𓋁.𓎛: tuple[tuple[int, int], tuple[int, int]] | None = None  # 🕳️↔️🕳️
        if 𓎛𓁋:
            𓄾 = 𓋁.𓆙()                       # 🕳️ a
            𓄿 = 𓋁.𓆙((𓄾,))                  # 🕳️ b
            𓋁.𓎛 = (𓄾, 𓄿)                   # 🕳️↔️🕳️
        𓋁.𓇬 = 𓋁.𓆙(𓋁.𓎜())             # 🧀
        𓋁.𓆛 = 𓋁.𓆙((𓋁.𓇬, *𓋁.𓎜()))            # 🐟
        𓋁.𓊮 = 𓋁.𓆙((𓋁.𓇬, 𓋁.𓆛, *𓋁.𓎜()))    # 🥛
        𓋁.𓅱: tuple[int, int] | None = None  # 🐦
        if 𓅱𓁋:
            𓋁.𓅱 = 𓋁.𓆙((𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮, *𓋁.𓎜()))  # 🐦🎲
        𓋁.𓃥: tuple[int, int] | None = None  # 🐕
        if 𓃥𓁋:
            𓋁.𓃥 = 𓋁.𓃥𓆙()               # 🐕🎲 far
        𓋁.𓏰 = 0                             # ⏱️
        𓋁.𓊛 = 0                             # 🐟😋 (fish eaten)
        𓋁.𓊳 = 0                             # 🥛😋 (milk eaten)
        𓋁.𓊰 = 0                             # ⚡ (pounce turns)
        𓋁.𓊟 = 0                             # 😿 (🐕 bonks)
        𓋁.𓅮 = 0                             # 🐦😋 (birds caught)
        𓋁.𓄊 = False                         # 🎯😻
        𓋁.𓊍 = 1                             # 🎚️ 🌊 level
        𓋁.𓋭: tuple[int, int] | None = None  # 🧶🎾 yarn
        𓋁.𓋮 = 0                             # ⏳ 🧶 distract countdown
        𓋁.𓋯 = False                         # 🧶×1 thrown flag
        𓋁.𓋹 = 𓋁.𓋹𓈖                      # ❤️ lives (🐾9️⃣ nine-lives)
        𓋁.𓋺 = False                         # 💀 lose flag (❤️=0 🎮🔚)
        𓋁.𓋻 = 0                             # 🔥 combo streak
        𓋁.𓋼 = 0                             # 🏆 combo bonus accumulator
        𓋁.𓋃𓁋 = 𓋃𓁋                          # ⏱️ time-attack ⚑  (default 🚫)
        𓋁.𓋂 = 𓋃𓈖(1)                        # ⏳ budget left  (🌊 → 𓊆 rescales)

    # ─────────── 🐭🐭  pack 🏦 ───────────
    @property
    def 𓁉(𓋁) -> tuple[int, int]:
        # 🐭  head of pack  (🚧 back-compat : solo ↔️ 𓁉𓂋[0] ; ∀🎯 → 📍 last)
        return 𓋁.𓁉𓂋[0] if 𓋁.𓁉𓂋 else 𓋁.𓁍

    @𓁉.setter
    def 𓁉(𓋁, 𓅘: tuple[int, int]) -> None:
        if 𓋁.𓁉𓂋:
            𓋁.𓁉𓂋[0] = 𓅘
        else:
            𓋁.𓁉𓂋 = [𓅘]
            𓋁.𓊚𓂋 = [0]
        𓋁.𓁍 = 𓅘

    @property
    def 𓊚(𓋁) -> int:
        # 😮‍💨  head 🐭 fatigue  (🚧 back-compat)
        return 𓋁.𓊚𓂋[0] if 𓋁.𓊚𓂋 else 0

    @𓊚.setter
    def 𓊚(𓋁, 𓂘: int) -> None:
        if 𓋁.𓊚𓂋:
            𓋁.𓊚𓂋[0] = 𓂘
        else:
            𓋁.𓊚𓂋 = [𓂘]

    def 𓁉𓆙(𓋁) -> tuple[int, int]:
        # 🐭🎲 📍  🔗 from 🐈  ≠🐈🐭🐭🧀🐟🥛🐕🐦🕳️
        𓂭 = 𓋁.𓃰(𓋁.𓃠)
        𓆊 = {𓋁.𓃠, *𓋁.𓁉𓂋, 𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮,
              𓋁.𓃥, 𓋁.𓅱, *𓋁.𓎜()}
        𓊾 = sorted(𓅘 for 𓅘 in 𓂭 if 𓅘 not in 𓆊)
        if not 𓊾:
            return 𓋁.𓁉
        return 𓋁.𓊃.choice(𓊾)

    def 𓁎(𓋁, 𓈖: int) -> None:
        # 🐭🐭  pack grow → 𓈖 total  (🔗✅ ∀🐭 : 𓁉𓆙 picks from BFS 🗺️)
        while len(𓋁.𓁉𓂋) < 𓈖:
            𓋁.𓁉𓂋.append(𓋁.𓁉𓆙())
            𓋁.𓊚𓂋.append(0)

    def 𓁏(𓋁, 𓅘: tuple[int, int]) -> bool:
        # 🎯  catch 🐭 @ 📍 → pop + 🔥 combo ;  ∀🐭 gone → 😻
        if 𓅘 not in 𓋁.𓁉𓂋:
            return 𓋁.𓄊
        𓇋 = 𓋁.𓁉𓂋.index(𓅘)
        𓋁.𓁉𓂋.pop(𓇋)
        𓋁.𓊚𓂋.pop(𓇋)
        𓋁.𓁍 = 𓅘
        𓋁.𓋿(𓋁.𓁉𓊙)                 # 🔥 combo +1 / 🐭
        if not 𓋁.𓁉𓂋:
            𓋁.𓄊 = True                # 😻 ⇔ ∀🐭 🎯
        return 𓋁.𓄊

    # ─────────── 🧱🗺️ ───────────
    def 𓆵(𓋁, 𓈖: int) -> None:
        # 🧱🎲  …  🐈↔️🐭 must stay 🔗  (connected)
        𓆖 = [(𓊪, 𓏏) for 𓊪 in range(𓈖𓊪) for 𓏏 in range(𓈖𓏏)]
        for _ in range(60):
            𓆗 = list(𓆖)
            𓋁.𓊃.shuffle(𓆗)
            𓆘: set[tuple[int, int]] = set()
            for 𓅘 in 𓆗:
                if len(𓆘) >= 𓈖:
                    break
                if 𓅘 in (𓋁.𓃠, 𓋁.𓁉):
                    continue
                𓆘.add(𓅘)
            𓋁.𓊵 = 𓆘
            if 𓋁.𓁉 in 𓋁.𓃰(𓋁.𓃠):     # 🔗❓
                return
        𓋁.𓊵 = set()                         # 🏳️  fallback

    def 𓊇𓈎(𓋁, 𓅘: tuple[int, int]) -> list[tuple[int, int]]:
        # 🟩 neighbors  (skip 🧱 & 🧱edge)
        𓊾 = []
        for 𓊍, 𓂄 in 𓂃.items():
            if 𓊍 == "🐾":
                continue
            𓆓 = (𓎘(𓅘[0] + 𓂄[0], 𓈖𓊪), 𓎘(𓅘[1] + 𓂄[1], 𓈖𓏏))
            if 𓆓 == 𓅘 or 𓆓 in 𓋁.𓊵:
                continue
            𓊾.append(𓆓)
        return 𓊾

    def 𓃰(𓋁, 𓄿: tuple[int, int]) -> dict[tuple[int, int], int]:
        # 🧭  BFS 📏 map  from 𓄿  over 🟩
        𓂭 = {𓄿: 0}
        𓆱 = deque([𓄿])
        while 𓆱:
            𓂚 = 𓆱.popleft()
            for 𓆓 in 𓋁.𓊇𓈎(𓂚):
                if 𓆓 not in 𓂭:
                    𓂭[𓆓] = 𓂭[𓂚] + 1
                    𓆱.append(𓆓)
        return 𓂭

    def 𓊐(𓋁, 𓅘: tuple[int, int], 𓄿: tuple[int, int]) -> tuple[int, int]:
        # ➡️🎯  next 🟩 from 𓅘 toward 𓄿  (min BFS 📏)
        𓂭 = 𓋁.𓃰(𓄿)
        𓅒 = 𓂭.get(𓅘, 10 ** 9)
        𓅑 = 𓅘
        for 𓆓 in sorted(𓋁.𓊇𓈎(𓅘)):
            𓊈 = 𓂭.get(𓆓, 10 ** 9)
            if 𓊈 < 𓅒:
                𓅒 = 𓊈
                𓅑 = 𓆓
        return 𓅑

    def 𓂊(𓋁, 𓄿: tuple[int, int], 𓃀: tuple[int, int]) -> str:
        # Δ 🔄 🧭
        return 𓂊𓈎.get((𓃀[0] - 𓄿[0], 𓃀[1] - 𓄿[1]), "🐾")

    # ─────────── 📍🎲 ───────────
    def 𓎜(𓋁) -> tuple:
        # 🕳️ exclusion  (portal cells or ∅)
        return 𓋁.𓎛 if 𓋁.𓎛 is not None else ()

    def 𓎚(𓋁, 𓆓: tuple[int, int], 𓄿: tuple[int, int]) -> tuple[int, int]:
        # 🕳️ landing :  🐾 from 𓄿 → 𓆓 .  enter 🕳️ from 🚫🕳️ → twin ; else 𓆓
        if 𓋁.𓎛 is not None and 𓆓 in 𓋁.𓎛 and 𓄿 not in 𓋁.𓎛:
            return 𓋁.𓎛[1] if 𓆓 == 𓋁.𓎛[0] else 𓋁.𓎛[0]
        return 𓆓

    def 𓆙(𓋁, 𓊫: tuple[tuple[int, int], ...] = ()) -> tuple[int, int]:
        # 🎲 📍  🟩  🔗  ≠🐈🐭  ≠𓊫
        𓂭 = 𓋁.𓃰(𓋁.𓃠)
        𓆊 = {𓋁.𓃠, *𓋁.𓁉𓂋, *𓊫}
        𓊾 = sorted(𓅘 for 𓅘 in 𓂭 if 𓅘 not in 𓆊)
        if not 𓊾:
            return 𓋁.𓁉
        return 𓋁.𓊃.choice(𓊾)

    def 𓃥𓆙(𓋁) -> tuple[int, int]:
        # 🐕🎲 📍  🔗  ≠🐈🐭🧀🐟🥛🐦  📏🐈 ≥ 𓃥𓊞
        𓂭 = 𓋁.𓃰(𓋁.𓃠)
        𓆊 = {𓋁.𓃠, *𓋁.𓁉𓂋, 𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮, 𓋁.𓅱, *𓋁.𓎜()}
        𓊾 = sorted(𓅘 for 𓅘, 𓂘 in 𓂭.items() if 𓅘 not in 𓆊 and 𓂘 >= 𓋁.𓃥𓊞)
        if not 𓊾:                              # 🤏🗺️ fallback → any 🟩
            𓊾 = sorted(𓅘 for 𓅘 in 𓂭 if 𓅘 not in 𓆊)
        if not 𓊾:
            return 𓋁.𓁉
        return 𓋁.𓊃.choice(𓊾)

    def 𓎗(𓋁, 𓄿: tuple[int, int], 𓂄: tuple[int, int]) -> tuple[int, int]:
        # 🐾 → 📍′  🚧  🧱🚫
        𓆓 = (𓎘(𓄿[0] + 𓂄[0], 𓈖𓊪), 𓎘(𓄿[1] + 𓂄[1], 𓈖𓏏))
        if 𓆓 in 𓋁.𓊵:
            return 𓄿                           # 🧱 blocked
        return 𓆓

    def 𓂷(𓋁, 𓊍: str) -> bool:
        # 🐈 🐾 (or 🧶 throw) →  🐭💨  →  🎯❓
        𓋢 = 𓊍 == "🧶"                    # 🧶 throw intent → 🐾 stay
        if 𓋢:
            𓊍 = "🐾"
        if 𓊍 not in 𓂃:
            return False
        𓋁.𓏰 += 1
        if 𓋁.𓋃𓁋:                     # ⏱️ ⏳ tick  (∀🐾 → −1)
            𓋁.𓋂 -= 1
        if 𓋁.𓊰 > 0:                   # ⚡⏳ tick
            𓋁.𓊰 -= 1
        if 𓋁.𓋮 > 0:                   # 🧶⏳ tick → 💨 gone
            𓋁.𓋮 -= 1
            if 𓋁.𓋮 == 0:
                𓋁.𓋭 = None
        𓋉 = 𓋁.𓃠                       # 📍 prev
        𓋁.𓃠 = 𓋁.𓎚(𓋁.𓎗(𓋁.𓃠, 𓂃[𓊍]), 𓋉)  # 🐾 + 🕳️➡️🕳️
        if 𓋢:                            # 🧶 throw 🎾 📍🐈  (after 🐾 stay)
            𓋁.𓋰()
        if 𓋁.𓁏(𓋁.𓃠):              # 😻🎯  (∀🐭 → 🎮🔚)
            return True
        if 𓋁.𓃠 == 𓋁.𓇬:            # 🧀😋
            𓋁.𓇬 = 𓋁.𓆙((𓋁.𓆛, 𓋁.𓊮, 𓋁.𓃥, 𓋁.𓅱, *𓋁.𓎜()))
        if 𓋁.𓃠 == 𓋁.𓆛:            # 🐟😋
            𓋁.𓊛 += 1
            𓋁.𓋿(5)                    # 🔥 combo (🐟 base 5)
            𓋁.𓆛 = 𓋁.𓆙((𓋁.𓇬, 𓋁.𓊮, 𓋁.𓃥, 𓋁.𓅱, *𓋁.𓎜()))
        if 𓋁.𓃠 == 𓋁.𓊮:            # 🥛😋 → ⚡
            𓋁.𓊳 += 1
            𓋁.𓊰 = 𓋁.𓋨
            𓋁.𓋿(3)                    # 🔥 combo (🥛 base 3)
            𓋁.𓊮 = 𓋁.𓆙((𓋁.𓇬, 𓋁.𓆛, 𓋁.𓃥, 𓋁.𓅱, *𓋁.𓎜()))
        if 𓋁.𓅱 is not None and 𓋁.𓃠 == 𓋁.𓅱:   # 🐦😋 → 🏆
            𓋁.𓅮 += 1
            𓋁.𓋿(𓋁.𓅯)              # 🔥 combo (🐦 base 𓅯=7)
            𓋁.𓅱 = 𓋁.𓆙((𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮, 𓋁.𓃥, *𓋁.𓎜()))
        if 𓋁.𓊰 > 0:                   # 🥛⚡  🐈🎯 nearest 🐭 from afar
            𓂭 = 𓋁.𓃰(𓋁.𓃠)
            𓆉 = sorted((𓂭.get(𓅘, 999), 𓅘) for 𓅘 in 𓋁.𓁉𓂋)
            if 𓆉 and 𓆉[0][0] <= 𓋁.𓋩 and 𓋁.𓁏(𓆉[0][1]):
                return True
        for 𓇋 in range(len(𓋁.𓁉𓂋)):   # 🐭🐭💨  (∀ own 🧠)
            𓋁.𓁉𓂋[𓇋] = 𓋁.𓅓𓎗(𓇋)
        if 𓋁.𓅱 is not None:            # 🐦🕊️  flee
            𓋁.𓅱𓎗()
        if 𓋁.𓁏(𓋁.𓃠):              # 😹
            return True
        if 𓋁.𓃥 is not None and 𓋁.𓏰 % 𓋁.𓃥𓎿 == 0:
            𓋁.𓃥𓎗()                   # 🐕💨🐈  (half-speed)
        𓋁.𓁏(𓋁.𓃠)                  # 😹  (🐈🌀 → 🐭?)
        if 𓋁.𓋃𓁋 and 𓋁.𓋂 <= 0 and not 𓋁.𓄊:
            𓋁.𓋺 = True                # ⏱️ ⏳0 → 💀  (🚫😻 → lose)
        return 𓋁.𓄊 or 𓋁.𓋺         # 🎮🔚 : 😻 win or 💀 lose

    def 𓋾(𓋁) -> bool:
        # 🎮🔚  game over : 😻 catch or 💀 (❤️0 | ⏳0)
        return 𓋁.𓄊 or 𓋁.𓋺

    def 𓋿(𓋁, 𓃀: int) -> None:
        # 🔥 combo tally :  🔥+1 , 🏆 bonus += base × (min(🔥,🧢)−1)
        𓋁.𓋻 += 1
        𓋁.𓋼 += 𓃀 * (min(𓋁.𓋻, 𓋁.𓋻𓈎) - 1)

    def 𓋰(𓋁) -> None:
        # 🧶 throw :  🎾 📍🐈  (×1 / 🎮 , 🚫🧱)  → 🐕 distract ⏳
        if 𓋁.𓋯 or 𓋁.𓃠 in 𓋁.𓊵:
            return
        𓋁.𓋭 = 𓋁.𓃠
        𓋁.𓋮 = 𓋁.𓋬                 # ⏳ armed
        𓋁.𓋯 = True                    # ×1 spent

    def 𓃥𓎗(𓋁) -> None:
        # 🐕🧠 :  BFS 1️⃣🐾 →🐈 .  🐕👉🐈 → 😿 :  🐈🌀 safe restart , 🐕🎲 far
        if 𓋁.𓃥 is None:
            return
        if 𓋁.𓋭 is not None and 𓎉(𓋁.𓃥, 𓋁.𓋭) <= 𓋁.𓋫:
            𓋁.𓃥 = 𓋁.𓊐(𓋁.𓃥, 𓋁.𓋭)   # 🧶 distract : 💨🎾 , 🚫💨🐈
            return                        # 🚫 bonk while 🧶
        𓋁.𓃥 = 𓋁.𓊐(𓋁.𓃥, 𓋁.𓃠)
        if 𓋁.𓃥 == 𓋁.𓃠:            # 😿  bonk!
            𓋁.𓊟 += 1
            𓋁.𓋹 -= 1                   # ❤️ −1  (🐾9️⃣)
            𓋁.𓋻 = 0                    # 🔥 streak reset  (😻🔥)
            if 𓋁.𓋹 <= 0:              # 💀 0 ❤️ → 🎮🔚
                𓋁.𓋺 = True
                return
            𓋁.𓃠 = 𓋁.𓆙((𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮, 𓋁.𓃥, *𓋁.𓎜()))  # 🐈🌀
            𓋁.𓃥 = 𓋁.𓃥𓆙()         # 🐕🎲 far

    def 𓅓𓎗(𓋁, 𓇋: int = 0) -> tuple[int, int]:
        # 🐭🧠 :  🐈👀 near → 💨(max BFS📏🐈) ; 😮‍💨💤 rest ; else → 🧀😋(min BFS📏🧀)
        #        𓇋 = 🐭 index in 🐭🐭 pack  (∀🐭 own 🧠 + 😮‍💨)
        𓅐 = 𓋁.𓁉𓂋[𓇋]
        𓂭 = 𓋁.𓃰(𓋁.𓃠)             # 📏→🐈
        if 𓂭.get(𓅐, 999) <= 𓋁.𓋴:
            # 😱💨  …  😮‍💨💤❓
            if 𓋁.𓊚𓂋[𓇋] >= 𓋁.𓎿:
                𓋁.𓊚𓂋[𓇋] = 0
                return 𓅐                 # 💤
            𓋁.𓊚𓂋[𓇋] += 1
            𓅑 = 𓅐
            𓅒 = 𓂭.get(𓅐, 0)
            for 𓆓 in sorted(𓋁.𓊇𓈎(𓅐)):
                𓊈 = 𓂭.get(𓆓, 0)
                if 𓊈 > 𓅒:
                    𓅒 = 𓊈
                    𓅑 = 𓆓
            return 𓅑
        # 🧀😋
        𓋁.𓊚𓂋[𓇋] = 0
        return 𓋁.𓊐(𓅐, 𓋁.𓇬)

    def 𓅱𓎗(𓋁) -> None:
        # 🐦🧠 :  🕊️ fly 8🧭 , 🚫🧱 perch , 💨 max 📐(chebyshev)→🐈 , ≠ 🐭🐕🧀🐟🥛
        if 𓋁.𓅱 is None:
            return
        𓆊 = {*𓋁.𓁉𓂋, 𓋁.𓃥, 𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮}
        𓅑 = 𓋁.𓅱
        𓅒 = 𓎉(𓋁.𓅱, 𓋁.𓃠)             # 📐 now
        for 𓂄𓊪 in (-1, 0, 1):
            for 𓂄𓏏 in (-1, 0, 1):
                𓆓 = (𓎘(𓋁.𓅱[0] + 𓂄𓊪, 𓈖𓊪), 𓎘(𓋁.𓅱[1] + 𓂄𓏏, 𓈖𓏏))
                if 𓆓 == 𓋁.𓅱 or 𓆓 in 𓋁.𓊵 or 𓆓 in 𓆊:
                    continue
                𓊈 = 𓎉(𓆓, 𓋁.𓃠)
                if 𓊈 > 𓅒:
                    𓅒 = 𓊈
                    𓅑 = 𓆓
        𓋁.𓅱 = 𓅑

    def 𓊙(𓋁) -> int:
        # 🏆  ⚡fast + 🐟bonus + 🥛bonus + 🐦bonus + 🔥combo + ⏳leftover − 😿penalty
        return (max(0, 100 - 𓋁.𓏰 - 10 * 𓋁.𓊟)
                + 5 * 𓋁.𓊛 + 3 * 𓋁.𓊳 + 𓋁.𓅯 * 𓋁.𓅮 + 𓋁.𓋼
                + (max(0, 𓋁.𓋂) if 𓋁.𓋃𓁋 else 0))

    def 𓁑(𓋁) -> str:
        # 🖼️ HUD :  ❤️×N + 🐭×N pack + 🔥×N streak (≥3 → ✨) + ⏳×N (⚑ , ≤5 → 🟥)
        #        🀄 : ⏳ = budget left  ≠  ⏱️ = 𓏰 turns  (🚫 collide ‼️)
        𓋠 = f"❤️×{𓋁.𓋹}  🐭×{len(𓋁.𓁉𓂋)}  🔥×{𓋁.𓋻}"
        if 𓋁.𓋻 >= 3:
            𓋠 += "✨"
        if 𓋁.𓋃𓁋:                      # ⏱️ ⚑ on → ⏳ left  (🚫⚑ → 📺 ↔️)
            𓋠 += f"  ⏳×{max(0, 𓋁.𓋂)}"
            if 𓋁.𓋂 <= 𓋁.𓋃𓈎:
                𓋠 += "🟥"                # ⏳ low → 🟥 flash
        return 𓋠

    def 𓁐(𓋁) -> str:
        # 🖼️  🗺️
        𓂏 = []
        for 𓏏 in range(𓈖𓏏):
            𓂐 = []
            for 𓊪 in range(𓈖𓊪):
                𓅘 = (𓊪, 𓏏)
                if 𓅘 == 𓋁.𓃠:
                    𓂐.append("🐈")
                elif 𓅘 in 𓋁.𓁉𓂋:
                    𓂐.append("🐭")
                elif 𓅘 == 𓋁.𓃥:
                    𓂐.append("🐕")
                elif 𓅘 == 𓋁.𓅱:
                    𓂐.append("🐦")
                elif 𓅘 == 𓋁.𓋭:
                    𓂐.append("🎾")
                elif 𓅘 == 𓋁.𓇬:
                    𓂐.append("🧀")
                elif 𓅘 == 𓋁.𓆛:
                    𓂐.append("🐟")
                elif 𓅘 == 𓋁.𓊮:
                    𓂐.append("🥛")
                elif 𓋁.𓎛 is not None and 𓅘 in 𓋁.𓎛:
                    𓂐.append("🕳️")
                elif 𓅘 in 𓋁.𓊵:
                    𓂐.append("🧱")
                else:
                    𓂐.append("🟩")
            𓂏.append("".join(𓂐))
        return "\n".join(𓂏)


# 🐈🧠  🐾9️⃣ caution :  ❤️ low + 🐕 near → 💨 flee mode  (🚫💀 死 , 🚫 livelock)
𓊄𓋹 = 3   # ❤️ ≤ this → cautious
𓊄𓃥 = 2   # 🐕 BFS 📏 ≤ this → 💨 flee trigger
𓊄𓎿 = 3   # 🐕 📏 🧢 :  far 🐕 → 🚫 tie-break noise  (🚫 🕳️🌀 livelock)
𓊄𓋬 = 2   # 🐕 📏 ≤ this + 🧶 unspent → 🎾 throw  (🐕 distract → 🐈🎯🐭)


def 𓊄𓁉(𓉔𓏤: 𓉔) -> tuple[int, int]:
    # 🎯  nearest 🐭 of 🐭🐭 pack  (BFS 📏 from 🐈 , tie → 📍 sort)
    𓂭 = 𓉔𓏤.𓃰(𓉔𓏤.𓃠)
    if not 𓉔𓏤.𓁉𓂋:
        return 𓉔𓏤.𓁉
    return min(𓉔𓏤.𓁉𓂋, key=lambda 𓅘: (𓂭.get(𓅘, 10 ** 9), 𓅘))


def 𓊄(𓉔𓏤: 𓉔) -> str:
    # 🐈🧠  BFS →🐭 (nearest of 🐭🐭) , 🚫🐕 :  greedy (min 📏🐭 , tie max 📏🐕) ;
    #        ❤️≤3 + 🐕📏≤2 → 💨 flee (max 📏🐕 , tie min 📏🐭)  → 🚫9️⃣😿💀
    𓂭𓁉 = 𓉔𓏤.𓃰(𓊄𓁉(𓉔𓏤))                     # 📏→🐭 (🎯 nearest)
    𓂭𓃥 = 𓉔𓏤.𓃰(𓉔𓏤.𓃥) if 𓉔𓏤.𓃥 is not None else {}   # 📏→🐕
    𓂘𓃥 = 𓂭𓃥.get(𓉔𓏤.𓃠, 10 ** 9)             # 📏 🐈↔️🐕
    𓋞 = (𓉔𓏤.𓃥 is not None                    # 💨 flee❓  ❤️低 + 🐕近
          and 𓉔𓏤.𓋹 <= 𓊄𓋹
          and 𓂘𓃥 <= 𓊄𓃥)
    if 𓉔𓏤.𓃥 is not None and not 𓉔𓏤.𓋯 and 𓂘𓃥 <= 𓊄𓋬:
        return "🧶"                            # 🎾 throw → 🐕💨🎾 ⏳ , 🐈🎯🐭 free
    𓅑 = 𓉔𓏤.𓃠
    𓅒 = None
    for 𓆓 in [𓉔𓏤.𓃠] + sorted(𓉔𓏤.𓊇𓈎(𓉔𓏤.𓃠)):
        if 𓆓 == 𓉔𓏤.𓃥:                        # 🚫🐕
            continue
        𓂚 = 𓉔𓏤.𓎚(𓆓, 𓉔𓏤.𓃠)                 # 🕳️ landing  (portal shortcut)
        if 𓂚 == 𓉔𓏤.𓃥:                        # 🚫🐕 land
            continue
        𓃀𓁉 = 𓂭𓁉.get(𓂚, 10 ** 9)              # 📏🐭
        𓃀𓃥 = 𓂭𓃥.get(𓂚, 10 ** 9)              # 📏🐕  (raw : 💨 flee → 🕳️🌀 far ✅)
        # 🎯 chase : 🧢 📏🐕 → 🐕远 = 🚫 tie-break noise  (🚫 ↔️↔️ livelock)
        𓊈 = (-𓃀𓃥, 𓃀𓁉) if 𓋞 else (𓃀𓁉, -min(𓃀𓃥, 𓊄𓎿))
        if 𓅒 is None or 𓊈 < 𓅒:
            𓅒 = 𓊈
            𓅑 = 𓆓
    return 𓉔𓏤.𓂊(𓉔𓏤.𓃠, 𓅑)


def 𓎎(𓉔𓏤: 𓉔) -> dict:
    # 📇  🎮 → 📜 record  ( ⏱️ 🏁 → ➕ ⏳ leftover marker )
    𓆳 = {
        "🏆": 𓉔𓏤.𓊙(), "🎚️": 𓉔𓏤.𓊍, "⏱️": 𓉔𓏤.𓏰, "🐟": 𓉔𓏤.𓊛,
        "🥛": 𓉔𓏤.𓊳, "🐦": 𓉔𓏤.𓅮, "😿": 𓉔𓏤.𓊟,
    }
    if 𓉔𓏤.𓋃𓁋:
        𓆳["⏳"] = max(0, 𓉔𓏤.𓋂)          # ⏱️ 🏁 tag  (🚫⚑ → 🚫 key)
    return 𓆳


def 𓎋𓉏(𓉔𓏤: 𓉔) -> str:
    # 💾 🛤️  by 🏁 mode :  ⏱️ → 🏆📜⏳.json  ;  classic → 🏆📜.json
    # 🚫 pollute : ⏱️ 🏆 ➕ ⏳ bonus ≫ classic 🏆 → 📜🔝 split ‼️
    return 𓎋𓊪𓋃 if 𓉔𓏤.𓋃𓁋 else 𓎋𓊪


# ─────────── 🌈 🎨📺 ───────────
𓋊𓊞 = {   # 🀄 → ANSI 🎨  (🟩🌿 , 🟥🐕 , 🟦🥛 , 🟨🧀 …)
    "🐈": "35", "🐭": "37", "🐕": "31", "🐦": "36", "🎾": "95",
    "🧀": "33", "🐟": "94", "🥛": "34", "🕳️": "95", "🧱": "90", "🟩": "32",
    "❤️": "91", "🔥": "93",   # 🟥❤️ lives , 🟧🔥 streak
    "⏳": "96", "🟥": "91",   # 🟦⏳ budget , 🟥 flash  (⏳ ≤ 𓋃𓈎)
}


def 𓋊(𓊞: str, 𓋉: bool = False) -> str:
    # 🌈  🀄 → ANSI wrap  (🚫⚑ → 📺 ↔️ plain , 🚫💥 🖼️👴)
    if not 𓋉:
        return 𓊞
    for 𓅕, 𓂭 in 𓋊𓊞.items():
        𓊞 = 𓊞.replace(𓅕, f"\033[{𓂭}m{𓅕}\033[0m")
    return 𓊞


# ─────────── 🎚️ 🌊 difficulty ───────────
𓊆𓈖 = 9   # 🌊 max 🎚️  (levels 1️⃣..9️⃣)
𓁉𓈎 = 4   # 🐭🐭 pack 🧢 cap
𓁉𓊞 = 5   # 🐭🐭 pack @ 🌊 ≥ this  (🌊< → solo 🐭)


def 𓋃𓈖(𓊍: int) -> int:
    # ⏱️  ⏳ budget @ 🌊 :  40 + 8×🌊   (🌊⬆️ → ⏳⬆️ , 🧱⬆️🐭🐭⬆️ 🤝)
    return 𓉔.𓋃𓊞 + 𓉔.𓋃𓎿 * 𓊍


def 𓁉𓈖(𓊍: int) -> int:
    # 🐭🐭  pack size @ 🌊 :  🌊<5 → 1 ; else 1 + (🌊−4)//2  , 🧢 ×4
    if 𓊍 < 𓁉𓊞:
        return 1
    return min(𓁉𓈎, 1 + (𓊍 - (𓁉𓊞 - 1)) // 2)


def 𓊆(𓊍: int = 1, 𓊃: random.Random | None = None, 𓋃𓁋: bool = False) -> 𓉔:
    # 🎚️  🌊 1..9 → scaled 🏠🎮 :  🧱↑ , 🐕@≥2 , 🐦@≥3 , 🕳️@≥4 , 👀🐭@≥5 ,
    #                              🐭🐭@≥5 , 💨🐕@≥7  ;  ⏱️ ⚑ → ⏳=40+8×🌊
    𓊍 = 𓎘(𓊍 - 1, 𓊆𓈖) + 1                  # 🚧 1..9
    𓉔𓏤 = 𓉔(
        𓊃,
        𓊵𓈖=2 + 2 * 𓊍,                       # 🧱 4..20
        𓃥𓁋=𓊍 >= 2,                          # 🐕 @ ≥2
        𓅱𓁋=𓊍 >= 3,                          # 🐦 @ ≥3
        𓎛𓁋=𓊍 >= 4,                          # 🕳️ @ ≥4
        𓋃𓁋=𓋃𓁋,                             # ⏱️ opt-in ⚑
    )
    𓉔𓏤.𓋂 = 𓋃𓈖(𓊍)                          # ⏱️ ⏳ = f(🌊)
    if 𓊍 >= 5:
        𓉔𓏤.𓋴 = 4                            # 🐭👀 sharper (flee sooner)
    𓉔𓏤.𓁎(𓁉𓈖(𓊍))                           # 🐭🐭 pack  (🌊≥5 → ×K)
    if 𓊍 >= 7:
        𓉔𓏤.𓃥𓎿 = 1                          # 🐕💨 full-speed (🚫 half)
    𓉔𓏤.𓊍 = 𓊍                               # 🎚️ tag
    return 𓉔𓏤


def 𓆲(𓊃𓏤: int = 7, 𓏲: int = 200, 𓊍: int = 1, 𓋉: bool = False,
      𓋃𓁋: bool = False) -> 𓉔:
    # 🤖🎬  🐈💨🐭🐭  (auto)  @ 🎚️ 🌊  , 🌈 optional , ⏱️ optional
    𓉔𓏤 = 𓊆(𓊍, random.Random(𓊃𓏤), 𓋃𓁋)
    print(f"😺🎬  🎚️{𓉔𓏤.𓊍}  {𓋊(𓉔𓏤.𓁑(), 𓋉)}")
    print(𓋊(𓉔𓏤.𓁐(), 𓋉))
    for _ in range(𓏲):
        𓆳 = 𓊄(𓉔𓏤)
        if 𓉔𓏤.𓂷(𓆳):
            break
    print("┈┈┈┈┈┈┈┈┈┈┈")
    print(𓋊(𓉔𓏤.𓁐(), 𓋉))
    if 𓉔𓏤.𓄊:
        print(f"😻🎯  ⏱️={𓉔𓏤.𓏰}  🐟×{𓉔𓏤.𓊛}  🥛×{𓉔𓏤.𓊳}  🐦×{𓉔𓏤.𓅮}  😿×{𓉔𓏤.𓊟}  {𓋊(𓉔𓏤.𓁑(), 𓋉)}  🏆={𓉔𓏤.𓊙()}  prrr~")
        print("┈┈┈┈┈┈┈┈┈┈┈")
        print(𓎍(𓎌(𓎎(𓉔𓏤), 𓎋𓉏(𓉔𓏤))))   # 💾🏆 → 📜🔝  (🏁 mode 🛤️)
    elif 𓉔𓏤.𓋺:
        print(𓋺𓁐(𓉔𓏤))                # 💀 : ⏳0 or ❤️0
        print("┈┈┈┈┈┈┈┈┈┈┈")
        print(𓎍(𓎌(𓎎(𓉔𓏤), 𓎋𓉏(𓉔𓏤))))   # 💾🏆 → 📜🔝  (💀 also 📜)
    else:
        print("🙀💨  meow…")
    return 𓉔𓏤


def 𓋺𓁐(𓉔𓏤: 𓉔) -> str:
    # 💀 🖼️ :  🐕 ❤️0  🥇  |  ⏳0 ⏱️  (🀄 ⏳ ≠ ⏱️)
    if 𓉔𓏤.𓋹 <= 0:                    # ❤️0 🥇  (⚔️ ⏳0 🀄 🐾 → 🐕 wins)
        return (f"💀🐕  ❤️×0  ⏱️={𓉔𓏤.𓏰}  😿×{𓉔𓏤.𓊟}"
                f"  🏆={𓉔𓏤.𓊙()}  meow…")
    return (f"💀⏳  ⏳×0  🐭×{len(𓉔𓏤.𓁉𓂋)}  ⏱️={𓉔𓏤.𓏰}"
            f"  ❤️×{𓉔𓏤.𓋹}  😿×{𓉔𓏤.𓊟}  🏆={𓉔𓏤.𓊙()}  meow…")


def 𓊪𓏰(𓊍: int = 1, 𓋉: bool = False, 𓋃𓁋: bool = False):
    # 🕹️  🐈  ⌨️⬆️⬇️⬅️➡️/🀄🐾   🧶=throw   🙀=🚪   @ 🎚️ 🌊  , 🌈 , ⏱️ optional
    𓉔𓏤 = 𓊆(𓊍, None, 𓋃𓁋)
    print(f"😺🕹️  🎚️{𓉔𓏤.𓊍}  ⌨️⬆️⬇️⬅️➡️ | 🀄⬆️⬇️⬅️➡️🐾   🧶=🎾   🙀=🚪")
    while not 𓉔𓏤.𓋾():
        print(𓋊(𓉔𓏤.𓁐(), 𓋉))
        𓋛 = "🚧" if 𓉔𓏤.𓋯 else "🎾"
        print(f"⏱️={𓉔𓏤.𓏰}  🐈{𓉔𓏤.𓃠} 🐭{𓉔𓏤.𓁉𓂋} 🐕{𓉔𓏤.𓃥} 🐦{𓉔𓏤.𓅱}  ⚡{𓉔𓏤.𓊰}  🧶{𓋛}{𓉔𓏤.𓋮}  {𓋊(𓉔𓏤.𓁑(), 𓋉)}  😿×{𓉔𓏤.𓊟}")
        try:
            𓂺 = input("🐾❓ ")
        except (EOFError, KeyboardInterrupt):
            print("\n👋😼")
            return
        𓊾𓏤 = 𓎏(𓂺)                    # ⌨️ ⎋[C → ▶️  (#23)
        if not 𓊾𓏤:
            print("🤔❓")
            continue
        for 𓊍 in 𓊾𓏤:                  # ⌨️⌨️ hold → 🐾🐾
            if 𓊍 in ("🙀", "🚪", "q"):
                print("👋😼")
                return
            if 𓊍 not in 𓂃 and 𓊍 != "🧶":
                print("🤔❓")
                break
            𓉔𓏤.𓂷(𓊍)
            if 𓉔𓏤.𓋾():               # 🎮🔚 mid-📜 → ✂️
                break
    print(𓋊(𓉔𓏤.𓁐(), 𓋉))
    if 𓉔𓏤.𓄊:
        print(f"😻🎯  ⏱️={𓉔𓏤.𓏰}  🐟×{𓉔𓏤.𓊛}  🥛×{𓉔𓏤.𓊳}  🐦×{𓉔𓏤.𓅮}  😿×{𓉔𓏤.𓊟}  {𓋊(𓉔𓏤.𓁑(), 𓋉)}  🏆={𓉔𓏤.𓊙()}  prrr~")
    else:
        print(𓋺𓁐(𓉔𓏤))                # 💀 : ⏳0 or ❤️0
    print("┈┈┈┈┈┈┈┈┈┈┈")
    print(𓎍(𓎌(𓎎(𓉔𓏤), 𓎋𓉏(𓉔𓏤))))   # 💾🏆 → 📜🔝  (🏁 mode 🛤️)


# ─────────── ⌨️ 🕹️ 🐾 reader ───────────
𓎏𓊞 = {"A": "⬆️", "B": "⬇️", "C": "➡️", "D": "⬅️"}   # ⎋[𓅕 / ⎋O𓅕 → 🧭
𓎏𓉏 = "\x1b"                                        # ⎋  ESC


def 𓎏(𓅕: str) -> list[str]:
    # ⌨️ 🐾 reader :  ⎋[A ⎋[B ⎋[C ⎋[D  (+ ⎋O𓅕 app-mode , `^[` 📺 echo)
    #                → 🔼🔽▶️◀️  , ∀ seq in 📜 (⌨️⌨️ hold → 🐾🐾)
    #                🚫⎋ → 🔤 as-is  (🀄 emoji ↔️ , 🚫💥)
    𓂺 = 𓅕.replace("^[", 𓎏𓉏).strip()
    if 𓎏𓉏 not in 𓂺:
        return [𓂺] if 𓂺 else []
    𓊾: list[str] = []
    𓇋 = 0
    while 𓇋 < len(𓂺):
        if (𓂺[𓇋] == 𓎏𓉏 and 𓂺[𓇋 + 1:𓇋 + 2] in ("[", "O")
                and 𓂺[𓇋 + 2:𓇋 + 3] in 𓎏𓊞):
            𓊾.append(𓎏𓊞[𓂺[𓇋 + 2]])
            𓇋 += 3
        else:
            𓇋 += 1                                 # 🚮 ⎋ noise  (solo ⎋ , 🚫🧭)
    return 𓊾


def 𓊆𓂺(𓊾: list[str]) -> int:
    # 🎚️  parse 🌊 level from 🏁 args  (digits or 1️⃣…9️⃣) → 1..9  (default 1)
    𓅔 = {"1️⃣": 1, "2️⃣": 2, "3️⃣": 3, "4️⃣": 4, "5️⃣": 5,
          "6️⃣": 6, "7️⃣": 7, "8️⃣": 8, "9️⃣": 9}
    for 𓅕 in 𓊾:
        if 𓅕 in 𓅔:
            return 𓅔[𓅕]
        if 𓅕.isdigit():
            return 𓎘(int(𓅕) - 1, 𓊆𓈖) + 1
    return 1


if __name__ == "__main__":
    𓊾 = sys.argv[1:]
    𓊍𓏤 = 𓊆𓂺(𓊾)
    𓋉𓏤 = "🌈" in 𓊾                                    # ⚑🌈
    𓋃𓏤 = "⏱️" in 𓊾 or "⏳" in 𓊾                       # ⚑⏱️  time-attack
    if any(𓅕 in ("🤖", "🎬", "--🤖") for 𓅕 in 𓊾):
        𓆲(𓊍=𓊍𓏤, 𓋉=𓋉𓏤, 𓋃𓁋=𓋃𓏤)
    else:
        𓊪𓏰(𓊍𓏤, 𓋉𓏤, 𓋃𓏤)
