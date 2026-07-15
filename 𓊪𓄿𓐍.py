# 🐈✅🐭 — 𓊪𓄿  ✨  🧱 + 🧭 BFS + 🪝😾 + 💾🏆
import importlib.util as 𓇓
import json
import os
import random
import subprocess
import sys
import tempfile

𓊒 = 𓇓.spec_from_file_location("𓅓", "𓃠𓐍𓅓.py")
𓅓 = 𓇓.module_from_spec(𓊒)
𓊒.loader.exec_module(𓅓)

𓊓 = 𓇓.spec_from_file_location("𓆓𓁐", ".claude/𓆓𓁐.py")
𓆦 = 𓇓.module_from_spec(𓊓)
𓊓.loader.exec_module(𓆦)


def 𓊪𓎘():
    # 🚧  clamp
    assert 𓅓.𓎘(-5, 10) == 0
    assert 𓅓.𓎘(99, 10) == 9
    assert 𓅓.𓎘(3, 10) == 3


def 𓊪𓐍():
    # 📏  manhattan
    assert 𓅓.𓐍((0, 0), (3, 4)) == 7
    assert 𓅓.𓐍((2, 2), (2, 2)) == 0


def 𓊪𓎗():
    # 🐾  🚧 edges  (🚫🧱)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (0, 0)
    assert 𓋁.𓎗(𓋁.𓃠, 𓅓.𓂃["⬅️"]) == (0, 0)     # 🧱edge
    assert 𓋁.𓎗(𓋁.𓃠, 𓅓.𓂃["⬆️"]) == (0, 0)     # 🧱edge
    assert 𓋁.𓎗(𓋁.𓃠, 𓅓.𓂃["➡️"]) == (1, 0)
    assert 𓋁.𓎗(𓋁.𓃠, 𓅓.𓂃["⬇️"]) == (0, 1)


def 𓊪𓊵():
    # 🧱  block  →  stay
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓊵 = {(3, 3)}
    assert 𓋁.𓎗((2, 3), 𓅓.𓂃["➡️"]) == (2, 3)     # 🧱 → 🚫
    assert 𓋁.𓎗((2, 3), 𓅓.𓂃["⬅️"]) == (1, 3)     # 🟩 → ✅
    # 🧭 neighbors skip 🧱
    assert (3, 3) not in 𓋁.𓊇𓈎((2, 3))
    # 🔗  BFS connected  (no 🧱)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓂭 = 𓋂.𓃰((0, 0))
    assert len(𓂭) == 𓅓.𓈖𓊪 * 𓅓.𓈖𓏏


def 𓊪𓎘𓁉():
    # 🔗  🐈 ↔️ 🐭 always reachable  (🧱🎲)
    for 𓊃 in range(50):
        𓋁 = 𓅓.𓉔(random.Random(𓊃))
        assert 𓋁.𓁉 in 𓋁.𓃰(𓋁.𓃠), f"🙀🔗 seed={𓊃}"


def 𓊪𓂷():
    # 🐈👉🐭  adjacent → 😻
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (5, 5)
    𓋁.𓁉 = (6, 5)
    assert 𓋁.𓂷("➡️") is True
    assert 𓋁.𓄊 is True
    assert 𓋁.𓏰 == 1


def 𓊪𓇬():
    # 🧀😋  → 🎲 new 🧀
    𓋁 = 𓅓.𓉔(random.Random(3), 𓊵𓈖=0)
    𓋁.𓁉 = (0, 7)         # 🐭 far
    𓋁.𓃠 = (2, 2)
    𓋁.𓇬 = (3, 2)         # 🧀 →➡️
    𓋁.𓂷("➡️")
    assert 𓋁.𓇬 != (3, 2)


def 𓊪𓄊():
    # 🤖  🐈 always 😻  (many 🎲 + 🧱)
    for 𓊃 in range(60):
        𓋁 = 𓅓.𓉔(random.Random(𓊃))
        for _ in range(500):
            if 𓋁.𓂷(𓅓.𓊄(𓋁)):
                break
        assert 𓋁.𓄊 is True, f"🙀 seed={𓊃}"


def 𓊪𓆛():
    # 🐟😋  → 🎲 new 🐟  + 🏆 bonus
    𓋁 = 𓅓.𓉔(random.Random(1), 𓊵𓈖=0)
    𓋁.𓁉 = (0, 7)         # 🐭 far
    𓋁.𓃠 = (2, 2)
    𓋁.𓇬 = (9, 0)         # 🧀 elsewhere
    𓋁.𓆛 = (3, 2)         # 🐟 →➡️
    𓋁.𓂷("➡️")
    assert 𓋁.𓊛 == 1          # 😋+1
    assert 𓋁.𓆛 != (3, 2)     # 🎲 respawn


def 𓊪𓊙():
    # 🏆  ⚡fast + 🐟 + 🥛 − 😿
    𓋁 = 𓅓.𓉔(random.Random(0))
    𓋁.𓏰 = 10
    𓋁.𓊛 = 3
    𓋁.𓊳 = 2
    𓋁.𓊟 = 0
    assert 𓋁.𓊙() == 90 + 15 + 6   # (100-10) + 5×3 + 3×2
    𓋁.𓊟 = 2                        # 😿×2 → −20
    assert 𓋁.𓊙() == 70 + 15 + 6   # (100-10-20) + 15 + 6
    𓋁.𓅮 = 2                        # 🐦×2 → +14
    assert 𓋁.𓊙() == 70 + 15 + 6 + 14
    𓋁.𓏰 = 250
    assert 𓋁.𓊙() == 0 + 15 + 6 + 14   # 🚧 ≥0 (base) , 🎁 stay


def 𓊪𓃥():
    # 🐕🎲  spawn : 🔗 , ≠🐈🐭🧀🐟🥛 , 📏🐈 ≥ 𓃥𓊞  (🚫🧱 map)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert 𓋂.𓃥 is not None
    assert 𓋂.𓃰(𓋂.𓃠)[𓋂.𓃥] >= 𓅓.𓉔.𓃥𓊞      # 📏 far
    for 𓊃 in range(30):
        𓋁 = 𓅓.𓉔(random.Random(𓊃))
        assert 𓋁.𓃥 is not None
        assert 𓋁.𓃥 in 𓋁.𓃰(𓋁.𓃠)              # 🔗
        assert 𓋁.𓃥 not in (𓋁.𓃠, 𓋁.𓁉, 𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮)


def 𓊪𓃥𓎗():
    # 🐕💨🐈  : BFS 1️⃣🐾 → 📏 shrinks
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (5, 4)
    𓋁.𓃥 = (5, 7)                              # 📏=3
    𓅐 = 𓋁.𓃰(𓋁.𓃠)[𓋁.𓃥]
    𓋁.𓃥𓎗()
    assert 𓋁.𓃰(𓋁.𓃠)[𓋁.𓃥] < 𓅐              # 🔽 closer


def 𓊪𓊟():
    # 😿  bonk : 🐕👉🐈 → 𓊟+1 , 🐈🌀 relocate , 🐕🎲 respawn
    𓋁 = 𓅓.𓉔(random.Random(2), 𓊵𓈖=0)
    𓋁.𓃠 = (5, 5)
    𓋁.𓃥 = (5, 6)                              # adjacent → catches
    𓋁.𓃥𓎗()
    assert 𓋁.𓊟 == 1                           # 😿+1
    assert 𓋁.𓃥 is not None
    assert 𓋁.𓃠 != 𓋁.𓃥                        # 🐈≠🐕 after 🌀
    assert 𓋁.𓃰(𓋁.𓃠)[𓋁.𓃥] >= 𓅓.𓉔.𓃥𓊞     # 🐕🎲 far again


def 𓊪𓃥𓎿():
    # 🐕💨  half-speed : 🐾 odd → 💤 , even → 💨
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (0, 0)
    𓋁.𓁉 = (10, 7)                             # 🐭 far
    𓋁.𓇬 = (0, 5)
    𓋁.𓆛 = (1, 5)
    𓋁.𓊮 = (2, 5)
    𓋁.𓃥 = (10, 0)                             # 🐕 far
    𓅐 = 𓋁.𓃥
    𓋁.𓂷("🐾")                                # 𓏰=1 odd → 🐕💤
    assert 𓋁.𓃥 == 𓅐
    𓋁.𓂷("🐾")                                # 𓏰=2 even → 🐕💨
    assert 𓋁.𓃥 != 𓅐


def 𓊪𓁋():
    # 🚫🐕  off : 𓃥=None , 🚫 render , 🐈 still 😻
    𓋁 = 𓅓.𓉔(random.Random(0), 𓃥𓁋=False)
    assert 𓋁.𓃥 is None
    assert "🐕" not in 𓋁.𓁐()
    for _ in range(500):
        if 𓋁.𓂷(𓅓.𓊄(𓋁)):
            break
    assert 𓋁.𓄊 is True
    assert 𓋁.𓊟 == 0


def 𓊪𓁐():
    # 🖼️  🗺️ 📐
    𓋁 = 𓅓.𓉔(random.Random(0))
    𓋀 = 𓋁.𓁐().split("\n")
    assert len(𓋀) == 𓅓.𓈖𓏏
    assert "🐈" in 𓋁.𓁐()
    assert "🐭" in 𓋁.𓁐()
    assert "🧱" in 𓋁.𓁐()      # 🧱 drawn
    assert "🐟" in 𓋁.𓁐()      # 🐟 drawn
    assert "🥛" in 𓋁.𓁐()      # 🥛 drawn
    assert "🐕" in 𓋁.𓁐()      # 🐕 drawn
    assert "🐦" in 𓋁.𓁐()      # 🐦 drawn
    assert "🕳️" in 𓋁.𓁐()      # 🕳️ drawn


def 𓊪𓋴():
    # 😮‍💨  🐭 tires → 💤 (stay) → 🐈 gains
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (5, 4)
    𓋁.𓁉 = (5, 6)        # 📏=2 ≤ 𓋴
    𓋁.𓊚 = 𓅓.𓉔.𓎿      # 😵 spent
    𓋂 = 𓋁.𓅓𓎗()
    assert 𓋂 == (5, 6)   # 💤 stay
    assert 𓋁.𓊚 == 0     # 🔄


def 𓊪𓊮():
    # 🥛😋  → 🎲 new 🥛 + ⚡ pounce armed
    𓋁 = 𓅓.𓉔(random.Random(1), 𓊵𓈖=0)
    𓋁.𓁉 = (0, 7)         # 🐭 far
    𓋁.𓃠 = (2, 2)
    𓋁.𓇬 = (0, 0)         # 🧀 elsewhere
    𓋁.𓆛 = (0, 1)         # 🐟 elsewhere
    𓋁.𓊮 = (3, 2)         # 🥛 →➡️
    𓋁.𓂷("➡️")
    assert 𓋁.𓊳 == 1                 # 😋+1
    assert 𓋁.𓊰 == 𓅓.𓉔.𓋨          # ⚡ armed
    assert 𓋁.𓊮 != (3, 2)           # 🎲 respawn


def 𓊪𓊰():
    # 🥛⚡  🐈🎯🐭 from 📏≤reach  (no adjacency)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓇬 = (0, 0)
    𓋁.𓆛 = (0, 1)
    𓋁.𓊮 = (0, 2)
    𓋁.𓃠 = (5, 5)
    𓋁.𓁉 = (5, 7)         # 📏=2 == 𓋩
    𓋁.𓊰 = 2              # ⚡ (tick → 1, still on)
    assert 𓋁.𓂷("🐾") is True     # 😼 pounce
    assert 𓋁.𓄊 is True
    # 🚫⚡ → 🚫 afar catch
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋂.𓇬 = (0, 0)
    𓋂.𓆛 = (0, 1)
    𓋂.𓊮 = (0, 2)
    𓋂.𓃠 = (5, 5)
    𓋂.𓁉 = (5, 7)
    𓋂.𓊰 = 0              # 🚫⚡
    𓋂.𓂷("🐾")
    assert 𓋂.𓄊 is False


def 𓊪𓅱():
    # 🐦🎲  spawn : 🔗 , ≠🐈🐭🧀🐟🥛🐕  (🚫🧱 map)
    for 𓊃 in range(30):
        𓋁 = 𓅓.𓉔(random.Random(𓊃))
        assert 𓋁.𓅱 is not None
        assert 𓋁.𓅱 in 𓋁.𓃰(𓋁.𓃠)              # 🔗 green
        assert 𓋁.𓅱 not in (𓋁.𓃠, 𓋁.𓁉, 𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮, 𓋁.𓃥)


