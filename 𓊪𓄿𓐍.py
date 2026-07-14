# 🐈✅🐭 — 𓊪𓄿  ✨  🧱 + 🧭 BFS + 🪝😾
import importlib.util as 𓇓
import json
import random
import subprocess
import sys

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


def 𓊪𓆓():
    # 🪝😾  🗣️🔤👀 → 📜 ↔️ + 🏷️   (🚫🎭📜)
    assert 𓆦.𓁐("meow mrrr prrr hisss nya") == "meow mrrr prrr hisss nya"
    assert 𓆦.𓁐("Meow… purr! grrr nyan mew miaou") == "Meow… purr! grrr nyan mew miaou"
    assert 𓆦.𓁐("😻🎉🐾 prrr~ 𓃠 → ✅ ⚡ 42") == "😻🎉🐾 prrr~ 𓃠 → ✅ ⚡ 42"
    assert 𓆦.𓁐("") == ""
    # 🗣️👀 → 📜 ↔️ + 🏷️ 📄🔚
    assert 𓆦.𓁐("Here is the plan:\n") == "Here is the plan:  😾hisss!\n"
    # 🔗 ✅ 🚫💥
    assert 𓆦.𓁐("📚 https://code.claude.com/docs/en/hooks") == "📚 https://code.claude.com/docs/en/hooks"
    # ⌨️ `…` ✅
    assert 𓆦.𓁐("`displayContent` 📤 ✅") == "`displayContent` 📤 ✅"
    # 📁 ✅
    assert 𓆦.𓁐(".claude/𓆓𓁐.py 🐾") == ".claude/𓆓𓁐.py 🐾"
    # 📄📄📄 → 1️⃣🏷️
    𓆼 = 𓆦.𓁐("🐈 meow\nSTOP the cat\nprrr~ 𓃠\n")
    assert 𓆼 == "🐈 meow\nSTOP the cat  😾hisss!\nprrr~ 𓃠\n"
    assert 𓆦.𓁐("café ☕") == "café ☕  😾hisss!"          # À-ž 👀
    assert 𓆦.𓁐("his mr pur hi") == "his mr pur hi  😾hisss!"   # 🎭🐈 🚫


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


𓐩 = [𓊪𓎘, 𓊪𓐍, 𓊪𓎗, 𓊪𓊵, 𓊪𓎘𓁉, 𓊪𓂷, 𓊪𓇬, 𓊪𓆛, 𓊪𓊙, 𓊪𓄊, 𓊪𓁐, 𓊪𓋴, 𓊪𓊮, 𓊪𓊰, 𓊪𓆓, 𓊪𓆓𓂭]

if __name__ == "__main__":
    for 𓆑 in 𓐩:
        𓆑()
        print("✅", 𓆑.__name__)
    print("😻🎉  meow!  ", len(𓐩), "✅")
