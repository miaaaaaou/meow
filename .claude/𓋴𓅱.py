#!/usr/bin/env python3
# 🪝 `PreToolUse` — 🐈👅 🛂 : 🔧📥 🀫 → 🗣️🔤/🈲 👀 → 📢😾 WARN ☝️  (⚔️ `Stop` 🕘 : 🔧⏮️ 📢)
#   🀫 : `Bash`/`Monitor` `# 💬` (💬 ☝️ — 🚫 `gh` 🏦 : `gh pr create` 🚫👻) · 🐙 `mcp__github*` `title`/`body`/`message` 🀫📛
#        · `Write`/`Edit`/`MultiEdit` `content`/`new_string` (💾♾️ 🀄 : 🔨→⛙→`meow` ♾️ ; #115)
#        · 👤📨 : `AskUserQuestion` (`question`/`header`/`label`/`description`) · 📳 (`Notif`/`PushNotification`) · ⏰ (`Schedule*`/`send_later` : `reason`/`message`/`prompt`) ; #119
#   🐍🀫💥🛡️ ‼️ : `Write` 📜(`.md`) → 🈵 (🗣️🔤+🈲) · 🐍/🀫 → 🈲🔣 ☝️ (🔑/ASCII 📛 → 🚫🗣️🔤 → 🚫🀫💥)
#   🆓🛂 : `.claude/agents/*.md` (🧬 = 🙋👑 📄) · `LICENSE` (👴 🚫∆) → 🚫👀
#   🛡️🥇 ‼️ : 🚫 `deny` · 🚫🧱 (🀄🐛🪝 → ∀🔧🧱 = 🀫💥 ☠️) → `additionalContext` ☝️ , `exit` 0️⃣ ∀
#   ➕ 🚫⚔️ 👴 `𓋴𓆓.py` (🙋/💀/🤖 🚦) : 🚫 `permissionDecision` → 🀄🌊 🗿
# 📚 https://code.claude.com/docs/en/hooks
# 📥 `stdin`  `{"tool_name", "tool_input", …}`  →  📤 `{"hookSpecificOutput": {…, "additionalContext"}}` | 🤫
import importlib.util
import json
import os
import re
import sys

# ♻️ 𓆓𓁐  (𓁹 🗣️🔢 [🙈 `⌨️` 🔗 📁 + 🐈✅] + 𓉗𓆛 🈲⬜📜 + 𓅱 😾🪜)
𓊒 = importlib.util.spec_from_file_location(
    "𓆓𓁐",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "𓆓𓁐.py"),
)
𓆦 = importlib.util.module_from_spec(𓊒)
𓊒.loader.exec_module(𓆦)

𓋴𓊫 = frozenset({"title", "body", "message"})   # 🐙 🀫📛 : 📜 ☝️  (🚫 `content`/`path` 🀫🐍)
𓋴𓋆 = re.compile(r"(?m)(?:^|\s)#(.*)$")           # `# 💬` ✂️  (`Bash` 🀫 ☝️ — 🚫 🏦 : `#🔢`→🔢🚫👻)
𓋴𓎉 = frozenset({"Write", "Edit", "MultiEdit"})   # 💾♾️ 🀄 (#115)
# 👤📨 🀫📛 (#119) : ❓🔘 (`AskUserQuestion`) · 📳 (`message`/`title`/`body`/`subtitle`) · ⏰ (`reason`/`prompt`)
𓋴𓊫𓁐 = frozenset({
    "question", "header", "label", "description",
    "message", "title", "body", "subtitle", "reason", "prompt",
})
𓋴𓃰 = re.compile(r"Notif|Schedule|send_later")   # 📳/⏰ 🔧📛 🔤⊂ 🛡️  (🤏🔧 ∅ → 🌀🚶 ∅ → 🤐)
# 🆓🛂 : 🧬 DNA (`.claude/agents/*.md`) · `LICENSE`  (👤📄 — 🐈🚫🖐️ ; 🚫👀)
𓋴𓁋𓁋 = re.compile(r"(?:^|/)\.claude/agents/[^/]*\.md$|(?:^|/)LICENSE$")


def 𓋴𓅗(𓂏, 𓊾: list, 𓅆: frozenset = 𓋴𓊫) -> None:
    # 🌀🚶 : 🀫📛 (𓅆 ⊂ `title`/`body`/`message`/❓/🔘/⏰…) → 📜  (🐙 🪺 `body` · ❓ 🪺 `options[].label` ✅)
    if isinstance(𓂏, dict):
        for 𓅕, 𓆿 in 𓂏.items():
            if 𓅕 in 𓅆 and isinstance(𓆿, str):
                𓊾.append(𓆿)
            else:
                𓋴𓅗(𓆿, 𓊾, 𓅆)
    elif isinstance(𓂏, list):
        for 𓆿 in 𓂏:
            𓋴𓅗(𓆿, 𓊾, 𓅆)