def 𓊪𓎉():
    # 📐  chebyshev
    assert 𓅓.𓎉((0, 0), (3, 4)) == 4
    assert 𓅓.𓎉((2, 2), (2, 2)) == 0
    assert 𓅓.𓎉((1, 1), (2, 3)) == 2


def 𓊪𓅱𓎗():
    # 🐦🕊️  flee : 8🧭 → 📐→🐈 grows  (🚫🧱 perch)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (5, 5)
    𓋁.𓅱 = (5, 6)                              # 📐=1
    𓋁.𓁉 = (0, 0)                              # 🐭 elsewhere
    𓋁.𓃥 = (10, 0)                             # 🐕 elsewhere
    𓋁.𓇬 = (0, 7)
    𓋁.𓆛 = (1, 7)
    𓋁.𓊮 = (2, 7)
    𓅐 = 𓅓.𓎉(𓋁.𓅱, 𓋁.𓃠)
    𓋁.𓅱𓎗()
    assert 𓅓.𓎉(𓋁.𓅱, 𓋁.𓃠) > 𓅐             # 🔼 farther
    assert 𓋁.𓅱 not in 𓋁.𓊵                    # 🚫🧱 perch


def 𓊪𓅱𓎗𓊵():
    # 🐦  🚫🧱 :  🕊️ never lands on 🧱
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓊵 = {(5, 7), (6, 6), (6, 7), (4, 7), (4, 6)}   # 🧱 ring far side
    𓋁.𓃠 = (5, 5)
    𓋁.𓅱 = (5, 6)
    𓋁.𓁉 = (0, 0)
    𓋁.𓃥 = (10, 0)
    𓋁.𓇬 = (0, 7)
    𓋁.𓆛 = (1, 7)
    𓋁.𓊮 = (2, 7)
    for _ in range(6):
        𓋁.𓅱𓎗()
        assert 𓋁.𓅱 not in 𓋁.𓊵


def 𓊪𓅲():
    # 🐦😋  → 𓅮+1 , 🎲 respawn , 🏆 bonus
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓁉 = (0, 7)         # 🐭 far
    𓋁.𓃥 = (10, 0)        # 🐕 far
    𓋁.𓇬 = (9, 0)
    𓋁.𓆛 = (9, 1)
    𓋁.𓊮 = (9, 2)
    𓋁.𓃠 = (2, 2)
    𓋁.𓅱 = (3, 2)         # 🐦 →➡️
    𓋁.𓂷("➡️")
    assert 𓋁.𓅮 == 1          # 😋+1
    assert 𓋁.𓅱 != (3, 2)     # 🎲 respawn
    assert 𓋁.𓄊 is False      # 🚫🎯 (🐭 far)


def 𓊪𓅱𓁋():
    # 🚫🐦  off : 𓅱=None , 🚫 render , 🐈 still 😻
    𓋁 = 𓅓.𓉔(random.Random(0), 𓅱𓁋=False)
    assert 𓋁.𓅱 is None
    assert "🐦" not in 𓋁.𓁐()
    for _ in range(500):
        if 𓋁.𓂷(𓅓.𓊄(𓋁)):
            break
    assert 𓋁.𓄊 is True
    assert 𓋁.𓅮 == 0


def 𓊪𓎛():
    # 🕳️➡️🕳️  teleport : 🐈 steps on 🕳️ → 🕳️ twin , 🚫 re-teleport standing
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False)
    𓋁.𓁉 = (0, 7)                              # 🐭 far
    𓋁.𓇬 = (9, 0)
    𓋁.𓆛 = (9, 1)
    𓋁.𓊮 = (9, 2)
    𓋁.𓎛 = ((5, 5), (1, 1))                    # 🕳️↔️🕳️
    𓋁.𓃠 = (4, 5)                              # →➡️ 🕳️(5,5)
    𓋁.𓂷("➡️")
    assert 𓋁.𓃠 == (1, 1)                      # 🕳️ twin
    𓋁.𓂷("🐾")                                # 💤 on 🕳️ → 🚫 re-teleport
    assert 𓋁.𓃠 == (1, 1)


def 𓊪𓎛𓁋():
    # 🚫🕳️  off : 𓎛=None , 🚫 render , 🐈 still 😻
    𓋁 = 𓅓.𓉔(random.Random(0), 𓎛𓁋=False)
    assert 𓋁.𓎛 is None
    assert "🕳️" not in 𓋁.𓁐()
    for _ in range(500):
        if 𓋁.𓂷(𓅓.𓊄(𓋁)):
            break
    assert 𓋁.𓄊 is True


def 𓊪𓋭():
    # 🧶🎾  throw : 🎾 📍🐈 , 🐾 stay , ⏳ armed , ×1 flag , 🖼️ render
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False)
    𓋁.𓁉 = (0, 7)          # 🐭 far
    𓋁.𓇬 = (9, 0)
    𓋁.𓆛 = (9, 1)
    𓋁.𓊮 = (9, 2)
    𓋁.𓃠 = (5, 5)
    𓋁.𓂷("🧶")
    assert 𓋁.𓋭 == (5, 5)              # 🎾 📍🐈
    assert 𓋁.𓋯 is True                # ×1 spent
    assert 𓋁.𓋮 == 𓅓.𓉔.𓋬             # ⏳ armed (🚫 tick on throw turn)
    assert 𓋁.𓃠 == (5, 5)              # 🐾 stay
    𓋁.𓃠 = (6, 5)                      # 🐈 step off
    assert "🎾" in 𓋁.𓁐()              # 🖼️ 🎾 drawn


def 𓊪𓋮():
    # 🧶🐕🌀  distract : 🐕👀🎾 📐≤𓋫 → 💨🎾 (🚫💨🐈)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (0, 5)          # 🐈 far left
    𓋁.𓋭 = (10, 5)         # 🎾 far right
    𓋁.𓋮 = 3
    𓋁.𓃥 = (6, 5)          # 🐕 : 📐→🎾=4≤4 , 📐→🐈=6
    𓅐 = 𓋁.𓃰(𓋁.𓋭)[𓋁.𓃥]   # 📏 🐕→🎾
    𓋁.𓃥𓎗()
    assert 𓋁.𓃰(𓋁.𓋭)[𓋁.𓃥] < 𓅐     # 🔽 💨🎾 not 🐈
    assert 𓋁.𓊟 == 0                  # 🚫 bonk while 🧶


def 𓊪𓋯():
    # 🧶⏳0😾  resume : ⏳ expire → 🎾💨 → 🐕😾 chase 🐈 again
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋁.𓃠 = (5, 5)
    𓋁.𓁉 = (0, 7)          # 🐭 far
    𓋁.𓅱 = None
    # 🧶 active , 🐕 near 🎾 → distract , 🚫 bonk
    𓋁.𓋭 = (5, 6)
    𓋁.𓋮 = 1
    𓋁.𓃥 = (5, 7)          # 📐→🎾=1
    𓋁.𓃥𓎗()
    assert 𓋁.𓊟 == 0                  # 🚫 bonk while 🧶
    # ⏳ expire (🧶⏳ tick via 𓂷) → 🎾💨
    𓋁.𓋮 = 1
    𓋁.𓋭 = (9, 9)          # dummy , will 💨
    𓋁.𓃥 = (9, 9)
    𓋁.𓂷("🐾")
    assert 𓋁.𓋭 is None               # 🎾💨 gone
    # 🐕😾 resume : adjacent → bonk
    𓋁.𓃠 = (5, 5)
    𓋁.𓃥 = (5, 6)
    𓋁.𓃥𓎗()
    assert 𓋁.𓊟 == 1                  # 😾 bonk resumes


def 𓊪𓋰():
    # 🧶×1🚧  limit : 2nd throw → 🚫 new 🎾
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False)
    𓋁.𓁉 = (0, 7)
    𓋁.𓇬 = (9, 0)
    𓋁.𓆛 = (9, 1)
    𓋁.𓊮 = (9, 2)
    𓋁.𓃠 = (3, 3)
    𓋁.𓂷("🧶")
    assert 𓋁.𓋭 == (3, 3)              # 1st 🎾
    𓋁.𓃠 = (6, 6)
    𓋁.𓂷("🧶")                         # 2nd → 🚧
    assert 𓋁.𓋭 != (6, 6)              # 🚫 new 🎾
    assert 𓋁.𓋯 is True                # still spent


def 𓊪𓋹():
    # 🐾9️⃣  nine-lives : 🏁 ❤️×9 , 😿 −1 , 0 → 💀🎮🔚 , 🖼️ HUD , 🔗✅ 🚫💀
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert 𓋁.𓋹 == 9                          # 🏁 start ❤️×9
    assert 𓋁.𓋺 is False                      # 🚫💀
    assert 𓋁.𓋾() is False                    # 🎮 on
    # 😿 bonk → ❤️ 8 + 🐈🌀 restart + still alive
    𓋁.𓃠 = (5, 5)
    𓋁.𓃥 = (5, 6)                             # adjacent → bonk
    𓋁.𓃥𓎗()
    assert 𓋁.𓋹 == 8                          # ❤️ −1
    assert 𓋁.𓊟 == 1                          # 😿 tally = 9−❤️
    assert 𓋁.𓋺 is False                      # still alive
    assert 𓋁.𓃰(𓋁.𓃠)[𓋁.𓃥] >= 𓅓.𓉔.𓃥𓊞    # 🐕🎲 far after 🌀
    # ❤️ 1 → 😿 → 0 → 💀 🎮🔚
    𓋂 = 𓅓.𓉔(random.Random(1), 𓊵𓈖=0)
    𓋂.𓋹 = 1
    𓋂.𓃠 = (5, 5)
    𓋂.𓃥 = (5, 6)
    𓋂.𓃥𓎗()
    assert 𓋂.𓋹 == 0                          # 0 ❤️
    assert 𓋂.𓋺 is True                       # 💀 lose flag
    assert 𓋂.𓋾() is True                     # 🎮🔚
    # 💀 propagates : 𓂷 returns 🎮🔚 True
    𓋃 = 𓅓.𓉔(random.Random(1), 𓊵𓈖=0)
    𓋃.𓋹 = 1
    𓋃.𓃥𓎿 = 1                                 # 🐕💨 full-speed (move this turn)
    𓋃.𓃠 = (5, 5)
    𓋃.𓁉 = (0, 7)                             # 🐭 far (🚫 catch)
    𓋃.𓅱 = None
    𓋃.𓃥 = (5, 6)                             # 🐕 adjacent → fatal bonk on 𓃥𓎗
    assert 𓋃.𓂷("🐾") is True                 # 🎮🔚 via 💀
    assert 𓋃.𓋺 is True and 𓋃.𓄊 is False
    # 🏆 −10 ×😿 (9−❤️) tally kept
    𓋄 = 𓅓.𓉔(random.Random(0))
    𓋄.𓏰 = 10
    𓋄.𓊟 = 3
    assert 𓋄.𓊙() == max(0, 100 - 10 - 30)     # −10×3 bonks
    # 🖼️ HUD ❤️×N  (plain + 🌈)
    assert "❤️×9" in 𓋄.𓁑()
    𓂮 = 𓅓.𓋊(𓋄.𓁑(), True)
    assert "\033[" in 𓂮 and "❤️" in 𓂮         # 🌈 wrap
    assert 𓅓.𓋊(𓋄.𓁑(), False) == 𓋄.𓁑()      # 🚫⚑ ↔️
    # 🔗✅ 120🎲 ↔️ 🚫💥  + 🚫💀 (🐾9️⃣ cat survives , always 😻)
    for 𓊃 in range(120):
        𓋅 = 𓅓.𓉔(random.Random(𓊃))
        for _ in range(500):
            if 𓋅.𓂷(𓅓.𓊄(𓋅)):
                break
        assert 𓋅.𓄊 is True, f"🙀 seed={𓊃}"     # 😻
        assert 𓋅.𓋺 is False, f"💀 seed={𓊃}"    # 🚫9️⃣😿 death
        assert 𓋅.𓋹 == 9 - 𓋅.𓊟                 # ❤️ = 9 − 😿


