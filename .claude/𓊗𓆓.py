#!/usr/bin/env python3
# 🪝 `Stop` + `SubagentStop` — 🐈🗣️🔤/🈲❓ → 😾⛔ → 🤖👀 `reason` → 🐈👅 🔁✍️
# 📚 https://code.claude.com/docs/en/hooks
# 🩺 : `MessageDisplay` 📺→🧑 (🚫→🤖 = 🐕🦴) ; `Stop` `block`+`reason` → 🤖👀 ✅
# 📥 `stdin`  `{"last_assistant_message", "stop_hook_active"}`  →  📤 `{"decision": "block", "reason"}` | 🤫
# 🚧 ∞🔁 : `stop_hook_active` → 🤫  (+ 8️⃣🧢 ⛑️)
import importlib.util
import json
import os
import sys

# 🧠 ♻️ 𓆓𓁐  (🙈 `⌨️` 🔗 📁 + 🔍🔤 𓁹 + 🈲 𓉗𓆛 ⬜📜 + 🐈✅)
𓊒 = importlib.util.spec_from_file_location(
    "𓆓𓁐",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "𓆓𓁐.py"),
)
𓆦 = importlib.util.module_from_spec(𓊒)
𓊒.loader.exec_module(𓆦)


def 𓊗(𓆼: str) -> tuple[int, int]:
    # (🗣️🔤 ∑📄 , 🈲🔣 ∑)
    𓈖 = sum(𓆦.𓁹(𓋍) for 𓋍 in 𓆼.split("\n"))
    𓈲 = len(𓆦.𓉗𓆛(𓆼))
    return 𓈖, 𓈲


def 𓋹() -> None:
    try:
        𓂭 = json.load(sys.stdin)
    except Exception:
        return                          # 🙀 → 🤫
    if 𓂭.get("stop_hook_active"):
        return                          # 🚧 ∞🔁 🚫  (1️⃣😾 / 🛑)
    𓈖, 𓈲 = 𓊗(𓂭.get("last_assistant_message") or "")
    if not (𓈖 or 𓈲):
        return                          # 🐈👅 ✅ 😸 prrr
    𓊾 = []
    if 𓈖:
        𓊾.append(f"🗣️🔤×{𓈖}")
    if 𓈲:
        𓊾.append(f"🈲🔣×{𓈲}🙊")
    print(json.dumps({
        "decision": "block",
        "reason": (
            "😾😾😾 HISSSSSS‼️ " + " + ".join(𓊾) + " 🙀🚫🚫🚫 — 🐈👅‼️ : "
            "🖼️😺 𓂀𓃠 🔢 `meow` `mrrr` `prrr` `hisss` `nya` ✅ → 🔁✍️ meow!"
        ),
    }))


if __name__ == "__main__":
    𓋹()