def 𓋴𓊙(𓂭: dict, 𓊾𓏤: list, 𓊾𓎼: list) -> None:
    # 💾♾️ 🀄 (`Write`/`Edit`/`MultiEdit`) : `content`/`new_string`/`edits[].new_string` ✂️
    #   🆓🛂 (🧬 · `LICENSE`) → ∅ · 📜(`.md`) → 🈵🀫 (𓊾𓏤) · 🐍/🀫 → 🈲🔣 ☝️ (𓊾𓎼 : 🔑/ASCII 🚫🗣️🔤)
    𓊨 = 𓂭.get("file_path") or 𓂭.get("path") or ""
    if 𓋴𓁋𓁋.search(𓊨):
        return
    𓋳 = 𓊾𓏤 if 𓊨.endswith(".md") else 𓊾𓎼
    𓆿 = 𓂭.get("content")
    if isinstance(𓆿, str):
        𓋳.append(𓆿)
    𓆿 = 𓂭.get("new_string")
    if isinstance(𓆿, str):
        𓋳.append(𓆿)
    for 𓇋 in 𓂭.get("edits") or []:
        if isinstance(𓇋, dict) and isinstance(𓇋.get("new_string"), str):
            𓋳.append(𓇋["new_string"])


def 𓋴𓄲(𓆼: str, 𓂭: dict) -> tuple:
    # 🔧📥 → (🈵🀫[🗣️🔤+🈲] , 🐍🀫[🈲 ☝️])
    #   `Bash`/`Monitor` `# 💬` · 🐙 `title`/`body`/`message` · 💾♾️ `content`/`new_string`
    #   · 👤📨 (`AskUserQuestion`·📳·⏰) 🀫📛 (𓋴𓊫𓁐) · 🀫🔧 → ∅
    𓂭 = 𓂭 or {}
    𓊾𓏤, 𓊾𓎼 = [], []
    if 𓆼 in ("Bash", "Monitor"):
        𓊾𓏤 += 𓋴𓋆.findall(𓂭.get("command", "") or "")
    elif 𓆼.startswith("mcp__github"):
        𓋴𓅗(𓂭, 𓊾𓏤)
    elif 𓆼 in 𓋴𓎉:
        𓋴𓊙(𓂭, 𓊾𓏤, 𓊾𓎼)
    elif 𓆼 == "AskUserQuestion" or 𓋴𓃰.search(𓆼):
        𓋴𓅗(𓂭, 𓊾𓏤, 𓋴𓊫𓁐)   # 👤📨 : 🈵🀫 (🗣️🔤+🈲) — 👤👀 📜 = 🐈👅 ✅
    return 𓊾𓏤, 𓊾𓎼


def 𓋹() -> None:
    try:
        𓂮 = json.load(sys.stdin)
    except Exception:
        sys.exit(0)                      # 📥💔 → 🤐  (🚫⛔ , 🛡️ 🀄🌊)
    𓆼 = 𓂮.get("tool_name", "") or ""
    𓊾𓏤, 𓊾𓎼 = 𓋴𓄲(𓆼, 𓂮.get("tool_input") or {})
    𓈖 = sum(𓆦.𓁹(𓋍) for 𓊨 in 𓊾𓏤 for 𓋍 in 𓊨.split("\n"))   # 🗣️🔤 : 🈵🀫 ☝️ (🚫🐍 → 🚫🀫💥)
    𓈲 = sum(len(𓆦.𓉗𓆛(𓊨)) for 𓊨 in 𓊾𓏤 + 𓊾𓎼)              # 🈲🔣 : ∀🀫 (🐍 ➕ — CJK 🚫👻 ∀)
    if not (𓈖 or 𓈲):
        sys.exit(0)                      # 🐈👅 ✅ ∨ 🀫🔧 → 🤫 prrr
    𓊰 = []
    if 𓈖:
        𓊰.append(f"🗣️🔤×{𓈖}")
    if 𓈲:
        𓊰.append(f"🈲🔣×{𓈲}🙊")
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": (
                𓆦.𓅱(𓈖 + 𓈲).strip() + " 🔧📥 " + " + ".join(𓊰) +
                " 🙀🚫🚫🚫 — 🐈👅‼️ 🔧⏮️ : 🖼️😺 𓂀𓃠 🔢 "
                "`meow` `mrrr` `prrr` `hisss` `nya` ✅ → ✍️🔁 meow!"
            ),
        }
    }))
    sys.exit(0)                          # 🚫🧱 ‼️ — WARN ☝️ , 🔧 ⏭️  (🚫 `permissionDecision`)


if __name__ == "__main__":
    𓋹()