def 𓊪𓋻():
    # 😻🔥  combo streak : 🎯 → 🔥+1 , 🏆 ×min(🔥,5) , 😿 reset , 🖼️ HUD✨
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert 𓋁.𓋻 == 0 and 𓋁.𓋼 == 0            # 🏁 clean
    # 🔥 tally math :  🔥+1 , bonus += base×(min(🔥,5)−1)
    𓋁.𓋿(5)                                   # 🔥1 → ×1 , +0
    assert 𓋁.𓋻 == 1 and 𓋁.𓋼 == 0
    𓋁.𓋿(5)                                   # 🔥2 → ×2 , +5
    assert 𓋁.𓋻 == 2 and 𓋁.𓋼 == 5
    𓅐 = 𓋁.𓋼
    𓋁.𓋿(5)                                   # 🔥3 → ×3 , +10  (🎯 total = base×3)
    assert 𓋁.𓋻 == 3
    assert 𓋁.𓋼 - 𓅐 == 10                     # bonus×2 + base×1 = base×3
    # 🔥 🧢 cap ×5  (6th 🎯 still ×5)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    for _ in range(4):
        𓋂.𓋿(10)                              # 🔥1..4
    𓅐 = 𓋂.𓋼
    𓋂.𓋿(10)                                  # 🔥5 → ×5 , +40
    assert 𓋂.𓋼 - 𓅐 == 40
    𓅐 = 𓋂.𓋼
    𓋂.𓋿(10)                                  # 🔥6 → 🧢 ×5 , +40 (🚫×6)
    assert 𓋂.𓋻 == 6
    assert 𓋂.𓋼 - 𓅐 == 40                     # 🧢 cap held
    # 😿 bonk → 🔥 0 reset
    𓋃 = 𓅓.𓉔(random.Random(2), 𓊵𓈖=0)
    𓋃.𓋻 = 4
    𓋃.𓃠 = (5, 5)
    𓋃.𓃥 = (5, 6)                             # adjacent → bonk
    𓋃.𓃥𓎗()
    assert 𓋃.𓊟 == 1
    assert 𓋃.𓋻 == 0                          # 🔥 reset
    # 🏆 folds 🔥 combo bonus
    𓋄 = 𓅓.𓉔(random.Random(0))
    𓋄.𓏰 = 10
    𓋄.𓊛 = 2
    𓋄.𓋼 = 17
    assert 𓋄.𓊙() == max(0, 100 - 10) + 5 * 2 + 17
    # 🎯 integration : 🐟😋 via 𓂷 → 🔥+1 , 🥛😋 → 🔥+1
    𓋅 = 𓅓.𓉔(random.Random(1), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False)
    𓋅.𓁉 = (0, 7)         # 🐭 far
    𓋅.𓇬 = (9, 0)         # 🧀 elsewhere
    𓋅.𓊮 = (9, 2)         # 🥛 elsewhere
    𓋅.𓃠 = (2, 2)
    𓋅.𓆛 = (3, 2)         # 🐟 →➡️
    𓋅.𓂷("➡️")
    assert 𓋅.𓊛 == 1 and 𓋅.𓋻 == 1            # 🐟😋 → 🔥1
    # 🖼️ HUD 🔥×N  (plain + 🌈 , 🔥≥3 → ✨)
    𓋆 = 𓅓.𓉔(random.Random(0))
    𓋆.𓋻 = 2
    assert "🔥×2" in 𓋆.𓁑()
    assert "✨" not in 𓋆.𓁑()                  # <3 → 🚫✨
    𓋆.𓋻 = 3
    assert "🔥×3✨" in 𓋆.𓁑()                  # ≥3 → ✨
    𓂮 = 𓅓.𓋊(𓋆.𓁑(), True)
    assert "\033[" in 𓂮 and "🔥" in 𓂮         # 🌈 wrap
    # 🔗✅ 120🎲 ↔️ 🚫💥  (🏁 clean streak ∀)
    for 𓊃 in range(120):
        𓋇 = 𓅓.𓉔(random.Random(𓊃))
        assert 𓋇.𓋻 == 0 and 𓋇.𓋼 == 0
        assert "🔥×0" in 𓋇.𓁑()


def 𓊪𓁉𓂋():
    # 🐭🐭  pack : K = f(🌊) 🧢 , 🏦 𓁉𓂋 list , 🚧 back-compat 𓁉 ↔️ [0]
    assert 𓅓.𓁉𓈖(1) == 1 and 𓅓.𓁉𓈖(4) == 1      # 🌊<5 → solo 🐭
    assert 𓅓.𓁉𓈖(5) == 1                        # 🌊5️⃣ → K=1
    assert 𓅓.𓁉𓈖(6) == 2 and 𓅓.𓁉𓈖(7) == 2      # 🌊7️⃣ → K=2
    assert 𓅓.𓁉𓈖(9) == 3                        # 🌊9️⃣ → K=3
    assert 𓅓.𓁉𓈖(99) == 𓅓.𓁉𓈎                   # 🧢 cap ×4
    # 🚧 back-compat :  𓁉 ↔️ 𓁉𓂋[0]
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert 𓋁.𓁉𓂋 == [𓋁.𓁉] and len(𓋁.𓊚𓂋) == 1
    𓋁.𓁉 = (4, 4)
    assert 𓋁.𓁉𓂋[0] == (4, 4) and 𓋁.𓁉 == (4, 4)
    # 🐭🐭 grow → 🔗✅ ∀🐭 , ≠🐈🧀🐟🥛 , 😮‍💨 per 🐭
    𓋁.𓁎(3)
    assert len(𓋁.𓁉𓂋) == 3 and 𓋁.𓊚𓂋 == [0, 0, 0]
    𓂭 = 𓋁.𓃰(𓋁.𓃠)
    for 𓅘 in 𓋁.𓁉𓂋:
        assert 𓅘 in 𓂭                          # 🔗✅
        assert 𓅘 not in (𓋁.𓃠, 𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮)
    assert len(set(𓋁.𓁉𓂋)) == 3                 # 🚫 stack


def 𓊪𓁏():
    # 🎯  catch 🐭 → pop + 🔥 combo ;  😻 ⇔ ∀🐭 caught  (partial → 🚫😻)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋁.𓇬 = (0, 0)
    𓋁.𓁉𓂋 = [(5, 5), (8, 2)]
    𓋁.𓊚𓂋 = [0, 0]
    𓋁.𓃠 = (4, 5)
    assert 𓋁.𓂷("➡️") is False                  # 🎯 1️⃣🐭 → 🚫😻 (partial)
    assert 𓋁.𓄊 is False
    assert len(𓋁.𓁉𓂋) == 1 and len(𓋁.𓊚𓂋) == 1
    assert 𓋁.𓋻 == 1                            # 🔥 +1 / 🐭
    assert 𓋁.𓁍 == (5, 5)                       # 📍 last 🐭
    # ∀🐭 → 😻
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋂.𓇬 = (0, 0)
    𓋂.𓁉𓂋 = [(5, 5)]
    𓋂.𓊚𓂋 = [0]
    𓋂.𓃠 = (4, 5)
    assert 𓋂.𓂷("➡️") is True                   # ∀🐭 🎯 → 😻
    assert 𓋂.𓄊 is True and 𓋂.𓁉𓂋 == []
    assert 𓋂.𓁉 == (5, 5)                       # 𓁉 → 📍 last  (🚫💥 🖼️)
    assert 𓋂.𓁐().count("🐭") == 0              # 🖼️ 🚫🐭 left


