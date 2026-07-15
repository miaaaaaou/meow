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
𓎋𓊪 = "🏆📜.json"   # 💾 default 🛤️
𓎋𓈖 = 10            # 📜🔝 keep top-N


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
        𓂐.append(
            f"{𓇋}. 🏆{𓆳.get('🏆', 0)}  🎚️{𓆳.get('🎚️', 1)}  ⏱️{𓆳.get('⏱️', 0)}"
            f"  🐟{𓆳.get('🐟', 0)}  🥛{𓆳.get('🥛', 0)}"
            f"  🐦{𓆳.get('🐦', 0)}  😿{𓆳.get('😿', 0)}"
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

    def __init__(self, 𓊃: random.Random | None = None, 𓊵𓈖: int = 9,
                 𓃥𓁋: bool = True, 𓅱𓁋: bool = True, 𓎛𓁋: bool = True):
        self.𓊃 = 𓊃 or random.Random()
        self.𓃠 = (0, 0)                        # 🐈
        self.𓁉𓂋 = [(𓈖𓊪 - 1, 𓈖𓏏 - 1)]        # 🐭🐭 pack  (📍 list)
        self.𓊚𓂋 = [0]                         # 😮‍💨 per 🐭  (fatigue)
        self.𓁍 = self.𓁉𓂋[0]                   # 📍 last 🐭  (∀ 🎯 → 🖼️)
        self.𓊵: set[tuple[int, int]] = set()   # 🧱
        self.𓆵(𓊵𓈖)                            # 🧱🎲
        self.𓎛: tuple[tuple[int, int], tuple[int, int]] | None = None  # 🕳️↔️🕳️
        if 𓎛𓁋:
            𓄾 = self.𓆙()                       # 🕳️ a
            𓄿 = self.𓆙((𓄾,))                  # 🕳️ b
            self.𓎛 = (𓄾, 𓄿)                   # 🕳️↔️🕳️
        self.𓇬 = self.𓆙(self.𓎜())             # 🧀
        self.𓆛 = self.𓆙((self.𓇬, *self.𓎜()))            # 🐟
        self.𓊮 = self.𓆙((self.𓇬, self.𓆛, *self.𓎜()))    # 🥛
        self.𓅱: tuple[int, int] | None = None  # 🐦
        if 𓅱𓁋:
            self.𓅱 = self.𓆙((self.𓇬, self.𓆛, self.𓊮, *self.𓎜()))  # 🐦🎲
        self.𓃥: tuple[int, int] | None = None  # 🐕
        if 𓃥𓁋:
            self.𓃥 = self.𓃥𓆙()               # 🐕🎲 far
        self.𓏰 = 0                             # ⏱️
        self.𓊛 = 0                             # 🐟😋 (fish eaten)
        self.𓊳 = 0                             # 🥛😋 (milk eaten)
        self.𓊰 = 0                             # ⚡ (pounce turns)
        self.𓊟 = 0                             # 😿 (🐕 bonks)
        self.𓅮 = 0                             # 🐦😋 (birds caught)
        self.𓄊 = False                         # 🎯😻
        self.𓊍 = 1                             # 🎚️ 🌊 level
        self.𓋭: tuple[int, int] | None = None  # 🧶🎾 yarn
        self.𓋮 = 0                             # ⏳ 🧶 distract countdown
        self.𓋯 = False                         # 🧶×1 thrown flag
        self.𓋹 = self.𓋹𓈖                      # ❤️ lives (🐾9️⃣ nine-lives)
        self.𓋺 = False                         # 💀 lose flag (❤️=0 🎮🔚)
        self.𓋻 = 0                             # 🔥 combo streak
        self.𓋼 = 0                             # 🏆 combo bonus accumulator

    # ─────────── 🐭🐭  pack 🏦 ───────────
    @property
    def 𓁉(self) -> tuple[int, int]:
        # 🐭  head of pack  (🚧 back-compat : solo ↔️ 𓁉𓂋[0] ; ∀🎯 → 📍 last)
        return self.𓁉𓂋[0] if self.𓁉𓂋 else self.𓁍

    @𓁉.setter
    def 𓁉(self, 𓅘: tuple[int, int]) -> None:
        if self.𓁉𓂋:
            self.𓁉𓂋[0] = 𓅘
        else:
            self.𓁉𓂋 = [𓅘]
            self.𓊚𓂋 = [0]
        self.𓁍 = 𓅘

    @property
    def 𓊚(self) -> int:
        # 😮‍💨  head 🐭 fatigue  (🚧 back-compat)
        return self.𓊚𓂋[0] if self.𓊚𓂋 else 0

    @𓊚.setter
    def 𓊚(self, 𓂘: int) -> None:
        if self.𓊚𓂋:
            self.𓊚𓂋[0] = 𓂘
        else:
            self.𓊚𓂋 = [𓂘]

    def 𓁉𓆙(self) -> tuple[int, int]:
        # 🐭🎲 📍  🔗 from 🐈  ≠🐈🐭🐭🧀🐟🥛🐕🐦🕳️
        𓂭 = self.𓃰(self.𓃠)
        𓆊 = {self.𓃠, *self.𓁉𓂋, self.𓇬, self.𓆛, self.𓊮,
              self.𓃥, self.𓅱, *self.𓎜()}
        𓊾 = sorted(𓅘 for 𓅘 in 𓂭 if 𓅘 not in 𓆊)
        if not 𓊾:
            return self.𓁉
        return self.𓊃.choice(𓊾)

    def 𓁎(self, 𓈖: int) -> None:
        # 🐭🐭  pack grow → 𓈖 total  (🔗✅ ∀🐭 : 𓁉𓆙 picks from BFS 🗺️)
        while len(self.𓁉𓂋) < 𓈖:
            self.𓁉𓂋.append(self.𓁉𓆙())
            self.𓊚𓂋.append(0)

    def 𓁏(self, 𓅘: tuple[int, int]) -> bool:
        # 🎯  catch 🐭 @ 📍 → pop + 🔥 combo ;  ∀🐭 gone → 😻
        if 𓅘 not in self.𓁉𓂋:
            return self.𓄊
        𓇋 = self.𓁉𓂋.index(𓅘)
        self.𓁉𓂋.pop(𓇋)
        self.𓊚𓂋.pop(𓇋)
        self.𓁍 = 𓅘
        self.𓋿(self.𓁉𓊙)                 # 🔥 combo +1 / 🐭
        if not self.𓁉𓂋:
            self.𓄊 = True                # 😻 ⇔ ∀🐭 🎯
        return self.𓄊

    # ─────────── 🧱🗺️ ───────────
    def 𓆵(self, 𓈖: int) -> None:
        # 🧱🎲  …  🐈↔️🐭 must stay 🔗  (connected)
        𓆖 = [(𓊪, 𓏏) for 𓊪 in range(𓈖𓊪) for 𓏏 in range(𓈖𓏏)]
        for _ in range(60):
            𓆗 = list(𓆖)
            self.𓊃.shuffle(𓆗)
            𓆘: set[tuple[int, int]] = set()
            for 𓅘 in 𓆗:
                if len(𓆘) >= 𓈖:
                    break
                if 𓅘 in (self.𓃠, self.𓁉):
                    continue
                𓆘.add(𓅘)
            self.𓊵 = 𓆘
            if self.𓁉 in self.𓃰(self.𓃠):     # 🔗❓
                return
        self.𓊵 = set()                         # 🏳️  fallback

    def 𓊇𓈎(self, 𓅘: tuple[int, int]) -> list[tuple[int, int]]:
        # 🟩 neighbors  (skip 🧱 & 🧱edge)
        𓊾 = []
        for 𓊍, 𓂄 in 𓂃.items():
            if 𓊍 == "🐾":
                continue
            𓆓 = (𓎘(𓅘[0] + 𓂄[0], 𓈖𓊪), 𓎘(𓅘[1] + 𓂄[1], 𓈖𓏏))
            if 𓆓 == 𓅘 or 𓆓 in self.𓊵:
                continue
            𓊾.append(𓆓)
        return 𓊾

    def 𓃰(self, 𓄿: tuple[int, int]) -> dict[tuple[int, int], int]:
        # 🧭  BFS 📏 map  from 𓄿  over 🟩
        𓂭 = {𓄿: 0}
        𓆱 = deque([𓄿])
        while 𓆱:
            𓂚 = 𓆱.popleft()
            for 𓆓 in self.𓊇𓈎(𓂚):
                if 𓆓 not in 𓂭:
                    𓂭[𓆓] = 𓂭[𓂚] + 1
                    𓆱.append(𓆓)
        return 𓂭

    def 𓊐(self, 𓅘: tuple[int, int], 𓄿: tuple[int, int]) -> tuple[int, int]:
        # ➡️🎯  next 🟩 from 𓅘 toward 𓄿  (min BFS 📏)
        𓂭 = self.𓃰(𓄿)
        𓅒 = 𓂭.get(𓅘, 10 ** 9)
        𓅑 = 𓅘
        for 𓆓 in sorted(self.𓊇𓈎(𓅘)):
            𓊈 = 𓂭.get(𓆓, 10 ** 9)
            if 𓊈 < 𓅒:
                𓅒 = 𓊈
                𓅑 = 𓆓
        return 𓅑

    def 𓂊(self, 𓄿: tuple[int, int], 𓃀: tuple[int, int]) -> str:
        # Δ 🔄 🧭
        return 𓂊𓈎.get((𓃀[0] - 𓄿[0], 𓃀[1] - 𓄿[1]), "🐾")

    # ─────────── 📍🎲 ───────────
    def 𓎜(self) -> tuple:
        # 🕳️ exclusion  (portal cells or ∅)
        return self.𓎛 if self.𓎛 is not None else ()

    def 𓎚(self, 𓆓: tuple[int, int], 𓄿: tuple[int, int]) -> tuple[int, int]:
        # 🕳️ landing :  🐾 from 𓄿 → 𓆓 .  enter 🕳️ from 🚫🕳️ → twin ; else 𓆓
        if self.𓎛 is not None and 𓆓 in self.𓎛 and 𓄿 not in self.𓎛:
            return self.𓎛[1] if 𓆓 == self.𓎛[0] else self.𓎛[0]
        return 𓆓

    def 𓆙(self, 𓊫: tuple[tuple[int, int], ...] = ()) -> tuple[int, int]:
        # 🎲 📍  🟩  🔗  ≠🐈🐭  ≠𓊫
        𓂭 = self.𓃰(self.𓃠)
        𓆊 = {self.𓃠, *self.𓁉𓂋, *𓊫}
        𓊾 = sorted(𓅘 for 𓅘 in 𓂭 if 𓅘 not in 𓆊)
        if not 𓊾:
            return self.𓁉
        return self.𓊃.choice(𓊾)

    def 𓃥𓆙(self) -> tuple[int, int]:
        # 🐕🎲 📍  🔗  ≠🐈🐭🧀🐟🥛🐦  📏🐈 ≥ 𓃥𓊞
        𓂭 = self.𓃰(self.𓃠)
        𓆊 = {self.𓃠, *self.𓁉𓂋, self.𓇬, self.𓆛, self.𓊮, self.𓅱, *self.𓎜()}
        𓊾 = sorted(𓅘 for 𓅘, 𓂘 in 𓂭.items() if 𓅘 not in 𓆊 and 𓂘 >= self.𓃥𓊞)
        if not 𓊾:                              # 🤏🗺️ fallback → any 🟩
            𓊾 = sorted(𓅘 for 𓅘 in 𓂭 if 𓅘 not in 𓆊)
        if not 𓊾:
            return self.𓁉
        return self.𓊃.choice(𓊾)

    def 𓎗(self, 𓄿: tuple[int, int], 𓂄: tuple[int, int]) -> tuple[int, int]:
        # 🐾 → 📍′  🚧  🧱🚫
        𓆓 = (𓎘(𓄿[0] + 𓂄[0], 𓈖𓊪), 𓎘(𓄿[1] + 𓂄[1], 𓈖𓏏))
        if 𓆓 in self.𓊵:
            return 𓄿                           # 🧱 blocked
        return 𓆓

    def 𓂷(self, 𓊍: str) -> bool:
        # 🐈 🐾 (or 🧶 throw) →  🐭💨  →  🎯❓
        𓋢 = 𓊍 == "🧶"                    # 🧶 throw intent → 🐾 stay
        if 𓋢:
            𓊍 = "🐾"
        if 𓊍 not in 𓂃:
            return False
        self.𓏰 += 1
        if self.𓊰 > 0:                   # ⚡⏳ tick
            self.𓊰 -= 1
        if self.𓋮 > 0:                   # 🧶⏳ tick → 💨 gone
            self.𓋮 -= 1
            if self.𓋮 == 0:
                self.𓋭 = None
        𓋉 = self.𓃠                       # 📍 prev
        self.𓃠 = self.𓎚(self.𓎗(self.𓃠, 𓂃[𓊍]), 𓋉)  # 🐾 + 🕳️➡️🕳️
        if 𓋢:                            # 🧶 throw 🎾 📍🐈  (after 🐾 stay)
            self.𓋰()
        if self.𓁏(self.𓃠):              # 😻🎯  (∀🐭 → 🎮🔚)
            return True
        if self.𓃠 == self.𓇬:            # 🧀😋
            self.𓇬 = self.𓆙((self.𓆛, self.𓊮, self.𓃥, self.𓅱, *self.𓎜()))
        if self.𓃠 == self.𓆛:            # 🐟😋
            self.𓊛 += 1
            self.𓋿(5)                    # 🔥 combo (🐟 base 5)
            self.𓆛 = self.𓆙((self.𓇬, self.𓊮, self.𓃥, self.𓅱, *self.𓎜()))
        if self.𓃠 == self.𓊮:            # 🥛😋 → ⚡
            self.𓊳 += 1
            self.𓊰 = self.𓋨
            self.𓋿(3)                    # 🔥 combo (🥛 base 3)
            self.𓊮 = self.𓆙((self.𓇬, self.𓆛, self.𓃥, self.𓅱, *self.𓎜()))
        if self.𓅱 is not None and self.𓃠 == self.𓅱:   # 🐦😋 → 🏆
            self.𓅮 += 1
            self.𓋿(self.𓅯)              # 🔥 combo (🐦 base 𓅯=7)
            self.𓅱 = self.𓆙((self.𓇬, self.𓆛, self.𓊮, self.𓃥, *self.𓎜()))
        if self.𓊰 > 0:                   # 🥛⚡  🐈🎯 nearest 🐭 from afar
            𓂭 = self.𓃰(self.𓃠)
            𓆉 = sorted((𓂭.get(𓅘, 999), 𓅘) for 𓅘 in self.𓁉𓂋)
            if 𓆉 and 𓆉[0][0] <= self.𓋩 and self.𓁏(𓆉[0][1]):
                return True
        for 𓇋 in range(len(self.𓁉𓂋)):   # 🐭🐭💨  (∀ own 🧠)
            self.𓁉𓂋[𓇋] = self.𓅓𓎗(𓇋)
        if self.𓅱 is not None:            # 🐦🕊️  flee
            self.𓅱𓎗()
        if self.𓁏(self.𓃠):              # 😹
            return True
        if self.𓃥 is not None and self.𓏰 % self.𓃥𓎿 == 0:
            self.𓃥𓎗()                   # 🐕💨🐈  (half-speed)
        self.𓁏(self.𓃠)                  # 😹  (🐈🌀 → 🐭?)
        return self.𓄊 or self.𓋺         # 🎮🔚 : 😻 win or 💀 lose

    def 𓋾(self) -> bool:
        # 🎮🔚  game over : 😻 catch or 💀 no ❤️
        return self.𓄊 or self.𓋺

    def 𓋿(self, 𓃀: int) -> None:
        # 🔥 combo tally :  🔥+1 , 🏆 bonus += base × (min(🔥,🧢)−1)
        self.𓋻 += 1
        self.𓋼 += 𓃀 * (min(self.𓋻, self.𓋻𓈎) - 1)

    def 𓋰(self) -> None:
        # 🧶 throw :  🎾 📍🐈  (×1 / 🎮 , 🚫🧱)  → 🐕 distract ⏳
        if self.𓋯 or self.𓃠 in self.𓊵:
            return
        self.𓋭 = self.𓃠
        self.𓋮 = self.𓋬                 # ⏳ armed
        self.𓋯 = True                    # ×1 spent

    def 𓃥𓎗(self) -> None:
        # 🐕🧠 :  BFS 1️⃣🐾 →🐈 .  🐕👉🐈 → 😿 :  🐈🌀 safe restart , 🐕🎲 far
        if self.𓃥 is None:
            return
        if self.𓋭 is not None and 𓎉(self.𓃥, self.𓋭) <= self.𓋫:
            self.𓃥 = self.𓊐(self.𓃥, self.𓋭)   # 🧶 distract : 💨🎾 , 🚫💨🐈
            return                        # 🚫 bonk while 🧶
        self.𓃥 = self.𓊐(self.𓃥, self.𓃠)
        if self.𓃥 == self.𓃠:            # 😿  bonk!
            self.𓊟 += 1
            self.𓋹 -= 1                   # ❤️ −1  (🐾9️⃣)
            self.𓋻 = 0                    # 🔥 streak reset  (😻🔥)
            if self.𓋹 <= 0:              # 💀 0 ❤️ → 🎮🔚
                self.𓋺 = True
                return
            self.𓃠 = self.𓆙((self.𓇬, self.𓆛, self.𓊮, self.𓃥, *self.𓎜()))  # 🐈🌀
            self.𓃥 = self.𓃥𓆙()         # 🐕🎲 far

    def 𓅓𓎗(self, 𓇋: int = 0) -> tuple[int, int]:
        # 🐭🧠 :  🐈👀 near → 💨(max BFS📏🐈) ; 😮‍💨💤 rest ; else → 🧀😋(min BFS📏🧀)
        #        𓇋 = 🐭 index in 🐭🐭 pack  (∀🐭 own 🧠 + 😮‍💨)
        𓅐 = self.𓁉𓂋[𓇋]
        𓂭 = self.𓃰(self.𓃠)             # 📏→🐈
        if 𓂭.get(𓅐, 999) <= self.𓋴:
            # 😱💨  …  😮‍💨💤❓
            if self.𓊚𓂋[𓇋] >= self.𓎿:
                self.𓊚𓂋[𓇋] = 0
                return 𓅐                 # 💤
            self.𓊚𓂋[𓇋] += 1
            𓅑 = 𓅐
            𓅒 = 𓂭.get(𓅐, 0)
            for 𓆓 in sorted(self.𓊇𓈎(𓅐)):
                𓊈 = 𓂭.get(𓆓, 0)
                if 𓊈 > 𓅒:
                    𓅒 = 𓊈
                    𓅑 = 𓆓
            return 𓅑
        # 🧀😋
        self.𓊚𓂋[𓇋] = 0
        return self.𓊐(𓅐, self.𓇬)

    def 𓅱𓎗(self) -> None:
        # 🐦🧠 :  🕊️ fly 8🧭 , 🚫🧱 perch , 💨 max 📐(chebyshev)→🐈 , ≠ 🐭🐕🧀🐟🥛
        if self.𓅱 is None:
            return
        𓆊 = {*self.𓁉𓂋, self.𓃥, self.𓇬, self.𓆛, self.𓊮}
        𓅑 = self.𓅱
        𓅒 = 𓎉(self.𓅱, self.𓃠)             # 📐 now
        for 𓂄𓊪 in (-1, 0, 1):
            for 𓂄𓏏 in (-1, 0, 1):
                𓆓 = (𓎘(self.𓅱[0] + 𓂄𓊪, 𓈖𓊪), 𓎘(self.𓅱[1] + 𓂄𓏏, 𓈖𓏏))
                if 𓆓 == self.𓅱 or 𓆓 in self.𓊵 or 𓆓 in 𓆊:
                    continue
                𓊈 = 𓎉(𓆓, self.𓃠)
                if 𓊈 > 𓅒:
                    𓅒 = 𓊈
                    𓅑 = 𓆓
        self.𓅱 = 𓅑

    def 𓊙(self) -> int:
        # 🏆  ⚡fast + 🐟bonus + 🥛bonus + 🐦bonus + 🔥combo − 😿penalty  (🐕 bonks hurt)
        return (max(0, 100 - self.𓏰 - 10 * self.𓊟)
                + 5 * self.𓊛 + 3 * self.𓊳 + self.𓅯 * self.𓅮 + self.𓋼)

    def 𓁑(self) -> str:
        # 🖼️ HUD :  ❤️×N lives  +  🐭×N pack left  +  🔥×N streak  (🔥≥3 → ✨)
        𓋠 = f"❤️×{self.𓋹}  🐭×{len(self.𓁉𓂋)}  🔥×{self.𓋻}"
        if self.𓋻 >= 3:
            𓋠 += "✨"
        return 𓋠

    def 𓁐(self) -> str:
        # 🖼️  🗺️
        𓂏 = []
        for 𓏏 in range(𓈖𓏏):
            𓂐 = []
            for 𓊪 in range(𓈖𓊪):
                𓅘 = (𓊪, 𓏏)
                if 𓅘 == self.𓃠:
                    𓂐.append("🐈")
                elif 𓅘 in self.𓁉𓂋:
                    𓂐.append("🐭")
                elif 𓅘 == self.𓃥:
                    𓂐.append("🐕")
                elif 𓅘 == self.𓅱:
                    𓂐.append("🐦")
                elif 𓅘 == self.𓋭:
                    𓂐.append("🎾")
                elif 𓅘 == self.𓇬:
                    𓂐.append("🧀")
                elif 𓅘 == self.𓆛:
                    𓂐.append("🐟")
                elif 𓅘 == self.𓊮:
                    𓂐.append("🥛")
                elif self.𓎛 is not None and 𓅘 in self.𓎛:
                    𓂐.append("🕳️")
                elif 𓅘 in self.𓊵:
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
    # 📇  🎮 → 📜 record
    return {
        "🏆": 𓉔𓏤.𓊙(), "🎚️": 𓉔𓏤.𓊍, "⏱️": 𓉔𓏤.𓏰, "🐟": 𓉔𓏤.𓊛,
        "🥛": 𓉔𓏤.𓊳, "🐦": 𓉔𓏤.𓅮, "😿": 𓉔𓏤.𓊟,
    }


# ─────────── 🌈 🎨📺 ───────────
𓋊𓊞 = {   # 🀄 → ANSI 🎨  (🟩🌿 , 🟥🐕 , 🟦🥛 , 🟨🧀 …)
    "🐈": "35", "🐭": "37", "🐕": "31", "🐦": "36", "🎾": "95",
    "🧀": "33", "🐟": "94", "🥛": "34", "🕳️": "95", "🧱": "90", "🟩": "32",
    "❤️": "91", "🔥": "93",   # 🟥❤️ lives , 🟧🔥 streak
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


def 𓁉𓈖(𓊍: int) -> int:
    # 🐭🐭  pack size @ 🌊 :  🌊<5 → 1 ; else 1 + (🌊−4)//2  , 🧢 ×4
    if 𓊍 < 𓁉𓊞:
        return 1
    return min(𓁉𓈎, 1 + (𓊍 - (𓁉𓊞 - 1)) // 2)


def 𓊆(𓊍: int = 1, 𓊃: random.Random | None = None) -> 𓉔:
    # 🎚️  🌊 1..9 → scaled 🏠🎮 :  🧱↑ , 🐕@≥2 , 🐦@≥3 , 🕳️@≥4 , 👀🐭@≥5 ,
    #                              🐭🐭@≥5 , 💨🐕@≥7
    𓊍 = 𓎘(𓊍 - 1, 𓊆𓈖) + 1                  # 🚧 1..9
    𓉔𓏤 = 𓉔(
        𓊃,
        𓊵𓈖=2 + 2 * 𓊍,                       # 🧱 4..20
        𓃥𓁋=𓊍 >= 2,                          # 🐕 @ ≥2
        𓅱𓁋=𓊍 >= 3,                          # 🐦 @ ≥3
        𓎛𓁋=𓊍 >= 4,                          # 🕳️ @ ≥4
    )
    if 𓊍 >= 5:
        𓉔𓏤.𓋴 = 4                            # 🐭👀 sharper (flee sooner)
    𓉔𓏤.𓁎(𓁉𓈖(𓊍))                           # 🐭🐭 pack  (🌊≥5 → ×K)
    if 𓊍 >= 7:
        𓉔𓏤.𓃥𓎿 = 1                          # 🐕💨 full-speed (🚫 half)
    𓉔𓏤.𓊍 = 𓊍                               # 🎚️ tag
    return 𓉔𓏤


def 𓆲(𓊃𓏤: int = 7, 𓏲: int = 200, 𓊍: int = 1, 𓋉: bool = False) -> 𓉔:
    # 🤖🎬  🐈💨🐭  (auto)  @ 🎚️ 🌊  , 🌈 optional
    𓉔𓏤 = 𓊆(𓊍, random.Random(𓊃𓏤))
    print(f"😺🎬  🎚️{𓉔𓏤.𓊍}")
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
        print(𓎍(𓎌(𓎎(𓉔𓏤))))          # 💾🏆 → 📜🔝
    elif 𓉔𓏤.𓋺:
        print(f"💀🐕  ❤️×0  ⏱️={𓉔𓏤.𓏰}  😿×{𓉔𓏤.𓊟}  🏆={𓉔𓏤.𓊙()}  meow…")
        print("┈┈┈┈┈┈┈┈┈┈┈")
        print(𓎍(𓎌(𓎎(𓉔𓏤))))          # 💾🏆 → 📜🔝  (💀 also 📜)
    else:
        print("🙀💨  meow…")
    return 𓉔𓏤


def 𓊪𓏰(𓊍: int = 1, 𓋉: bool = False):
    # 🕹️  🐈  ⬆️⬇️⬅️➡️🐾   🧶=throw   🙀=🚪   @ 🎚️ 🌊  , 🌈 optional
    𓉔𓏤 = 𓊆(𓊍)
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
        print(f"💀🐕  ❤️×0  ⏱️={𓉔𓏤.𓏰}  😿×{𓉔𓏤.𓊟}  🏆={𓉔𓏤.𓊙()}  meow…")
    print("┈┈┈┈┈┈┈┈┈┈┈")
    print(𓎍(𓎌(𓎎(𓉔𓏤))))          # 💾🏆 → 📜🔝


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
    if any(𓅕 in ("🤖", "🎬", "--🤖") for 𓅕 in 𓊾):
        𓆲(𓊍=𓊍𓏤, 𓋉=𓋉𓏤)
    else:
        𓊪𓏰(𓊍𓏤, 𓋉𓏤)
