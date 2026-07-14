# 🐈🎮🐭 — 𓃠 𓆲 𓅓 𓐍  ✨  🧱🗺️ + 🧭 BFS + 🐕😾
# ⬆️⬇️⬅️➡️ 🐾 … 🐈💨🐭 … 🐕💨🐈 … 🧱 … 🎯 → 😻😹😼
#
# 𓉻 𓐁 𓂀:  𓊪↔️  𓏏↕️  𓃠🐈  𓁉🐭  𓃥🐕  𓇬🧀  𓊵🧱  𓊟😿
from __future__ import annotations
import sys
import random
from collections import deque

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

    def __init__(self, 𓊃: random.Random | None = None, 𓊵𓈖: int = 9, 𓃥𓁋: bool = True):
        self.𓊃 = 𓊃 or random.Random()
        self.𓃠 = (0, 0)                        # 🐈
        self.𓁉 = (𓈖𓊪 - 1, 𓈖𓏏 - 1)          # 🐭
        self.𓊵: set[tuple[int, int]] = set()   # 🧱
        self.𓆵(𓊵𓈖)                            # 🧱🎲
        self.𓇬 = self.𓆙()                     # 🧀
        self.𓆛 = self.𓆙((self.𓇬,))            # 🐟
        self.𓊮 = self.𓆙((self.𓇬, self.𓆛))    # 🥛
        self.𓃥: tuple[int, int] | None = None  # 🐕
        if 𓃥𓁋:
            self.𓃥 = self.𓃥𓆙()               # 🐕🎲 far
        self.𓏰 = 0                             # ⏱️
        self.𓊚 = 0                             # 😮‍💨 (🐭 fatigue)
        self.𓊛 = 0                             # 🐟😋 (fish eaten)
        self.𓊳 = 0                             # 🥛😋 (milk eaten)
        self.𓊰 = 0                             # ⚡ (pounce turns)
        self.𓊟 = 0                             # 😿 (🐕 bonks)
        self.𓄊 = False                         # 🎯😻

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
    def 𓆙(self, 𓊫: tuple[tuple[int, int], ...] = ()) -> tuple[int, int]:
        # 🎲 📍  🟩  🔗  ≠🐈🐭  ≠𓊫
        𓂭 = self.𓃰(self.𓃠)
        𓆊 = {self.𓃠, self.𓁉, *𓊫}
        𓊾 = sorted(𓅘 for 𓅘 in 𓂭 if 𓅘 not in 𓆊)
        if not 𓊾:
            return self.𓁉
        return self.𓊃.choice(𓊾)

    def 𓃥𓆙(self) -> tuple[int, int]:
        # 🐕🎲 📍  🔗  ≠🐈🐭🧀🐟🥛  📏🐈 ≥ 𓃥𓊞
        𓂭 = self.𓃰(self.𓃠)
        𓆊 = {self.𓃠, self.𓁉, self.𓇬, self.𓆛, self.𓊮}
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
        # 🐈 🐾  →  🐭💨  →  🎯❓
        if 𓊍 not in 𓂃:
            return False
        self.𓏰 += 1
        if self.𓊰 > 0:                   # ⚡⏳ tick
            self.𓊰 -= 1
        self.𓃠 = self.𓎗(self.𓃠, 𓂃[𓊍])
        if self.𓃠 == self.𓁉:            # 😻🎯
            self.𓄊 = True
            return True
        if self.𓃠 == self.𓇬:            # 🧀😋
            self.𓇬 = self.𓆙((self.𓆛, self.𓊮, self.𓃥))
        if self.𓃠 == self.𓆛:            # 🐟😋
            self.𓊛 += 1
            self.𓆛 = self.𓆙((self.𓇬, self.𓊮, self.𓃥))
        if self.𓃠 == self.𓊮:            # 🥛😋 → ⚡
            self.𓊳 += 1
            self.𓊰 = self.𓋨
            self.𓊮 = self.𓆙((self.𓇬, self.𓆛, self.𓃥))
        if self.𓊰 > 0:                   # 🥛⚡  🐈🎯🐭 from afar
            𓂭 = self.𓃰(self.𓃠)
            if 𓂭.get(self.𓁉, 999) <= self.𓋩:
                self.𓄊 = True
                return True
        self.𓁉 = self.𓅓𓎗()             # 🐭💨
        if self.𓃠 == self.𓁉:            # 😹
            self.𓄊 = True
            return self.𓄊
        if self.𓃥 is not None and self.𓏰 % self.𓃥𓎿 == 0:
            self.𓃥𓎗()                   # 🐕💨🐈  (half-speed)
        if self.𓃠 == self.𓁉:            # 😹  (🐕 nudge → 🐭?)
            self.𓄊 = True
        return self.𓄊

    def 𓃥𓎗(self) -> None:
        # 🐕🧠 :  BFS 1️⃣🐾 →🐈 .  🐕👉🐈 → 😿 :  🐈🌀 safe restart , 🐕🎲 far
        if self.𓃥 is None:
            return
        self.𓃥 = self.𓊐(self.𓃥, self.𓃠)
        if self.𓃥 == self.𓃠:            # 😿  bonk!
            self.𓊟 += 1
            self.𓃠 = self.𓆙((self.𓇬, self.𓆛, self.𓊮, self.𓃥))  # 🐈🌀
            self.𓃥 = self.𓃥𓆙()         # 🐕🎲 far

    def 𓅓𓎗(self) -> tuple[int, int]:
        # 🐭🧠 :  🐈👀 near → 💨(max BFS📏🐈) ; 😮‍💨💤 rest ; else → 🧀😋(min BFS📏🧀)
        𓅐 = self.𓁉
        𓂭 = self.𓃰(self.𓃠)             # 📏→🐈
        if 𓂭.get(𓅐, 999) <= self.𓋴:
            # 😱💨  …  😮‍💨💤❓
            if self.𓊚 >= self.𓎿:
                self.𓊚 = 0
                return 𓅐                 # 💤
            self.𓊚 += 1
            𓅑 = 𓅐
            𓅒 = 𓂭.get(𓅐, 0)
            for 𓆓 in sorted(self.𓊇𓈎(𓅐)):
                𓊈 = 𓂭.get(𓆓, 0)
                if 𓊈 > 𓅒:
                    𓅒 = 𓊈
                    𓅑 = 𓆓
            return 𓅑
        # 🧀😋
        self.𓊚 = 0
        return self.𓊐(𓅐, self.𓇬)

    def 𓊙(self) -> int:
        # 🏆  ⚡fast + 🐟bonus + 🥛bonus − 😿penalty  (🐕 bonks hurt)
        return max(0, 100 - self.𓏰 - 10 * self.𓊟) + 5 * self.𓊛 + 3 * self.𓊳

    def 𓁐(self) -> str:
        # 🖼️  🗺️
        𓂏 = []
        for 𓏏 in range(𓈖𓏏):
            𓂐 = []
            for 𓊪 in range(𓈖𓊪):
                𓅘 = (𓊪, 𓏏)
                if 𓅘 == self.𓃠:
                    𓂐.append("🐈")
                elif 𓅘 == self.𓁉:
                    𓂐.append("🐭")
                elif 𓅘 == self.𓃥:
                    𓂐.append("🐕")
                elif 𓅘 == self.𓇬:
                    𓂐.append("🧀")
                elif 𓅘 == self.𓆛:
                    𓂐.append("🐟")
                elif 𓅘 == self.𓊮:
                    𓂐.append("🥛")
                elif 𓅘 in self.𓊵:
                    𓂐.append("🧱")
                else:
                    𓂐.append("🟩")
            𓂏.append("".join(𓂐))
        return "\n".join(𓂏)