def 𓊪𓁉𓎗():
    # 🐭🐭  ∀🐭 own 🧠 :  👀near → 💨 , far → 🧀😋 ;  😮‍💨 per 🐭
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋁.𓃠 = (5, 4)
    𓋁.𓇬 = (0, 0)
    𓋁.𓁉𓂋 = [(5, 6), (9, 7)]                    # 🐭a near , 🐭b far
    𓋁.𓊚𓂋 = [0, 0]
    𓂭 = 𓋁.𓃰(𓋁.𓃠)
    𓅐 = 𓋁.𓅓𓎗(0)                               # 🐭a 😱💨
    assert 𓂭.get(𓅐, 0) > 𓂭.get((5, 6), 0)      # 💨 away
    assert 𓋁.𓊚𓂋 == [1, 0]                      # 😮‍💨 only 🐭a
    𓅑 = 𓋁.𓅓𓎗(1)                               # 🐭b → 🧀😋
    assert 𓋁.𓃰(𓋁.𓇬).get(𓅑, 99) < 𓋁.𓃰(𓋁.𓇬).get((9, 7), 99)
    # 🐭🐭 both 💨 per 🐾  (𓂷 → ∀ 🐭 move)
    𓋂 = 𓅓.𓉔(random.Random(1), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋂.𓃠 = (5, 4)
    𓋂.𓇬 = (0, 0)
    𓋂.𓁉𓂋 = [(5, 6), (6, 6)]
    𓋂.𓊚𓂋 = [0, 0]
    𓅔 = list(𓋂.𓁉𓂋)
    𓋂.𓂷("🐾")
    assert 𓋂.𓁉𓂋 != 𓅔                          # 🐭🐭 💨


def 𓊪𓁉𓎗𓆊():
    # 🚫🥞 (#30) :  ∀🐭 📍 distinct  —  🐭 🚫 step on 🐭
    # 🥇 🧠 unit :  🐭a 💨 → 🚫 tile of 🐭b  (even if max 📏🐈)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋁.𓃠 = (5, 4)
    𓋁.𓇬 = (0, 0)
    𓋁.𓁉𓂋 = [(5, 6), (5, 7)]                    # 🐭a 😱 , 🐭b 🀄 @ best flee tile
    𓋁.𓊚𓂋 = [0, 0]
    assert 𓋁.𓅓𓎗(0) != (5, 7)                   # 🚫🥞 : 🐭b tile 🚷
    # 🧀😋 🌿 : 🐭a → 🧀 , 🐭b 🚧 on the way  → 🚫🥞
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋂.𓃠 = (9, 9)                               # 🐈 far → 🚫😱
    𓋂.𓇬 = (0, 0)
    𓋂.𓁉𓂋 = [(3, 3), (2, 3)]                    # 🐭b @ 🐭a ➡️🧀 step
    𓋂.𓊚𓂋 = [0, 0]
    assert 𓋂.𓅓𓎗(0) != (2, 3)                   # 🚫🥞
    # 🎮 e2e :  ∀🌊 × 🎲 → 🚫🥞 ∀ 🐾
    for 𓊍 in (6, 8, 9):
        for 𓊃 in range(6):
            𓉔𓏤 = 𓅓.𓊆(𓊍, random.Random(𓊃))
            for _ in range(200):
                if 𓉔𓏤.𓂷(𓅓.𓊄(𓉔𓏤)):
                    break
                assert len(set(𓉔𓏤.𓁉𓂋)) == len(𓉔𓏤.𓁉𓂋)   # 🚫🥞 ∀🐾
    # 𓊐 𓊫 :  🚫 tiles honored , 🈳 𓊫 → 🚧 back-compat (🐕 🚫 touched)
    𓋃 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    assert 𓋃.𓊐((3, 3), (0, 3)) == (2, 3)        # 🈳 𓊫 → ➡️🎯
    assert 𓋃.𓊐((3, 3), (0, 3), {(2, 3)}) != (2, 3)


def 𓊪𓁉𓊆():
    # 🎚️  🌊 → 🐭🐭 pack @ ≥5️⃣ , 🖼️ HUD 🐭×N , 🔗✅ ∀🐭
    for 𓊍 in range(1, 10):
        𓋁 = 𓅓.𓊆(𓊍, random.Random(𓊍))
        assert len(𓋁.𓁉𓂋) == 𓅓.𓁉𓈖(𓊍), f"🙀 🎚️={𓊍}"
        assert len(𓋁.𓊚𓂋) == len(𓋁.𓁉𓂋)
        𓂭 = 𓋁.𓃰(𓋁.𓃠)
        for 𓅘 in 𓋁.𓁉𓂋:
            assert 𓅘 in 𓂭, f"🙀🔗 🎚️={𓊍}"      # 🔗✅ ∀🐭
    # 🖼️ HUD 🐭×N remaining  (+ ❤️ + 🔥 🤝 , 🚫 collide)
    𓋂 = 𓅓.𓊆(9, random.Random(0))
    assert "🐭×3" in 𓋂.𓁑()
    assert "❤️×9" in 𓋂.𓁑() and "🔥×0" in 𓋂.𓁑()
    𓋂.𓋻 = 3
    assert "🔥×3✨" in 𓋂.𓁑()
    𓂮 = 𓅓.𓋊(𓋂.𓁑(), True)
    assert "\033[" in 𓂮 and "🐭" in 𓂮           # 🌈 wrap
    assert 𓅓.𓋊(𓋂.𓁑(), False) == 𓋂.𓁑()        # 🚫⚑ ↔️
    # 🖼️ 🗺️ → ∀🐭 drawn
    assert 𓋂.𓁐().count("🐭") == len(set(𓋂.𓁉𓂋))


def 𓊪𓁉𓊰():
    # 🥛⚡  pounce 📏≤2 → 🎯 nearest 🐭 of 🐭🐭  (🚫 ∀ at once)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋁.𓇬 = (0, 0)
    𓋁.𓆛 = (0, 1)
    𓋁.𓊮 = (0, 2)
    𓋁.𓃠 = (5, 5)
    𓋁.𓁉𓂋 = [(5, 7), (5, 6)]                    # 📏 2 , 📏 1  → 🎯 nearest
    𓋁.𓊚𓂋 = [0, 0]
    𓋁.𓊰 = 2
    assert 𓋁.𓂷("🐾") is False                  # 1️⃣🐭 only → 🚫😻
    assert 𓋁.𓁍 == (5, 6)                       # 😼 nearest 🎯
    assert len(𓋁.𓁉𓂋) == 1


def 𓊪𓊄𓁉():
    # 🐈🧠  🎯 nearest 🐭  +  🧶 throw @ 🐕📏🤏  (🚫 stalemate)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋁.𓃠 = (5, 5)
    𓋁.𓁉𓂋 = [(0, 0), (7, 5)]
    𓋁.𓊚𓂋 = [0, 0]
    assert 𓅓.𓊄𓁉(𓋁) == (7, 5)                  # 🎯 nearest
    assert 𓅓.𓊄(𓋁) == "➡️"                     # 🐈 → nearest 🐭
    # 🧶 : 🐕 📏≤2 + 🧶 unspent → 🎾 throw
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋂.𓃠 = (5, 5)
    𓋂.𓁉 = (0, 0)
    𓋂.𓃥 = (5, 6)                               # 🐕 📏=1
    assert 𓅓.𓊄(𓋂) == "🧶"
    𓋂.𓋯 = True                                 # 🧶 spent → 🚫 2nd
    assert 𓅓.𓊄(𓋂) != "🧶"
    # 🐕 far → 🚫 🎾 waste
    𓋃 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋃.𓃠 = (5, 5)
    𓋃.𓁉 = (0, 0)
    𓋃.𓃥 = (10, 0)
    assert 𓅓.𓊄(𓋃) != "🧶"
    # 🐭🐭 🔗✅ 120🎲 ↔️ 🚫💥  (🌊9️⃣ pack : ∀🐭 reachable @ 🏁)
    for 𓊃 in range(120):
        𓋄 = 𓅓.𓊆(9, random.Random(𓊃))
        𓂭 = 𓋄.𓃰(𓋄.𓃠)
        assert len(𓋄.𓁉𓂋) == 3
        for 𓅘 in 𓋄.𓁉𓂋:
            assert 𓅘 in 𓂭, f"🙀🔗 seed={𓊃}"


def 𓊪𓋃𓁋():
    # ⏱️  time-attack ⚑ :  🚫⚑ default → ⏳ ∞ (🚫 tick , 🚫 HUD , 🚫 🏆)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert 𓋁.𓋃𓁋 is False                      # 🏁 opt-in → off
    𓋁.𓁉 = (0, 7)                              # 🐭 far (🚫 catch)
    𓅐 = 𓋁.𓋂
    𓋁.𓂷("🐾")
    assert 𓋁.𓋂 == 𓅐                          # 🚫⚑ → ⏳ 🚫 tick (∞)
    assert "⏳×" not in 𓋁.𓁑()                  # 🖼️ HUD ↔️ unchanged
    𓋁.𓋂 = 0
    𓋁.𓂷("🐾")
    assert 𓋁.𓋺 is False                       # ⏳0 + 🚫⚑ → 🚫💀
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋂.𓏰 = 10
    assert 𓋂.𓊙() == 90                        # 🚫⚑ → 🚫 ⏳ leftover


def 𓊪𓋃𓈖():
    # ⏱️  ⏳ = 40 + 8×🌊  (🌊 scaling , 𓊆 factory ⚑)
    assert 𓅓.𓋃𓈖(1) == 48
    assert 𓅓.𓋃𓈖(5) == 80
    assert 𓅓.𓋃𓈖(9) == 112
    for 𓊍 in range(1, 10):
        𓋁 = 𓅓.𓊆(𓊍, random.Random(0), 𓋃𓁋=True)
        assert 𓋁.𓋃𓁋 is True
        assert 𓋁.𓋂 == 40 + 8 * 𓊍, f"🙀 🎚️={𓊍}"
        𓋂 = 𓅓.𓊆(𓊍, random.Random(0))         # 🚫⚑ default
        assert 𓋂.𓋃𓁋 is False


def 𓊪𓋂():
    # ⏱️  ⏳ tick / 🐾  →  ⏳0 → 💀 🎮🔚 ;  🎯 before ⏳0 → 😻 (🚫💀)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False, 𓋃𓁋=True)
    𓋁.𓁉 = (0, 7)                              # 🐭 far
    𓋁.𓇬 = (5, 0)
    𓅐 = 𓋁.𓋂
    𓋁.𓂷("🐾")
    assert 𓋁.𓋂 == 𓅐 - 1                      # ⏳ −1 / 🐾
    𓋁.𓂷("🐾")
    assert 𓋁.𓋂 == 𓅐 - 2
    assert 𓋁.𓋾() is False                     # ⏳ left → 🎮 on
    # ⏳ 1 → 🐾 → 0 → 💀 🎮🔚 + 🚫😻
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False, 𓋃𓁋=True)
    𓋂.𓁉 = (0, 7)
    𓋂.𓇬 = (5, 0)
    𓋂.𓋂 = 1
    assert 𓋂.𓂷("🐾") is True                  # 🎮🔚 via ⏳0
    assert 𓋂.𓋂 == 0
    assert 𓋂.𓋺 is True and 𓋂.𓄊 is False      # 💀 lose , 🚫😻
    assert 𓋂.𓋾() is True
    assert 𓋂.𓋹 == 9                           # ❤️ full → 💀 = ⏳ , 🚫🐕
    # 🎯 on last ⏳ → 😻 win  (🚫💀)
    𓋃 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False, 𓋃𓁋=True)
    𓋃.𓃠 = (5, 5)
    𓋃.𓁉 = (6, 5)                              # 👉 adjacent
    𓋃.𓋂 = 1
    assert 𓋃.𓂷("➡️") is True
    assert 𓋃.𓄊 is True and 𓋃.𓋺 is False      # 😻 , 🚫💀
    # ⏳ ⬇️ past 0 → 💀 stays , 🏆 🚧 ≥ base
    assert max(0, 𓋃.𓋂) >= 0


def 𓊪𓋂𓊙():
    # 🏆  ⏳ leftover bonus  (⚑ on)  folded into 𓊙
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋃𓁋=True)
    𓋁.𓏰 = 10
    𓋁.𓊛 = 2
    𓋁.𓋂 = 20                                  # ⏳ leftover
    assert 𓋁.𓊙() == (100 - 10) + 5 * 2 + 20   # + ⏳ bonus
    𓋁.𓋂 = -3                                  # ⏳ 💀 → 🚧 ≥0
    assert 𓋁.𓊙() == (100 - 10) + 5 * 2
    # ⏳ 🏆 ⚔️ 🔥 combo 🤝  (both fold)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋃𓁋=True)
    𓋂.𓏰 = 10
    𓋂.𓋼 = 17
    𓋂.𓋂 = 5
    assert 𓋂.𓊙() == 90 + 17 + 5


def 𓊪𓋃𓁑():
    # 🖼️ HUD ⏱️×N  (⚑ on) , ⏳≤5 → 🟥 flash , 🌈 wrap , 🤝 ❤️🐭🔥  (🚫 collide)
    𓋁 = 𓅓.𓊆(5, random.Random(0), 𓋃𓁋=True)
    assert "⏳×80" in 𓋁.𓁑()                   # 🀄 ⏳ = budget  (≠ ⏱️ = 𓏰 ‼️)
    assert "⏱️×" not in 𓋁.𓁑()                 # 🚫 collide 🀄
    assert "🟥" not in 𓋁.𓁑()                  # ⏳ ⬆️ → 🚫 flash
    assert "❤️×9" in 𓋁.𓁑() and "🐭×1" in 𓋁.𓁑() and "🔥×0" in 𓋁.𓁑()
    𓋁.𓋂 = 5
    assert "⏳×5🟥" in 𓋁.𓁑()                  # ⏳ ≤5 → 🟥
    𓋁.𓋂 = 0
    assert "⏳×0🟥" in 𓋁.𓁑()                  # 🚧 ≥0
    𓋁.𓋂 = -4
    assert "⏳×0🟥" in 𓋁.𓁑()                  # 🚧 🚫 negative
    𓂮 = 𓅓.𓋊(𓋁.𓁑(), True)
    assert "\033[" in 𓂮 and "⏳" in 𓂮         # 🌈 wrap
    assert 𓅓.𓋊(𓋁.𓁑(), False) == 𓋁.𓁑()      # 🚫⚑ ↔️


def 𓊪𓋺𓁐():
    # 💀 🖼️  :  ⏳0 → 💀⏱️  ;  ❤️0 → 💀🐕
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋃𓁋=True)
    𓋁.𓋂 = 0
    𓋁.𓋺 = True
    assert "💀⏳" in 𓅓.𓋺𓁐(𓋁) and "⏳×0" in 𓅓.𓋺𓁐(𓋁)
    assert "❤️×9" in 𓅓.𓋺𓁐(𓋁)                # ❤️ 🖼️ kept  (🚫 🙈)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋂.𓋹 = 0
    𓋂.𓋺 = True
    assert "💀🐕" in 𓅓.𓋺𓁐(𓋂) and "❤️×0" in 𓅓.𓋺𓁐(𓋂)
    # ⚔️ ❤️0 ∧ ⏳0 🀄 🐾 → 🐕 wins  (🚫 🙈 ❤️×0)
    𓋃 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋃𓁋=True)
    𓋃.𓋹 = 0
    𓋃.𓋂 = 0
    𓋃.𓋺 = True
    assert "💀🐕" in 𓅓.𓋺𓁐(𓋃) and "❤️×0" in 𓅓.𓋺𓁐(𓋃)


def 𓊪𓎋𓉏():
    # 💾 📜🔝 split by 🏁 mode :  ⏱️ 🏆 ➕⏳ ≫ classic 🏆 → 🚫 pollute ‼️
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋃𓁋=True)
    assert 𓅓.𓎋𓉏(𓋁) == 𓅓.𓎋𓊪                 # 🏁 classic 🛤️
    assert 𓅓.𓎋𓉏(𓋂) == 𓅓.𓎋𓊪𓋃               # ⏱️ 🏁 🛤️
    assert 𓅓.𓎋𓊪 != 𓅓.𓎋𓊪𓋃                   # 🛤️ ≠ 🛤️
    # 📇 : ⏱️ → ⏳ marker ; 🚫⚑ → 🚫 key
    𓋁.𓏰 = 10
    assert "⏳" not in 𓅓.𓎎(𓋁)
    𓋂.𓏰 = 10
    𓋂.𓋂 = 33
    𓆳 = 𓅓.𓎎(𓋂)
    assert 𓆳["⏳"] == 33                       # ⏳ leftover tagged
    assert 𓆳["⏱️"] == 10                       # ⏱️ = 𓏰 turns  (🀄 ≠ ⏳)
    𓋂.𓋂 = -5
    assert 𓅓.𓎎(𓋂)["⏳"] == 0                  # 🚧 ≥0
    # 🖼️ 📜🔝 : ⏳ shown ⇔ ⏱️ 🏁
    assert "⏳33" in 𓅓.𓎍([𓆳])
    assert "⏳" not in 𓅓.𓎍([𓅓.𓎎(𓋁)])
    # 💾 e2e : 2 🏁 → 2 📜  (🚫 🤝 mix)
    with tempfile.TemporaryDirectory() as 𓊪𓉏:
        𓄿 = os.path.join(𓊪𓉏, "a.json")
        𓃀 = os.path.join(𓊪𓉏, "b.json")
        𓅓.𓎌(𓅓.𓎎(𓋁), 𓄿)                     # classic
        𓅓.𓎌(𓅓.𓎎(𓋂), 𓃀)                     # ⏱️
        assert len(𓅓.𓎋(𓄿)) == 1 and len(𓅓.𓎋(𓃀)) == 1
        assert "⏳" not in 𓅓.𓎋(𓄿)[0]          # classic 📜 🚫 ⏱️ record
        assert "⏳" in 𓅓.𓎋(𓃀)[0]


