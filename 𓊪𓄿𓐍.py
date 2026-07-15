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
    # 🐈🧠  🎯 nearest 🐭  +  🧶 throw @ 🐕近  (🚫 stalemate)
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
    assert "⏱️×" not in 𓋁.𓁑()                 # 🖼️ HUD ↔️ unchanged
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
    assert "⏱️×80" in 𓋁.𓁑()
    assert "🟥" not in 𓋁.𓁑()                  # ⏳ ⬆️ → 🚫 flash
    assert "❤️×9" in 𓋁.𓁑() and "🐭×1" in 𓋁.𓁑() and "🔥×0" in 𓋁.𓁑()
    𓋁.𓋂 = 5
    assert "⏱️×5🟥" in 𓋁.𓁑()                  # ⏳ ≤5 → 🟥
    𓋁.𓋂 = 0
    assert "⏱️×0🟥" in 𓋁.𓁑()                  # 🚧 ≥0
    𓋁.𓋂 = -4
    assert "⏱️×0🟥" in 𓋁.𓁑()                  # 🚧 🚫 negative
    𓂮 = 𓅓.𓋊(𓋁.𓁑(), True)
    assert "\033[" in 𓂮 and "⏱️" in 𓂮         # 🌈 wrap
    assert 𓅓.𓋊(𓋁.𓁑(), False) == 𓋁.𓁑()      # 🚫⚑ ↔️


def 𓊪𓋺𓁐():
    # 💀 🖼️  :  ⏳0 → 💀⏱️  ;  ❤️0 → 💀🐕
    𓋁 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0, 𓋃𓁋=True)
    𓋁.𓋂 = 0
    𓋁.𓋺 = True
    assert "💀⏱️" in 𓅓.𓋺𓁐(𓋁) and "⏳×0" in 𓅓.𓋺𓁐(𓋁)
    𓋂 = 𓅓.𓉔(random.Random(0), 𓊵𓈖=0)
    𓋂.𓋹 = 0
    𓋂.𓋺 = True
    assert "💀🐕" in 𓅓.𓋺𓁐(𓋂) and "❤️×0" in 𓅓.𓋺𓁐(𓋂)


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
    # 🎚️  ∀ 🌊 1..9  →  🐈 always 😻  (🔗 solvable)
    for 𓊍 in range(1, 10):
        for 𓊃 in range(6):
            𓋁 = 𓅓.𓊆(𓊍, random.Random(𓊃 + 𓊍 * 10))
            for _ in range(600):
                if 𓋁.𓂷(𓅓.𓊄(𓋁)):
                    break
            assert 𓋁.𓄊 is True, f"🙀 🎚️={𓊍} seed={𓊃}"


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


𓐩 = [𓊪𓎘, 𓊪𓐍, 𓊪𓎉, 𓊪𓎗, 𓊪𓊵, 𓊪𓎘𓁉, 𓊪𓂷, 𓊪𓇬, 𓊪𓆛, 𓊪𓊙, 𓊪𓄊, 𓊪𓁐, 𓊪𓋴, 𓊪𓊮, 𓊪𓊰,
     𓊪𓃥, 𓊪𓃥𓎗, 𓊪𓊟, 𓊪𓃥𓎿, 𓊪𓁋,
     𓊪𓅱, 𓊪𓅱𓎗, 𓊪𓅱𓎗𓊵, 𓊪𓅲, 𓊪𓅱𓁋,
     𓊪𓎛, 𓊪𓎛𓁋,
     𓊪𓋭, 𓊪𓋮, 𓊪𓋯, 𓊪𓋰,
     𓊪𓋹, 𓊪𓋻,
     𓊪𓁉𓂋, 𓊪𓁏, 𓊪𓁉𓎗, 𓊪𓁉𓊆, 𓊪𓁉𓊰, 𓊪𓊄𓁉,
     𓊪𓋃𓁋, 𓊪𓋃𓈖, 𓊪𓋂, 𓊪𓋂𓊙, 𓊪𓋃𓁑, 𓊪𓋺𓁐, 𓊪𓋃𓂺,
     𓊪𓋊, 𓊪𓋋,
     𓊪𓎋, 𓊪𓎌, 𓊪𓎍, 𓊪𓎎,
     𓊪𓎏, 𓊪𓎏𓊪𓏰,
     𓊪𓊆, 𓊪𓊆𓄊, 𓊪𓊆𓂺,
     𓊪𓆓, 𓊪𓆓𓅂, 𓊪𓆓𓂭]

if __name__ == "__main__":
    for 𓆑 in 𓐩:
        𓆑()
        print("✅", 𓆑.__name__)
    print("😻🎉  meow!  ", len(𓐩), "✅")