def 𓊄(𓉔𓏤: 𓉔) -> str:
    # 🐈🧠  BFS 💨→🐭 , 🚫🐕 :  min 📏→🐭 , tie → max 📏→🐕 , 🚫 step onto 🐕
    𓂭𓁉 = 𓉔𓏤.𓃰(𓉔𓏤.𓁉)                       # 📏→🐭
    𓂭𓃥 = 𓉔𓏤.𓃰(𓉔𓏤.𓃥) if 𓉔𓏤.𓃥 is not None else {}   # 📏→🐕
    𓅑 = 𓉔𓏤.𓃠
    𓅒 = (10 ** 9, 0)
    for 𓆓 in [𓉔𓏤.𓃠] + sorted(𓉔𓏤.𓊇𓈎(𓉔𓏤.𓃠)):
        if 𓆓 == 𓉔𓏤.𓃥:                        # 🚫🐕
            continue
        𓊈 = (𓂭𓁉.get(𓆓, 10 ** 9), -𓂭𓃥.get(𓆓, 0))
        if 𓊈 < 𓅒:
            𓅒 = 𓊈
            𓅑 = 𓆓
    return 𓉔𓏤.𓂊(𓉔𓏤.𓃠, 𓅑)


def 𓆲(𓊃𓏤: int = 7, 𓏲: int = 200) -> 𓉔:
    # 🤖🎬  🐈💨🐭  (auto)
    𓉔𓏤 = 𓉔(random.Random(𓊃𓏤))
    print("😺🎬")
    print(𓉔𓏤.𓁐())
    for _ in range(𓏲):
        𓆳 = 𓊄(𓉔𓏤)
        if 𓉔𓏤.𓂷(𓆳):
            break
    print("┈┈┈┈┈┈┈┈┈┈┈")
    print(𓉔𓏤.𓁐())
    if 𓉔𓏤.𓄊:
        print(f"😻🎯  ⏱️={𓉔𓏤.𓏰}  🐟×{𓉔𓏤.𓊛}  🥛×{𓉔𓏤.𓊳}  😿×{𓉔𓏤.𓊟}  🏆={𓉔𓏤.𓊙()}  prrr~")
    else:
        print("🙀💨  meow…")
    return 𓉔𓏤


def 𓊪𓏰():
    # 🕹️  🐈  ⬆️⬇️⬅️➡️🐾   🙀=🚪
    𓉔𓏤 = 𓉔()
    print("😺🕹️  ⬆️⬇️⬅️➡️🐾   🙀=🚪")
    while not 𓉔𓏤.𓄊:
        print(𓉔𓏤.𓁐())
        print(f"⏱️={𓉔𓏤.𓏰}  🐈{𓉔𓏤.𓃠} 🐭{𓉔𓏤.𓁉} 🐕{𓉔𓏤.𓃥}  ⚡{𓉔𓏤.𓊰}  😿×{𓉔𓏤.𓊟}")
        try:
            𓊍 = input("🐾❓ ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋😼")
            return
        if 𓊍 in ("🙀", "🚪", "q"):
            print("👋😼")
            return
        if 𓊍 not in 𓂃:
            print("🤔❓")
            continue
        𓉔𓏤.𓂷(𓊍)
    print(𓉔𓏤.𓁐())
    print(f"😻🎯  ⏱️={𓉔𓏤.𓏰}  🐟×{𓉔𓏤.𓊛}  🥛×{𓉔𓏤.𓊳}  😿×{𓉔𓏤.𓊟}  🏆={𓉔𓏤.𓊙()}  prrr~")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("🤖", "🎬", "--🤖"):
        𓆲()
    else:
        𓊪𓏰()