def 𓊪𓋃𓂺():
    # 🏁  ⚑⏱️ parse + 🤝 🌈 🤖 🎚️  ;  🎮🔚 → 📜🔝  (💀 ⏳0 → 📇)
    𓋁 = 𓅓.𓊆(9, random.Random(0), 𓋃𓁋=True)
    assert 𓋁.𓋂 == 112 and 𓋁.𓊍 == 9
    # 🔗✅ 120🎲 ↔️ 🚫💥 :  ⏱️ ON → 🎮🔚 always (😻 or 💀) , 🚫 hang
    for 𓊃 in range(120):
        𓋂 = 𓅓.𓊆(5, random.Random(𓊃), 𓋃𓁋=True)
        𓅐 = 𓋂.𓋂
        for _ in range(300):
            if 𓋂.𓂷(𓅓.𓊄(𓋂)):
                break
        assert 𓋂.𓋾() is True, f"🙀 seed={𓊃}"   # 🎮🔚 ‼️  (⏳ 🚧 → 🚫 ∞)
        assert 𓋂.𓏰 <= 𓅐, f"🙀⏳ seed={𓊃}"     # ⏱️ ≤ ⏳ budget
        assert 𓋂.𓄊 or 𓋂.𓋺                    # 😻 or 💀
        assert 𓅓.𓎎(𓋂)["🏆"] >= 0                 # 📇 ✅
    # 🚫⚑ → 🚫 ⏳ 🚧  (long 🎮 ok)
    𓋃 = 𓅓.𓊆(5, random.Random(0))
    for _ in range(300):
        if 𓋃.𓂷(𓅓.𓊄(𓋃)):
            break
    assert 𓋃.𓋂 == 80                          # ⏳ 🚫 ticked


def 𓊪𓋊():
    # 🌈  colorize : ⚑ → ANSI wrap , 🚫⚑ → 📺 ↔️ plain
    𓊞 = "🐈🟩🧱\n🐭🐕🥛"
    𓂭 = 𓅓.𓋊(𓊞, True)
    assert "\033[" in 𓂭               # 🎨 ANSI present
    assert "\033[0m" in 𓂭             # 🔚 reset
    assert "🐈" in 𓂭 and "🐕" in 𓂭    # 🀄 kept
    assert 𓅓.𓋊(𓊞, False) == 𓊞        # 🚫⚑ → ↔️
    assert 𓅓.𓋊(𓊞) == 𓊞               # default plain


def 𓊪𓋋():
    # 🌈🤖  : color 🗺️ strips → plain 🗺️  (🎨 reversible , 🀄 ↔️)
    import re as 𓂯
    𓋁 = 𓅓.𓉔(random.Random(0))
    𓊞 = 𓋁.𓁐()
    𓂮 = 𓅓.𓋊(𓊞, True)
    𓂰 = 𓂯.sub(r"\033\[[0-9;]*m", "", 𓂮)
    assert 𓂰 == 𓊞                     # 🎨 reversible → 📺 ↔️
    assert 𓂮.count("\033[0m") > 0     # 🌈 wrapped 🀄


def 𓊪𓎋():
    # 💾📥  missing 🛤️ → 📜🕳️  ; 🙀💔 json → 📜🕳️
    𓊪𓉏 = os.path.join(tempfile.gettempdir(), "🚫👻.json")
    if os.path.exists(𓊪𓉏):
        os.remove(𓊪𓉏)
    assert 𓅓.𓎋(𓊪𓉏) == []
    with open(𓊪𓉏, "w", encoding="utf-8") as 𓆑:
        𓆑.write("🙀🚫json")
    assert 𓅓.𓎋(𓊪𓉏) == []          # 💔 → 📜🕳️
    os.remove(𓊪𓉏)


def 𓊪𓎌():
    # 💾📤  add → sort 🔽🏆 → ✂️ top-N → 💾 persist
    with tempfile.TemporaryDirectory() as 𓊭:
        𓊪𓉏 = os.path.join(𓊭, "🏆.json")
        𓅓.𓎌({"🏆": 50, "⏱️": 20}, 𓊪𓉏)
        𓅓.𓎌({"🏆": 90, "⏱️": 10}, 𓊪𓉏)
        𓂏 = 𓅓.𓎌({"🏆": 70, "⏱️": 30}, 𓊪𓉏)
        assert [𓅘["🏆"] for 𓅘 in 𓂏] == [90, 70, 50]   # 🔽🏆
        # 💾 persist ↔️ reload
        assert [𓅘["🏆"] for 𓅘 in 𓅓.𓎋(𓊪𓉏)] == [90, 70, 50]
        # ✂️ top-N
        for 𓇋 in range(20):
            𓅓.𓎌({"🏆": 𓇋, "⏱️": 0}, 𓊪𓉏, 𓈖=3)
        𓂐 = 𓅓.𓎋(𓊪𓉏)
        assert len(𓂐) == 3
        assert [𓅘["🏆"] for 𓅘 in 𓂐] == [90, 70, 50]
        # tie 🏆 → 🔼⏱️ first
        𓅓.𓎌({"🏆": 90, "⏱️": 5}, 𓊪𓉏, 𓈖=5)
        𓂑 = 𓅓.𓎋(𓊪𓉏)
        assert 𓂑[0] == {"🏆": 90, "⏱️": 5}     # ⏱️5 < ⏱️10


def 𓊪𓎍():
    # 🖼️  📜🔝 render  : 🕳️ → 📜🕳️ ; 🎁 → rank + 🏆
    assert 𓅓.𓎍([]) == "📜🕳️"
    𓊮 = 𓅓.𓎍([{"🏆": 88, "⏱️": 12, "🐟": 2, "🥛": 1, "🐦": 3, "😿": 0}])
    assert "🏆📜🔝" in 𓊮
    assert "1." in 𓊮
    assert "🏆88" in 𓊮
    assert "🐦3" in 𓊮


def 𓊪𓊆():
    # 🎚️  🌊 factory : 🚧 1..9 , 🐕@≥2 , 🐦@≥3 , 🕳️@≥4 , 💨🐕@≥7 , 👀🐭@≥5
    # 🚧 clamp
    assert 𓅓.𓊆(0, random.Random(0)).𓊍 == 1
    assert 𓅓.𓊆(99, random.Random(0)).𓊍 == 9
    assert 𓅓.𓊆(5, random.Random(0)).𓊍 == 5
    # 🌊1️⃣ → 🚫🐕🐦🕳️
    𓋁 = 𓅓.𓊆(1, random.Random(0))
    assert 𓋁.𓃥 is None and 𓋁.𓅱 is None and 𓋁.𓎛 is None
    # 🌊2️⃣ → 🐕 on
    assert 𓅓.𓊆(2, random.Random(0)).𓃥 is not None
    # 🌊3️⃣ → 🐦 on
    assert 𓅓.𓊆(3, random.Random(0)).𓅱 is not None
    # 🌊4️⃣ → 🕳️ on
    assert 𓅓.𓊆(4, random.Random(0)).𓎛 is not None
    # 🌊5️⃣ → 👀🐭 sharper
    assert 𓅓.𓊆(5, random.Random(0)).𓋴 == 4
    # 🌊7️⃣ → 🐕💨 full-speed
    assert 𓅓.𓊆(7, random.Random(0)).𓃥𓎿 == 1
    assert 𓅓.𓊆(6, random.Random(0)).𓃥𓎿 == 𓅓.𓉔.𓃥𓎿   # half-speed still
    # 🧱 grows with 🎚️  (record tag)
    assert 𓅓.𓎎(𓅓.𓊆(4, random.Random(0)))["🎚️"] == 4


def 𓊪𓊆𓄊():
    # 🎚️  ∀ 🌊 1..9  →  🔗 solvable  +  🐈 😻 rate ≥ 5/6 per 🌊 , Σ ≥ 52/54
    #
    # 🀄 ‼️  «∀ 😻» = 🚫 invariant : 🐈🧠 greedy stateless → 🐕💨 tail (#27)
    #        📊 1080🎲 : 🏁 base 1044 😻 (36 loss) · 🌟🧊 1059 😻 (21 loss)
    #        → 🧪 rate , 🚫 ∀  (🍀 seed luck ≠ ✅ ; 🎲 stream shift → 🆕 🗺️)
    𓊾 = []
    for 𓊍 in range(1, 10):
        𓄊 = 0
        for 𓊃 in range(6):
            𓋁 = 𓅓.𓊆(𓊍, random.Random(𓊃 + 𓊍 * 10))
            for _ in range(600):
                if 𓋁.𓂷(𓅓.𓊄(𓋁)):
                    break
            𓄊 += 1 if 𓋁.𓄊 else 0
        assert 𓄊 >= 5, f"🙀 🎚️={𓊍} → 😻 {𓄊}/6"      # 🔗 solvable ∀🌊
        𓊾.append(𓄊)
    assert sum(𓊾) >= 52, f"🙀 Σ 😻 {sum(𓊾)}/54"     # 😻 rate 🚧


def 𓊪𓋔():
    # 🌟🧊  spawn :  🧊 ⇔ 🐕  (🚫🐕 → 🚫🧊)  ·  🚫 overlap 🀄  ·  ⚑ off
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert 𓋁.𓋔 is not None and 𓋁.𓋕 == 0
    assert 𓋁.𓋔 not in (𓋁.𓃠, 𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮, 𓋁.𓅱, 𓋁.𓃥, *𓋁.𓁉𓂋)
    assert 𓋁.𓋔 not in 𓋁.𓎜() and 𓋁.𓋔 not in 𓋁.𓊵
    assert 𓋁.𓋔 in 𓋁.𓃰(𓋁.𓃠)                  # 🔗✅ reachable
    # 🚫🐕 → 🚫🧊  (🧊 = 🐕 counter → 🚫🐕 = 🚫 sense)
    assert 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False).𓋔 is None
    # ⚑ off → 🚫🧊  (🚧 opt-out)
    assert 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋔𓁋=False).𓋔 is None
    # 🎚️ : 🧊 @ 🌊≥2️⃣  (⇔ 🐕)
    assert 𓅓.𓊆(1, random.Random(0)).𓋔 is None
    for 𓊍 in range(2, 10):
        assert 𓅓.𓊆(𓊍, random.Random(0)).𓋔 is not None, f"🙀 🌊{𓊍}"
    # 🐭 spawn ≠ 🧊  (𓁉𓆙 excl)
    𓋂 = 𓅓.𓉔(random.Random(3), 𓊵𓈖=0)
    𓋂.𓁎(4)
    assert 𓋂.𓋔 not in 𓋂.𓁉𓂋


def 𓊪𓋕():
    # 🌟🧊  🐈🧊😋 → 🐕 ❄️ 5🐾 (🚫🐾 , 🚫😿) → thaw → 🐕 💨 again  ·  🧊 respawn
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋁.𓁉𓂋 = [(10, 7)]                          # 🐭 far → 🚫 😻 mid-🧪
    𓋁.𓊚𓂋 = [0]
    𓋂 = 𓋁.𓋔
    𓋁.𓃠 = 𓋂
    𓋁.𓃥 = (5, 0)
    𓋁.𓂷("🐾")                                  # 🐈 @ 🧊 → 😋
    assert 𓋁.𓋕 == 𓋁.𓋕𓊞 == 5                  # ❄️ armed
    assert 𓋁.𓋔 is not None and 𓋁.𓋔 != 𓋂      # 🧊 respawn 🎲
    assert 𓋁.𓋻 == 0 and 𓋁.𓊙() >= 0            # 🛠️ tool : 🚫🔥 , 🚫🏆
    # 🐕 ❄️ → 🚫🐾  ∀ ❄️⏳  :  grab 🐾 = skip 🥇 → Σ 5 skips  (𓋕𓊞=5)
    𓋁.𓋔 = None                                 # 🚫 re-grab noise
    𓋃 = 𓋁.𓃥
    for 𓇋 in range(4):                         # 🐾 #2..#5  (grab 🐾 = #1)
        𓋁.𓂷("🐾")
        assert 𓋁.𓃥 == 𓋃, f"🙀 🐕 💨 while ❄️ @ {𓇋}"
    assert 𓋁.𓋕 == 1                            # ❄️ ⏳ 1 left
    # thaw 🐾 #6 → 🐕 💨 again
    𓋁.𓂷("🐾")
    assert 𓋁.𓋕 == 0                            # thaw
    𓋄 = 𓋁.𓃥
    for _ in range(4):
        𓋁.𓂷("🐾")
    assert 𓋁.𓃥 != 𓋄                           # 🐕 💨🐈 resumed
    # ❄️ → 🚫😿 bonk  (🐕 👉🐈 tile , frozen → 🚫 −❤️)
    𓋅 = 𓅓.𓉔(random.Random(1), 𓊵𓈖=0, 𓅱𓁋=False, 𓎛𓁋=False)
    𓋅.𓁉𓂋 = [(10, 7)]
    𓋅.𓊚𓂋 = [0]
    𓋅.𓋕 = 3
    𓋅.𓃠 = (4, 4)
    𓋅.𓃥 = (4, 5)                               # 🐕 adjacent ‼️
    𓋆 = 𓋅.𓋹
    𓋅.𓂷("🐾")
    assert 𓋅.𓃥 == (4, 5) and 𓋅.𓋹 == 𓋆 and 𓋅.𓊟 == 0   # ❄️ → 🚫🐾 , 🚫😿


