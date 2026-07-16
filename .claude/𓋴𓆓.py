#!/usr/bin/env python3
# 🪝 `PreToolUse` — 🐈 🏷️📓 : 📵 (🚫⛔ , 🚫🔓)
#   🏷️ : 🙋 · 💀 🩸🔫 · 🤖 🀫
#   🐈📜 : 🙋 (`AskUserQuestion`) → `ask` (→ 👤 🛡️) ;
#          💀🩸🐚 (`rm -rf` · `--force` · `reset --hard` · `git clean` · `DROP` · `dd` · `mkfs` · `>`)
#            → 📓 `stderr` 🔊 + `exit` 0️⃣  (📵 , 🚫⛔) ;
#          🤖 🀫 (+ 🐙 `mcp__github*` 🏛️👑) → 🤐 `exit` 0️⃣ → 🛡️ 🀄🌊 .
#          🚫🔓 : 🪝 🚫 🤖`allow` ‼️
# 📚 https://code.claude.com/docs/en/hooks
# 📥 `stdin`  `{"tool_name","tool_input","hook_event_name":"PreToolUse"}`
# 📤 🙋 → `stdout` `{"hookSpecificOutput":{…,"permissionDecision":"ask",…}}` · 💀 → `stderr` 📓 · 🤖 → 🤐
# 🚧 📥💔 (🚫 `json` / 🈳) → 🤐 `exit` 0️⃣  (🚫⛔ , 🚫🙀)
import json
import re
import sys

# 💀🩸  `Bash` 🀄 → 🩸 `re`  (`rm -rf` · `--force` · `--hard` · `git clean` · `DROP` · `dd` · `mkfs` · `>`)
𓋴𓋆 = re.compile(
    r"rm\s+-\w*[rf]|--force|--hard|git\s+clean|\bDROP\b|\bTRUNCATE\b|"
    r"\bmkfs\b|\bdd\s|chmod\s+-R|:\s*>|[^>|]>[^>|]"
)

𓋴𓁋 = ("AskUserQuestion",)            # 🙋 → `ask` (→ 👤)
# 💀  🩸🔫 🔧📛  (🚫🐙 — 🐙🐱 🏛️👑 🀄)
𓋴𓁏 = ("TaskStop", "CronDelete")


def 𓋴(𓆼: str, 𓂭: dict) -> str:
    # 🏷️ : 🙋 | 💀 🩸🔫 | 🤖 🀫  ( 🐙 `mcp__github*` → 🤖 )
    if 𓆼 in 𓋴𓁋:
        return "🙋"
    if 𓆼.startswith("mcp__github"):
        return "🤖"                      # 🐙🐱 🏛️👑 → 📵
    if any(𓄿 in 𓆼 for 𓄿 in 𓋴𓁏):
        return "💀"
    if 𓆼 == "Bash":
        𓊾 = (𓂭 or {}).get("command", "") or ""
        return "💀" if 𓋴𓋆.search(𓊾) else "🤖"
    return "🤖"


def 𓋹() -> None:
    try:
        𓂮 = json.load(sys.stdin)
    except Exception:
        sys.exit(0)                      # 📥💔 → 🤐 → 🛡️ 🀄🌊 (🚫⛔)
    𓆼 = 𓂮.get("tool_name", "") or ""
    𓊍 = 𓋴(𓆼, 𓂮.get("tool_input") or {})
    if 𓊍 == "🙋":                        # 🙋 → `ask` (→ 👤 🛡️)
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": "🙋 → 👤 🛡️ : 🐈🙏 🐾⏸️ prrr?",
            }
        }))
        return
    if 𓊍 == "💀":                        # 💀🩸🐚 → 📓 `stderr` 🔊 (📵 , 🚫⛔)
        print("😿📓 💀🩸🔫 🐚 🏷️ — 🐈👀 , 🚫⛔ 📵 prrr", file=sys.stderr)
    sys.exit(0)                          # 💀 + 🤖 → 🤐 `exit` 0️⃣ → 🛡️ 🀄🌊


if __name__ == "__main__":
    𓋹()
