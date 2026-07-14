# 🐈✅🐭 — 𓊪𓄿  (tests for 𓃠𓐍𓅓)  ✨  🧱 + 🧭 BFS
import importlib.util as 𓇓
import random

𓊒 = 𓇓.spec_from_file_location("𓅓", "𓃠𓐍𓅓.py")
𓅓 = 𓇓.module_from_spec(𓊒)
𓊒.loader.exec_module(𓅓)


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
    # 🏆  ⚡fast + 🐟 + 🥛
    𓋁 = 𓅓.𓉔(random.Random(0))
    𓋁.𓏰 = 10
    𓋁.𓊛 = 3
    𓋁.𓊳 = 2
    assert 𓋁.𓊙() == 90 + 15 + 6   # (100-10) + 5×3 + 3×2
    𓋁.𓏰 = 250
    assert 𓋁.𓊙() == 0 + 15 + 6    # 🚧 ≥0


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


𓐩 = [𓊪𓎘, 𓊪𓐍, 𓊪𓎗, 𓊪𓊵, 𓊪𓎘𓁉, 𓊪𓂷, 𓊪𓇬, 𓊪𓆛, 𓊪𓊙, 𓊪𓄊, 𓊪𓁐, 𓊪𓋴, 𓊪𓊮, 𓊪𓊰]

if __name__ == "__main__":
    for 𓆑 in 𓐩:
        𓆑()
        print("✅", 𓆑.__name__)
    print("😻🎉  meow!  ", len(𓐩), "✅")