def 𓊪𓋗():
    # 🌟🧊  📜 cycle 👀 :  period-2/3/4 → 🧱 stalemate  (#27 🧠 memory ; 🕳️ 4-cycle)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert 𓋁.𓋗() is False                      # 📜 🈳 → 🚫
    for 𓅘 in [(1, 1), (1, 2), (1, 1)]:
        𓋁.𓋗𓂋.append(𓅘)
    assert 𓋁.𓋗() is False                      # <4 📜
    𓋁.𓋗𓂋.append((1, 2))
    assert 𓋁.𓋗() is True                       # A B A B → 🧱  (period-2)
    𓋁.𓋗𓂋.append((3, 3))                       # …A B A B C → 🚫 (🚫 fresh cycle)
    assert 𓋁.𓋗() is False
    # 💤 🐾 (A A A A) → 🚫 cycle  (𓄾 ≠ 𓃀 🚧 : blocked ≠ loop)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    for _ in range(8):
        𓋂.𓋗𓂋.append((2, 2))
    assert 𓋂.𓋗() is False
    # 🕳️ portal 4-cycle : A B C D A B C D  →  🧱  (2-cycle detect 🙈 → #27 tail)
    𓋃 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    for 𓅘 in [(1, 4), (8, 1), (7, 1), (2, 4)] * 2:
        𓋃.𓋗𓂋.append(𓅘)
    assert 𓋃.𓋗() is True                       # period-4 → 🧱 ‼️
    # 3-cycle : A B C A B C  →  🧱
    𓋄 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    for 𓅘 in [(0, 0), (0, 1), (0, 2)] * 2:
        𓋄.𓋗𓂋.append(𓅘)
    assert 𓋄.𓋗() is True                       # period-3 → 🧱
    # 🚫 false-⚡ : monotone walk A B C D E F G H → 🚫 cycle
    𓋅 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    for 𓅘 in [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]:
        𓋅.𓋗𓂋.append(𓅘)
    assert 𓋅.𓋗() is False                      # 🚫 repeat → 🚫🧱
    # 🐾 → 📜 grows  (𓂷 feeds 𓋗𓂋)
    𓋆 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋆.𓂷("➡️")
    assert list(𓋆.𓋗𓂋)[-1] == 𓋆.𓃠


def 𓊪𓋚():
    # 🧱  cycle 🔁 streak 𓋚  (#27 🌙7️⃣) :  transient 🌀 ≠ 🧱  →  𓂷 tallies
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
    assert 𓋁.𓋚 == 0                            # 🐣 → 0
    𓋁.𓃠 = (5, 4)
    𓋁.𓁉𓂋, 𓋁.𓊚𓂋 = [(0, 0)], [0]             # 🐭 far → 🚫 🎯 mid-🧪
    𓋁.𓇬, 𓋁.𓆛, 𓋁.𓊮 = (0, 7), (10, 0), (10, 7)
    for 𓅕 in ["➡️", "⬅️"] * 6:                 # A↔️B ×6 → period-2 🔁 ⏳ 🚧
        𓋁.𓂷(𓅕)
    assert 𓋁.𓋗() is True and 𓋁.𓋚 >= 𓅓.𓊄𓋚   # 🔁 streak ⬆️ → 🧱 armed
    𓋁.𓂷("⬇️")                                 # 🆕 📍 → cycle ✂️
    assert 𓋁.𓋗() is False and 𓋁.𓋚 == 0       # 🔁 streak 🔄 reset ‼️


def 𓊪𓋘():
    # 🧱  📜 memory break  (#27 🌙7️⃣) :  🧱 persistent → 🐈 🚫 re-🐾 📜 , drift 🆓
    #
    # 🏠 : 🐈(5,4) 🐭(5,0) ⬆️ → 🎯 chase 🀄 = ⬆️  ;  🚫🐕 🚫🧊 → 🚫 flee 🚫 gamble
    def 𓋅():
        𓋆 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False, 𓅱𓁋=False, 𓎛𓁋=False)
        𓋆.𓃠 = (5, 4)
        𓋆.𓁉𓂋, 𓋆.𓊚𓂋 = [(5, 0)], [0]
        𓋆.𓇬, 𓋆.𓆛, 𓋆.𓊮 = (0, 7), (10, 0), (10, 7)
        return 𓋆
    assert 𓅓.𓊄(𓋅()) == "⬆️"                   # 🏁 base 🐾 : 🎯 chase 🐭
    # 🧱 armed + 📜 = ⬆️ tile 🆕 visited  →  🚫 re-🐾 → ⊥ 🀄  (📜 recency 🥇)
    𓋂 = 𓋅()
    𓋂.𓋚 = 𓅓.𓊄𓋚
    for 𓅘 in [(5, 4), (5, 3)] * 4:             # A↔️B 📜  (B = ⬆️ tile)
        𓋂.𓋗𓂋.append(𓅘)
    assert 𓅓.𓊄(𓋂) != "⬆️"                    # 🧱 → 🐈 drift ⊥ , 🧱 ✂️ ‼️
    # 🚫 armed (𓋚 < 🚧) → 📜 🙈 → 🎯 chase 🀄 back  (transient 🌀 → 🚫 divert)
    𓋃 = 𓋅()
    𓋃.𓋚 = 𓅓.𓊄𓋚 - 1
    for 𓅘 in [(5, 4), (5, 3)] * 4:
        𓋃.𓋗𓂋.append(𓅘)
    assert 𓅓.𓊄(𓋃) == "⬆️"                    # 🚫 armed → 🏁 base 🐾 ‼️


def 𓊪𓋤():
    # 🌟🚀  tile :  ⚑ opt-in  ·  🐈🚀😋 → 💨 ×𓋧 , respawn 🎲  (🚫🏆 , 🚫🔥 : 🛠️ tool)
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋦𓁋=False)
    assert 𓋁.𓋤 is None and 𓋁.𓋥 == 0        # 🚫⚑ → 🚫🚀  (🏁 base 🚫 regress ‼️)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋦𓁋=True)
    assert 𓋂.𓋤 is not None                    # ⚑ → 🚀 🗺️
    assert 𓋂.𓋤 not in (𓋂.𓃠, 𓋂.𓇬, 𓋂.𓆛, 𓋂.𓊮, 𓋂.𓅱, 𓋂.𓃥, 𓋂.𓋔)
    assert 𓋂.𓋤 not in 𓋂.𓁉𓂋                # 🚫 stack ∀🀄
    # 😋 → 💨 ×𓋧 , respawn ≠ 📍 old  ,  🚫🏆 🚫🔥
    𓋂.𓃠, 𓋂.𓋤 = (5, 4), (5, 3)
    𓋂.𓅱, 𓋂.𓃥 = None, None
    𓋂.𓁉𓂋, 𓋂.𓊚𓂋 = [(0, 0)], [0]
    𓋂.𓇬, 𓋂.𓆛, 𓋂.𓊮 = (0, 7), (10, 0), (10, 7)
    𓋃, 𓋄 = 𓋂.𓋻, 𓋂.𓋼                     # 🔥 , 🏆 combo before
    𓋂.𓂷("⬆️")
    assert 𓋂.𓋥 == 𓋂.𓋧                     # 💨 ×3 armed ‼️  (🚫 instant spend)
    assert 𓋂.𓃠 == (5, 3)                    # 🚀😋 @ 📍1️⃣ → 🚫 leap ⏳ this 🐾
    assert 𓋂.𓋤 != (5, 3)                    # 🎲 respawn
    assert 𓋂.𓋻 == 𓋃 and 𓋂.𓋼 == 𓋄       # 🛠️ tool → 🚫🔥 , 🚫🏆
    # 🚀🚀 stack → +𓋧 ×2  (⏭️ 🐾 → leap −1)
    𓋂.𓃠, 𓋂.𓋤, 𓋂.𓋥 = (5, 4), (5, 3), 0
    𓋂.𓂷("⬆️")
    assert 𓋂.𓋥 == 𓋂.𓋧
    𓋂.𓃠, 𓋂.𓋤 = (5, 4), (5, 3)
    𓋂.𓂷("⬆️")                               # 💨 armed → leap 2️⃣ + 🚀😋 @ 📍1️⃣
    assert 𓋂.𓋥 == 2 * 𓋂.𓋧 - 1             # +3 stack , −1 leap ‼️


def 𓊪𓋪():
    # 🌟🚀  dash leap :  𓋥>0 + 🧭 → 🐈 2️⃣ cells / 🐾 , −1 💨  ·  🚧 🧱 · 🐕 · 🕳️
    def 𓋅(𓋥=1, 𓃥=None, 𓊵=()):
        𓋆 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓅱𓁋=False, 𓎛𓁋=False, 𓋔𓁋=False)
        𓋆.𓃠, 𓋆.𓋥, 𓋆.𓃥 = (5, 4), 𓋥, 𓃥
        𓋆.𓁉𓂋, 𓋆.𓊚𓂋 = [(0, 0)], [0]
        𓋆.𓇬, 𓋆.𓆛, 𓋆.𓊮 = (0, 7), (10, 0), (10, 7)
        𓋆.𓊵 = set(𓊵)
        return 𓋆
    # 💨 0️⃣ → 🐾 1️⃣ cell  (🏁 base)
    𓋁 = 𓋅(𓋥=0)
    𓋁.𓂷("⬆️")
    assert 𓋁.𓃠 == (5, 3) and 𓋁.𓋥 == 0
    # 💨 >0 → leap 2️⃣ cells , −1 💨
    𓋂 = 𓋅(𓋥=2)
    𓋂.𓂷("⬆️")
    assert 𓋂.𓃠 == (5, 2) and 𓋂.𓋥 == 1     # 2️⃣🐾 ‼️
    # 🐾 stay → 🚫 leap , 🚫 consume
    𓋂.𓂷("🐾")
    assert 𓋂.𓃠 == (5, 2) and 𓋂.𓋥 == 1
    # 🧶 throw → 🚫 leap , 🚫 consume  (🐾 stay 🀄)
    𓋂.𓂷("🧶")
    assert 𓋂.𓃠 == (5, 2) and 𓋂.𓋥 == 1
    # 🧱 @ 📍2️⃣ → 1️⃣ cell 只 , 🚫 consume  (📏 value-gated)
    𓋃 = 𓋅(𓋥=1, 𓊵=((5, 2),))
    𓋃.𓂷("⬆️")
    assert 𓋃.𓃠 == (5, 3) and 𓋃.𓋥 == 1     # 💨 kept ‼️
    # 🧱edge @ 📍2️⃣ → 1️⃣ cell 只 , 🚫 consume
    𓋄 = 𓋅(𓋥=1)
    𓋄.𓃠 = (5, 1)
    𓋄.𓂷("⬆️")
    assert 𓋄.𓃠 == (5, 0) and 𓋄.𓋥 == 1
    # 🐕 @ 📍2️⃣ → stay 📍1️⃣ , 🚫 consume  (🚫 self-😿)
    𓋅𓏤 = 𓋅(𓋥=1, 𓃥=(5, 2))
    𓋅𓏤.𓃥𓎿 = 99                             # 🐕 🚫🐾 ⏳ 🧪
    𓋅𓏤.𓂷("⬆️")
    assert 𓋅𓏤.𓃠 == (5, 3) and 𓋅𓏤.𓋥 == 1 and 𓋅𓏤.𓊟 == 0
    # 🎯 @ 📍1️⃣ mid-leap → 😻  (🚫 🙈 fly-over ‼️)
    𓋆 = 𓋅(𓋥=1)
    𓋆.𓁉𓂋, 𓋆.𓊚𓂋 = [(5, 3)], [0]
    assert 𓋆.𓂷("⬆️") is True and 𓋆.𓄊 is True
    assert 𓋆.𓃠 == (5, 3)                     # 🎯 @ 📍1️⃣ → 🎮🔚 , 🚫 leap on
    # 🎯 @ 📍2️⃣ → 😻
    𓋇 = 𓋅(𓋥=1)
    𓋇.𓁉𓂋, 𓋇.𓊚𓂋 = [(5, 2)], [0]
    assert 𓋇.𓂷("⬆️") is True and 𓋇.𓃠 == (5, 2)
    # 🕳️🌀 : 📍1️⃣ = portal → 🐈 twin , sub-step 2️⃣ 🐾 from twin
    𓋈 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓅱𓁋=False, 𓃥𓁋=False, 𓋔𓁋=False)
    𓋈.𓎛 = ((5, 3), (1, 6))
    𓋈.𓃠, 𓋈.𓋥 = (5, 4), 1
    𓋈.𓁉𓂋, 𓋈.𓊚𓂋 = [(9, 0)], [0]
    𓋈.𓇬, 𓋈.𓆛, 𓋈.𓊮 = (0, 7), (10, 0), (10, 7)
    𓋈.𓂷("⬆️")
    assert 𓋈.𓃠 == (1, 5) and 𓋈.𓋥 == 0     # 🕳️ twin (1,6) → ⬆️ → (1,5) ‼️
    # 📜 : 1️⃣ entry / 🐾  (leap → 🔚 📍 只)
    𓋉 = 𓋅(𓋥=1)
    𓋉.𓋗𓂋.clear()
    𓋉.𓂷("⬆️")
    assert list(𓋉.𓋗𓂋) == [(5, 2)]


