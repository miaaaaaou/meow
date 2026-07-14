# 🐈🎮🐭 — 𓃠 𓆲 𓅓 𓐍  ✨
# ⬆️⬇️⬅️➡️ 🐾 … 🐈💨🐭 … 🎯 → 😻😹😼
#
# 𓉻 𓐁 𓂀:  𓊪↔️  𓏏↕️  𓃠🐈  𓁉🐭  𓇬🧀
from __future__ import annotations
import sys
import random

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


def 𓎘(𓆼: int, 𓊝: int) -> int:
    # 🚧  0 … 𓊝-1
    return max(0, min(𓊝 - 1, 𓆼))


def 𓐍(𓄿: tuple[int, int], 𓃀: tuple[int, int]) -> int:
    # 📏  (|Δ↔️| + |Δ↕️|)
    return abs(𓄿[0] - 𓃀[0]) + abs(𓄿[1] - 𓃀[1])


class 𓉔:
    # 🏠🎮  🐈💨🐭
    def __init__(self, 𓊃: random.Random | None = None):
        self.𓊃 = 𓊃 or random.Random()
        self.𓃠 = (0, 0)                        # 🐈
        self.𓁉 = (𓈖𓊪 - 1, 𓈖𓏏 - 1)          # 🐭
        self.𓇬 = self.𓆙()                     # 🧀
        self.𓏰 = 0                             # ⏱️
        self.𓊚 = 0                             # 😮‍💨 (🐭 fatigue)
        self.𓄊 = False                         # 🎯😻

    def 𓆙(self) -> tuple[int, int]:
        # 🎲 📍
        return (self.𓊃.randrange(𓈖𓊪), self.𓊃.randrange(𓈖𓏏))

    def 𓎗(self, 𓄿: tuple[int, int], 𓂄: tuple[int, int]) -> tuple[int, int]:
        # 🐾 → 📍′  🚧
        return (𓎘(𓄿[0] + 𓂄[0], 𓈖𓊪), 𓎘(𓄿[1] + 𓂄[1], 𓈖𓏏))

    def 𓂷(self, 𓊍: str) -> bool:
        # 🐈 🐾  →  🐭💨  →  🎯❓
        if 𓊍 not in 𓂃:
            return False
        self.𓏰 += 1
        self.𓃠 = self.𓎗(self.𓃠, 𓂃[𓊍])
        if self.𓃠 == self.𓁉:            # 😻🎯
            self.𓄊 = True
            return True
        if self.𓃠 == self.𓇬:            # 🧀😋
            self.𓇬 = self.𓆙()
        self.𓁉 = self.𓅓𓎗()             # 🐭💨
        if self.𓃠 == self.𓁉:            # 😹
            self.𓄊 = True
        return self.𓄊

    # 👀  🐈 near → 🐭😱
    𓋴 = 3
    # 💨💨💨 → 💤  (🐭 stamina)
    𓎿 = 4

    def 𓅓𓎗(self) -> tuple[int, int]:
        # 🐭🧠 :  🐈👀 near → 💨(max 📏🐈) ; 😮‍💨💤 rest ; else → 🧀😋(min 📏🧀)
        𓅐 = self.𓁉
        𓅑 = 𓅐
        if 𓐍(𓅐, self.𓃠) <= self.𓋴:
            # 😱💨  …  😮‍💨💤❓
            if self.𓊚 >= self.𓎿:
                self.𓊚 = 0
                return 𓅐            # 💤
            self.𓊚 += 1
            𓅒 = 𓐍(𓅐, self.𓃠)
            for 𓊍, 𓂄 in 𓂃.items():
                if 𓊍 == "🐾":
                    continue
                𓊇 = self.𓎗(𓅐, 𓂄)
                𓊈 = 𓐍(𓊇, self.𓃠)
                if 𓊈 > 𓅒:
                    𓅒 = 𓊈
                    𓅑 = 𓊇
        else:
            # 🧀😋
            self.𓊚 = 0
            𓅒 = 𓐍(𓅐, self.𓇬)
            for 𓊍, 𓂄 in 𓂃.items():
                if 𓊍 == "🐾":
                    continue
                𓊇 = self.𓎗(𓅐, 𓂄)
                𓊈 = 𓐍(𓊇, self.𓇬)
                if 𓊈 < 𓅒:
                    𓅒 = 𓊈
                    𓅑 = 𓊇
        return 𓅑

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
                elif 𓅘 == self.𓇬:
                    𓂐.append("🧀")
                else:
                    𓂐.append("🟩")
            𓂏.append("".join(𓂐))
        return "\n".join(𓂏)


def 𓊄(𓉔𓏤: 𓉔) -> str:
    # 🐈🧠  💨→🐭  (min 📏)  → 🧭
    𓅐 = 𓉔𓏤.𓃠
    𓆳 = "🐾"
    𓅒 = 𓐍(𓅐, 𓉔𓏤.𓁉)
    for 𓊍, 𓂄 in 𓂃.items():
        𓊇 = 𓉔𓏤.𓎗(𓅐, 𓂄)
        𓊈 = 𓐍(𓊇, 𓉔𓏤.𓁉)
        if 𓊈 < 𓅒:
            𓅒 = 𓊈
            𓆳 = 𓊍
    return 𓆳


def 𓆲(𓊃𓏤: int = 7, 𓏲: int = 80) -> 𓉔:
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
        print(f"😻🎯  ⏱️={𓉔𓏤.𓏰}  prrr~")
    else:
        print("🙀💨  meow…")
    return 𓉔𓏤


def 𓊪𓏰():
    # 🕹️  🐈  ⬆️⬇️⬅️➡️🐾   🙀=🚪
    𓉔𓏤 = 𓉔()
    print("😺🕹️  ⬆️⬇️⬅️➡️🐾   🙀=🚪")
    while not 𓉔𓏤.𓄊:
        print(𓉔𓏤.𓁐())
        print(f"⏱️={𓉔𓏤.𓏰}  🐈{𓉔𓏤.𓃠} 🐭{𓉔𓏤.𓁉}")
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
    print(f"😻🎯  ⏱️={𓉔𓏤.𓏰}  prrr~")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("🤖", "🎬", "--🤖"):
        𓆲()
    else:
        𓊪𓏰()
