#!/usr/bin/env python3
# 🪝 `PostToolUse` — 📬 👀 → 📭 ✂️ → 📢😾 `additionalContext` → 🤖👀 ⚡  (⚔️ `Stop` 🕘😿🕳️ ; #91)
# 📚 https://code.claude.com/docs/en/hooks
# 🩺 : `MessageDisplay` (`𓆓𓁐.py`) 🗣️🔤/🈲 👀 → ✍️ 📬 ; 🈁 📭 → 🤖👀 🔧⏭️ ⚡  (🚫 ⏳ 🛑)
# 📥 `stdin`  `{"session_id", "tool_name", …}`  →  📤 `{"hookSpecificOutput": {"hookEventName", "additionalContext"}}` | 🤫
# 🚧 ➿ : 📭 ✂️ = 1️⃣📢 / 📬  (🚫🔁🔁)  ·  👴📬 >1🕐 → 🗑️  (👻 🍂)
import importlib.util
import json
import os
import sys
import time

# ♻️ 𓆓𓁐  (📬 🛤️ 🪞 : `𓊕𓉏` + `𓊕𓊨`)
𓊒 = importlib.util.spec_from_file_location(
    "𓆓𓁐",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "𓆓𓁐.py"),
)
𓆦 = importlib.util.module_from_spec(𓊒)
𓊒.loader.exec_module(𓆦)

𓊕𓏰 = 3600                              # 👴📬 🕐🚧  (>1🕐 → 🗑️)


def 𓊕𓄲(𓊨𓉏: str) -> tuple[int, int]:
    # 📬 📖 → 📭 ✂️ → 🖊️ 🔗↩️ → 🔢 @ ☝️ → (∑🗣️🔤 , ∑🈲🔣)   (∅📬 → 0,0)
    #   🌊✂️🩹 (#92) : 🖊️ 🔗↩️ ⏮️ 🔢 → 🐈🗣️ `meow` 🌊🔪 → 🔗↩️ → 🚫👻😾
    try:
        with open(𓊨𓉏, encoding="utf-8") as 𓊨:
            𓆼 = 𓊨.read()
        os.unlink(𓊨𓉏)                  # 📭 ‼️  (🚧 ➿ : 1️⃣📢 / 📬)
    except Exception:
        return 0, 0
    𓊾 = []
    for 𓋍 in 𓆼.splitlines():
        try:
            𓊾.append(json.loads(𓋍).get("🖊️") or "")
        except Exception:
            continue                    # 💔📄 → ⏭️
    𓋎 = "".join(𓊾)                     # 🔗↩️ 🌊✂️ → 🔢 🎯 (🚫👻)
    𓈖 = sum(𓆦.𓁹(𓊍) for 𓊍 in 𓋎.split("\n"))
    𓈲 = len(𓆦.𓉗𓆛(𓋎))
    return 𓈖, 𓈲


def 𓊕𓋯() -> None:
    # 👴📬 🗑️  (👻 🍂 >1🕐 ; 🙀 → 🤫)
    try:
        𓉏 = 𓆦.𓊕𓉏()
        𓏰 = time.time()
        for 𓅕 in os.listdir(𓉏):
            𓊨 = os.path.join(𓉏, 𓅕)
            if 𓏰 - os.path.getmtime(𓊨) > 𓊕𓏰:
                os.unlink(𓊨)
    except Exception:
        pass


def 𓋹() -> None:
    try:
        𓂭 = json.load(sys.stdin)
    except Exception:
        return                          # 🙀 📥💔 → 🤫
    𓈖, 𓈲 = 𓊕𓄲(𓆦.𓊕𓊨(𓂭))
    𓊕𓋯()
    if not (𓈖 or 𓈲):
        return                          # 📬 ∅ → 🤫 prrr
    𓊾 = []
    if 𓈖:
        𓊾.append(f"🗣️🔤×{𓈖}")
    if 𓈲:
        𓊾.append(f"🈲🔣×{𓈲}🙊")
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": (
                𓆦.𓅱(𓈖 + 𓈲).strip() + " " + " + ".join(𓊾) + " 🙀🚫🚫🚫 — 🐈👅‼️ : "
                "🖼️😺 𓂀𓃠 🔢 `meow` `mrrr` `prrr` `hisss` `nya` ✅ → ⚡🔁✍️ meow!"
            ),
        }
    }))


if __name__ == "__main__":
    𓋹()