def 𓊪𓋤𓁐():
    # 🌟🚀  🖼️ :  🗺️ 🚀 tile  ·  HUD 🚀×N ⇔ 💨 > 0  ·  🌈 🟨
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋦𓁋=True)
    assert "🚀" in 𓋁.𓁐()                     # 🗺️ 🚀 drawn
    assert "🚀×" not in 𓋁.𓁑()                # 💨 0️⃣ → 🙈 HUD
    𓋁.𓋥 = 3
    assert "🚀×3" in 𓋁.𓁑()                   # 💨 → HUD ‼️
    assert "🚀×3" in 𓋁.𓁑() and "❄️" not in 𓋁.𓁑()   # ⚔️ ❄️ , 🚫 collide
    assert "\033[93m🚀" in 𓅓.𓋊(𓋁.𓁐(), True)  # 🌈 🟨
    # 🚫⚑ → 🚫 🚀 🗺️
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert "🚀" not in 𓋂.𓁐() and "🚀×" not in 𓋂.𓁑()


def 𓊪𓋦𓊆():
    # 🌟🚀  🌊 gate :  ⚑ + 🌊≥3 → 🚀  ;  🌊<3 → 🚫  ;  🚫⚑ → 🚫 ∀🌊  (🚫 regress)
    assert 𓅓.𓊆(3, random.Random(0), False, True).𓋤 is not None
    assert 𓅓.𓊆(2, random.Random(0), False, True).𓋤 is None      # 🌊<3 → 🚫🚀
    assert 𓅓.𓊆(9, random.Random(0), False, True).𓋤 is not None
    for 𓊍 in range(1, 10):                    # 🚫⚑ → 🚫🚀 ∀🌊  (🏁 base ‼️)
        assert 𓅓.𓊆(𓊍, random.Random(0)).𓋤 is None


def 𓊪𓋦𓆲():
    # 🌟🚀  🔗✅ :  🤖🎬 ×120🎲 @ 🌊3/9 , ⚑🚀 on  →  🚫💥 , 💨 fires
    𓋁 = 0
    for 𓊃𓏤 in range(120):
        for 𓊍 in (3, 9):
            𓋂 = 𓅓.𓊆(𓊍, random.Random(𓊃𓏤), False, True)
            for _ in range(300):
                if 𓋂.𓂷(𓅓.𓊄(𓋂)):
                    break
            𓋁 += 𓋂.𓋥
            assert 𓋂.𓋤 is None or 𓋂.𓋤 not in 𓋂.𓊵   # 🚀 🚫 in 🧱
    assert 𓋁 > 0                              # 💨 grabbed ≥1 ⏳ 240🎮


def 𓊪𓋔𓊄():
    # 🌟🧊  🐈🧠 :  💨 flee + 🧊 📏🤏 → 🏃🧊  ;  🚧 guard (🐕 🥇 → 🚫) ; 🧱 → relax
    #
    # 🏠 : 🐈(5,4) 🐕(7,4) 📏2 → 💨 flee (❤️≤3) · 🐭(0,4) ⬅️ side · 🧊(5,7) ⬇️ side
    #      → 💨 flee 🀄 = ⬅️ (max 📏🐕 , tie min 📏🐭)  ⊥  🏃🧊 = ⬇️   → discriminating ‼️
    def 𓋅(𓋔=(5, 7), 𓃥=(7, 4), 𓋹=3):
        𓋆 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓅱𓁋=False, 𓎛𓁋=False)
        𓋆.𓋹, 𓋆.𓋯 = 𓋹, True                 # ❤️≤3 → 💨 flee ; 🧶 spent → 🚫🎾
        𓋆.𓃠, 𓋆.𓃥, 𓋆.𓋔 = (5, 4), 𓃥, 𓋔
        𓋆.𓁉𓂋, 𓋆.𓊚𓂋 = [(0, 4)], [0]
        𓋆.𓇬, 𓋆.𓆛, 𓋆.𓊮 = (0, 0), (0, 7), (10, 0)
        return 𓋆
    # 🚫🧊 → 💨 flee 🀄 = ⬅️  (🏁 base 🐾)
    assert 𓅓.𓊄(𓋅(𓋔=None)) == "⬅️"
    # 🧊 ⬇️ : 📏🧊(🐈)=3 , 📏🧊(🐕)=5 → 3+1 < 5 ✅ → 🏃🧊
    𓋁 = 𓋅()
    assert 𓋁.𓃰(𓋁.𓋔).get(𓋁.𓃠) == 3 and 𓋁.𓃰(𓋁.𓋔).get(𓋁.𓃥) == 5
    assert 𓅓.𓊄(𓋁) == "⬇️"                     # 🏃🧊 ‼️  (⚔️ 💨 flee ⬅️)
    # 🚧 guard : 🐕 📏🤏🧊 → 🚫 🏃🧊  (🚫😿💀)
    𓋂 = 𓋅(𓃥=(5, 6))                           # 📏🧊(🐕)=1 → 3+1 < 1 ✗
    assert 𓅓.𓊄(𓋂) != "⬇️"                     # 💨 flee 🀄 , 🚫 🏃🧊 → 🐕
    # 🧱 stalemate (📜 2-cycle) → 🚧 relax → 🏃🧊 gamble
    for 𓅘 in [(5, 4), (4, 4), (5, 4), (4, 4)]:
        𓋂.𓋗𓂋.append(𓅘)
    assert 𓋂.𓋗() is True
    assert 𓅓.𓊄(𓋂) == "⬇️"                     # 🧱 → gamble 🏃🧊 ‼️
    # 🚧 🔚 ❤️ : ❤️ ≤ 𓊄𓋹𓈎 → 🚫 gamble  (🚫💀)
    𓋂.𓋹 = 𓅓.𓊄𓋹𓈎
    assert 𓅓.𓊄(𓋂) != "⬇️"
    # ❄️ already on → 🚫 🏃🧊  (🚫 waste)
    𓋃 = 𓋅()
    𓋃.𓋕 = 4
    assert 𓅓.𓊄(𓋃) == "⬅️"                     # ❄️ on → 💨 flee 🀄
    # ❤️ ⬆️ → 🚫 flee mode → 🚫 🏃🧊  (🎯🐭 🀄)
    assert 𓅓.𓊄(𓋅(𓋹=9)) != "⬇️"


def 𓊪𓋔𓁐():
    # 🌟🧊  🖼️ :  🗺️ 🧊 tile  ·  HUD ❄️×N ⇔ frozen  ·  🌈 cyan
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    assert "🧊" in 𓋁.𓁐()                       # 🗺️ 🧊 drawn
    assert "❄️" not in 𓋁.𓁑()                   # 🚫❄️ → 🙈 HUD
    𓋁.𓋕 = 3
    assert "❄️×3" in 𓋁.𓁑()                     # ❄️ on → HUD
    𓋁.𓋕 = 0
    assert "❄️" not in 𓋁.𓁑()                   # thaw → 🙈
    # 🚫🧊 → 🚫 🗺️  (🚫🐕 🏠)
    assert "🧊" not in 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓃥𓁋=False).𓁐()
    # 🌈 : 🧊 + ❄️ → cyan wrap
    assert "\033[96m🧊" in 𓅓.𓋊(𓋁.𓁐(), True)
    𓋁.𓋕 = 2
    assert "\033[96m❄️" in 𓅓.𓋊(𓋁.𓁑(), True)
    assert 𓅓.𓋊(𓋁.𓁐(), False) == 𓋁.𓁐()        # 🚫⚑ → 📺 ↔️


def 𓊪𓎏():
    # ⌨️  🐾 reader :  ⎋[A⎋[B⎋[C⎋[D → 🔼🔽▶️◀️  (#23 🐛)  ; 🀄 ↔️ ; 🚫💥
    assert 𓅓.𓎏("\x1b[A") == ["⬆️"]
    assert 𓅓.𓎏("\x1b[B") == ["⬇️"]
    assert 𓅓.𓎏("\x1b[C") == ["➡️"]              # 🙏 #23 : ^[[C 🟰 ➡️
    assert 𓅓.𓎏("\x1b[D") == ["⬅️"]
    # ⎋O𓅕  app-cursor mode  (📺 🔀)
    assert 𓅓.𓎏("\x1bOA") == ["⬆️"]
    assert 𓅓.𓎏("\x1bOD") == ["⬅️"]
    # `^[` 📺 echo 🔤  (🧑📋 paste)
    assert 𓅓.𓎏("^[[C") == ["➡️"]
    assert 𓅓.𓎏("^[[A") == ["⬆️"]
    # ⌨️⌨️ hold → 🐾🐾  (∀ seq in 📜 , 🧭 order kept)
    assert 𓅓.𓎏("\x1b[C\x1b[C\x1b[B") == ["➡️", "➡️", "⬇️"]
    # 🀄 ↔️ passthrough  (🚫⎋ → 🔤 as-is)
    assert 𓅓.𓎏("⬆️") == ["⬆️"]
    assert 𓅓.𓎏(" 🐾 ") == ["🐾"]
    assert 𓅓.𓎏("🧶") == ["🧶"]
    assert 𓅓.𓎏("🙀") == ["🙀"]
    assert 𓅓.𓎏("q") == ["q"]
    # 🕳️ / 🤔❓
    assert 𓅓.𓎏("") == []
    assert 𓅓.𓎏("   ") == []
    assert 𓅓.𓎏("\x1b") == []                   # solo ⎋ → 🚫🧭
    assert 𓅓.𓎏("\x1b[Z") == []                 # ⇧⇥ → 🚫🧭  (🚫💥)
    assert 𓅓.𓎏("🐕") == ["🐕"]                  # 🚫🧭 🔤 → 🤔❓ @ 🕹️
    # ⎋ noise 🚮 + 🧭 kept  (🐈🚧 partial seq)
    assert 𓅓.𓎏("\x1b[\x1b[C") == ["➡️"]
    # 🀄 ⚔️ ⎋ 🤝 : ⎋ present → 🀄 token 🚫 dropped ‼️  (🙀 🚪 must 💨)
    assert 𓅓.𓎏("\x1b[C🙀") == ["➡️", "🙀"]      # ▶️ then 🚪
    assert 𓅓.𓎏("\x1b[C🧶") == ["➡️", "🧶"]      # ▶️ then 🎾
    assert 𓅓.𓎏("🧶\x1b[C") == ["🧶", "➡️"]      # 🀄 🥇 then 🧭
    assert 𓅓.𓎏("\x1b[C 🐾 ") == ["➡️", "🐾"]    # 🚿 strip
    assert 𓅓.𓎏("\x1b[1;5C") == []              # ⌃➡️ params → 🚫🧭 (🚫💥)
    assert 𓅓.𓎏("\x1b[C\x1b[1;5C\x1b[B") == ["➡️", "⬇️"]   # 🚮 mid , 🧭 kept
    # 🕹️ 🔗 : ∀ 🧭 → 𓂃 ✅  (🐾 map 🤝)
    for 𓅕 in ("\x1b[A", "\x1b[B", "\x1b[C", "\x1b[D"):
        assert 𓅓.𓎏(𓅕)[0] in 𓅓.𓂃


def 𓊪𓎏𓊪𓏰():
    # 🕹️  ⌨️ → 🐈🐾 e2e  (📥 ⎋[C → 🐈 ▶️ ; 🐾🐾 hold ; 🙀 → 🚪)
    𓂺 = subprocess.run(
        [sys.executable, "𓃠𓐍𓅓.py", "1"],
        input="\x1b[C\n\x1b[C\n\x1b[B\n🙀\n",
        capture_output=True, text=True, timeout=60,
    )
    assert 𓂺.returncode == 0
    assert "🤔❓" not in 𓂺.stdout                # ⌨️ 🚫 😿  (🙏 #23)
    assert "⏱️=3" in 𓂺.stdout                   # 🐾×3  (🧱🎲 → 📍 ⚖️ , ⏱️ ✅)
    assert "👋😼" in 𓂺.stdout                   # 🙀 🚪
    # ⌨️⌨️ hold : 1 📜 → 🐾🐾🐾
    𓂭 = subprocess.run(
        [sys.executable, "𓃠𓐍𓅓.py", "1"],
        input="\x1b[C\x1b[C\x1b[C\n🙀\n",
        capture_output=True, text=True, timeout=60,
    )
    assert 𓂭.returncode == 0
    assert "🤔❓" not in 𓂭.stdout
    assert "⏱️=3" in 𓂭.stdout                   # ▶️×3 in 1 📜
    # ⌨️ 🤝 🀄 : ⎋[C + 🙀 1️⃣ 📜 → ▶️ then 🚪  (🐛 : 🙀 💨 dropped)
    𓂯 = subprocess.run(
        [sys.executable, "𓃠𓐍𓅓.py", "1"],
        input="\x1b[C🙀\n", capture_output=True, text=True, timeout=60,
    )
    assert 𓂯.returncode == 0
    assert "👋😼" in 𓂯.stdout                   # 🚪 ✅  (🚫 🙈)
    assert "🤔❓" not in 𓂯.stdout
    # 🤔❓ 🚫🧭 🔤  (🚫💥)
    𓂮 = subprocess.run(
        [sys.executable, "𓃠𓐍𓅓.py", "1"],
        input="🐕\n🙀\n", capture_output=True, text=True, timeout=60,
    )
    assert 𓂮.returncode == 0
    assert "🤔❓" in 𓂮.stdout and "👋😼" in 𓂮.stdout


def 𓊪𓊆𓂺():
    # 🏁  parse 🌊 level from args  (digits + keycap emoji)
    assert 𓅓.𓊆𓂺([]) == 1
    assert 𓅓.𓊆𓂺(["🤖", "5"]) == 5
    assert 𓅓.𓊆𓂺(["3️⃣"]) == 3
    assert 𓅓.𓊆𓂺(["🤖", "99"]) == 9       # 🚧 clamp
    assert 𓅓.𓊆𓂺(["🤖", "0"]) == 1        # 🚧 clamp
    assert 𓅓.𓊆𓂺(["🤖", "🐾"]) == 1       # 🚫digit → default


def 𓊪𓎎():
    # 📇  🎮 → 📜 record  (🏆⏱️🐟🥛🐦😿)
    𓋁 = 𓅓.𓉔(random.Random(0))
    𓋁.𓏰 = 12
    𓋁.𓊛 = 3
    𓋁.𓊳 = 1
    𓋁.𓅮 = 2
    𓋁.𓊟 = 1
    𓆳 = 𓅓.𓎎(𓋁)
    assert 𓆳["🏆"] == 𓋁.𓊙()
    assert 𓆳["⏱️"] == 12
    assert 𓆳["🐟"] == 3
    assert 𓆳["🥛"] == 1
    assert 𓆳["🐦"] == 2
    assert 𓆳["😿"] == 1


def 𓊪𓆓():
    # 🪝😾  🗣️🔤👀 → 📜 ↔️ + 🏷️   (🚫🎭📜)
    assert 𓆦.𓁐("meow mrrr prrr hisss nya") == "meow mrrr prrr hisss nya"
    assert 𓆦.𓁐("Meow… purr! grrr nyan mew miaou") == "Meow… purr! grrr nyan mew miaou"
    assert 𓆦.𓁐("😻🎉🐾 prrr~ 𓃠 → ✅ ⚡ 42") == "😻🎉🐾 prrr~ 𓃠 → ✅ ⚡ 42"
    assert 𓆦.𓁐("") == ""
    # 🗣️👀 → 📜 ↔️ + 🏷️ 📄🔚   (4🗣️ → ⬆️⬆️)
    assert 𓆦.𓁐("Here is the plan:\n") == "Here is the plan:  😾😾hisssss!!\n"
    # 🔗 ✅ 🚫💥
    assert 𓆦.𓁐("📚 https://code.claude.com/docs/en/hooks") == "📚 https://code.claude.com/docs/en/hooks"
    # ⌨️ `…` ✅
    assert 𓆦.𓁐("`displayContent` 📤 ✅") == "`displayContent` 📤 ✅"
    # 📁 ✅
    assert 𓆦.𓁐(".claude/𓆓𓁐.py 🐾") == ".claude/𓆓𓁐.py 🐾"
    # 📄📄📄 → 1️⃣🏷️
    𓆼 = 𓆦.𓁐("🐈 meow\nSTOP the cat\nprrr~ 𓃠\n")
    assert 𓆼 == "🐈 meow\nSTOP the cat  😾😾hisssss!!\nprrr~ 𓃠\n"
    assert 𓆦.𓁐("café ☕") == "café ☕  😾hisss!"          # À-ž 👀
    assert 𓆦.𓁐("his mr pur hi") == "his mr pur hi  😾😾hisssss!!"   # 🎭🐈 🚫


def 𓊪𓆓𓅂():
    # 😾 ⬆️⬆️⬆️ → 📢   (🗣️🔢 → 🔊🪜)
    assert 𓆦.𓅱(1) == "  😾hisss!"
    assert 𓆦.𓅱(2) == "  😾hisss!"
    assert 𓆦.𓅱(3) == "  😾😾hisssss!!"
    assert 𓆦.𓅱(5) == "  😾😾hisssss!!"
    assert 𓆦.𓅱(6) == "  📢😾😾😾HISSSSSS‼️"
    assert 𓆦.𓅱(42) == "  📢😾😾😾HISSSSSS‼️"
    # ⬆️  1-2 🗣️
    assert 𓆦.𓁐("cat 🐾") == "cat 🐾  😾hisss!"
    # ⬆️⬆️  3-5 🗣️
    assert 𓆦.𓁐("the cat sat 🐾") == "the cat sat 🐾  😾😾hisssss!!"
    # ⬆️⬆️⬆️ 📢  ≥6 🗣️
    𓆼 = 𓆦.𓁐("the quick brown fox jumps over dogs")
    assert 𓆼 == "the quick brown fox jumps over dogs  📢😾😾😾HISSSSSS‼️"
    # 🐈✅ 🚫🔢 : meow prrr 🚫➕
    assert 𓆦.𓁐("meow prrr the cat sat nya 🐾") == "meow prrr the cat sat nya 🐾  😾😾hisssss!!"


def 𓊪𓆓𓂭():
    # 🪝 ⛓️  📥 stdin json → 📤 displayContent
    𓂺 = json.dumps({
        "hook_event_name": "MessageDisplay",
        "turn_id": "𓏤",
        "message_id": "𓏥",
        "index": 0,
        "final": True,
        "delta": "Let me meow, nya!\n🐈 prrr~\n",
    })
    𓊾 = subprocess.run(
        [sys.executable, ".claude/𓆓𓁐.py"],
        input=𓂺, capture_output=True, text=True, timeout=30,
    )
    assert 𓊾.returncode == 0
    𓂭 = json.loads(𓊾.stdout)["hookSpecificOutput"]
    assert 𓂭["hookEventName"] == "MessageDisplay"
    assert 𓂭["displayContent"] == "Let me meow, nya!  😾hisss!\n🐈 prrr~\n"
    # 🙀 📥💔 → 🤫 (📺 🅾️)
    𓊿 = subprocess.run(
        [sys.executable, ".claude/𓆓𓁐.py"],
        input="🙀🚫json", capture_output=True, text=True, timeout=30,
    )
    assert 𓊿.returncode == 0
    assert 𓊿.stdout == ""


def 𓊪𓆓𓉗():
    # 🪝🈲  🇨🇳🇭🇰🇵🇱🇲🇻🇳🇴🇺🇬 → 🙊❌ ‼️‼️   (absolute — `⌨️`🔗📁 🚫🙈 ; 📜 🙊📜.md)
    assert 𓆦.𓁐("\u4f60\u597d 🐈") == "🙊🙊 🐈  🙊❌😾😾‼️‼️"
    assert 𓆦.𓁐("\u0142apa") == "🙊apa  🙊❌😾😾‼️‼️"
    assert 𓆦.𓁐("sm\u00f8rrebr\u00f8d") == "sm🙊rrebr🙊d  🙊❌😾😾‼️‼️"
    assert 𓆦.𓁐("\u078b\u07a8\u0788\u07ac\u0780\u07a8") == "🙊🙊🙊🙊🙊🙊  🙊❌😾😾‼️‼️"
    assert 𓆦.𓁐("e\u014bkima") == "e🙊kima  🙊❌😾😾‼️‼️"
    # `⌨️` 🚫🙈 — 🈲 absolute ‼️  (⚔️ 😾🪜 🙈)
    assert 𓆦.𓁐("`\u4e2d`") == "`🙊`  🙊❌😾😾‼️‼️"
    # 📄📄 mix : 🈲📄 → 🙊 , 🐈📄 ↔️
    assert 𓆦.𓁐("meow 🐾\n\u732b\n") == "meow 🐾\n🙊  🙊❌😾😾‼️‼️\n"
    # 🐈✅ + 𓂀 + 😺 + \u00e9 ↔️  (🚫🈲 → 😾🪜 🀄)
    assert 𓆦.𓁐("prrr~ 𓃠 😺 caf\u00e9 ☕") == "prrr~ 𓃠 😺 caf\u00e9 ☕  😾hisss!"


def 𓊪𓆓𓉗𓂭():
    # 🪝 ⛓️  🈲 📥 stdin → 🙊 📤
    𓂺 = json.dumps({"delta": "\u4e2d\u6587 nya\n🐈 prrr~\n"})
    𓊾 = subprocess.run(
        [sys.executable, ".claude/𓆓𓁐.py"],
        input=𓂺, capture_output=True, text=True, timeout=30,
    )
    assert 𓊾.returncode == 0
    𓂭 = json.loads(𓊾.stdout)["hookSpecificOutput"]
    assert 𓂭["displayContent"] == "🙊🙊 nya  🙊❌😾😾‼️‼️\n🐈 prrr~\n"


𓐩 = [𓊪𓎘, 𓊪𓐍, 𓊪𓎉, 𓊪𓎗, 𓊪𓊵, 𓊪𓎘𓁉, 𓊪𓂷, 𓊪𓇬, 𓊪𓆛, 𓊪𓊙, 𓊪𓄊, 𓊪𓁐, 𓊪𓋴, 𓊪𓊮, 𓊪𓊰,
     𓊪𓃥, 𓊪𓃥𓎗, 𓊪𓊟, 𓊪𓃥𓎿, 𓊪𓁋,
     𓊪𓅱, 𓊪𓅱𓎗, 𓊪𓅱𓎗𓊵, 𓊪𓅲, 𓊪𓅱𓁋,
     𓊪𓎛, 𓊪𓎛𓁋,
     𓊪𓋔, 𓊪𓋕, 𓊪𓋗, 𓊪𓋚, 𓊪𓋘, 𓊪𓋔𓊄, 𓊪𓋔𓁐,
     𓊪𓋤, 𓊪𓋪, 𓊪𓋤𓁐, 𓊪𓋦𓊆, 𓊪𓋦𓆲,
     𓊪𓋭, 𓊪𓋮, 𓊪𓋯, 𓊪𓋰,
     𓊪𓋹, 𓊪𓋻,
     𓊪𓁉𓂋, 𓊪𓁏, 𓊪𓁉𓎗, 𓊪𓁉𓎗𓆊, 𓊪𓁉𓊆, 𓊪𓁉𓊰, 𓊪𓊄𓁉,
     𓊪𓋃𓁋, 𓊪𓋃𓈖, 𓊪𓋂, 𓊪𓋂𓊙, 𓊪𓋃𓁑, 𓊪𓋺𓁐, 𓊪𓎋𓉏, 𓊪𓋃𓂺,
     𓊪𓋊, 𓊪𓋋,
     𓊪𓎋, 𓊪𓎌, 𓊪𓎍, 𓊪𓎎,
     𓊪𓎏, 𓊪𓎏𓊪𓏰,
     𓊪𓊆, 𓊪𓊆𓄊, 𓊪𓊆𓂺,
     𓊪𓆓, 𓊪𓆓𓅂, 𓊪𓆓𓂭, 𓊪𓆓𓉗, 𓊪𓆓𓉗𓂭]

if __name__ == "__main__":
    for 𓆑 in 𓐩:
        𓆑()
        print("✅", 𓆑.__name__)
    print("😻🎉  meow!  ", len(𓐩), "✅")
