#  𓊪𓂀𓅓  —  🐈👅 🚧  ·  🚫🗣️  ∀ 🐍 🏷️  →  𓂀 / 😺 / meow
#  ✅ : 𓂀 , 😺 🐾 , 🐈🗣️ (meow, mrr, prrr, nya, hiss, purr)
#  ❌ : 🗣️🙈  ASCII 🔤  (𓎉 `__x__` / 📦 `import` 🤝)
#  ➕ 🈲 ∀🏳️🌐 ¬🇺🇲🇬🇧 → 🙊❌ 💥  ∀📂  (⬜📜 ; 📜 🙊📜.md ; 🙈 LICENSE , `.git` , 🐈📜🏛️)
#  ➕ 🗣️🔤 (🇺🇲🇬🇧) → 😾 💥  ∀ 💬🐍 + 📜📄  (🐾5️⃣ #45 : 🔒 → 🗣️ ↩️ 🚫🔁)
#  ➕ 📛 🚧 → 😾 💥  ∀ 📄 📛  (🚫🚫🚫 README : 📛 = 🀄 → 🚫🐈👅 ‼️ ; 🙈 LICENSE , 🎛️)
import ast
import builtins
import io
import json
import keyword
import os
import pathlib
import re
import sys
import tokenize
import unicodedata

#  🐈🗣️  —  ASCII 🆗  (𓂺 👀)   ·   🔁 🀄  (🪞🔒 ≡ `𓃠𓊍` `.claude/𓆓𓁐.py` #70 ; `meoooow` = `meow`)
#  ⏮️ 🌊↔️ ✂️ #70-🥈 : `yowl` `trill` `chirr` = 🗣️🇺🇲 🕳️ → 🚮
𓊞 = {
    "meow", "meoow", "meooow", "meoooow", "mew", "mrr", "mrrr", "mrrrr",
    "prr", "prrr", "prrrr", "purr", "purrr", "nya", "nyan", "hiss", "hsss",
    "miao", "miau", "mao", "mrow", "mrowr",
}
𓊞𓊍 = re.compile(
    r"(?i)^(?:m+e+o+w+|m+e+w+|m+i+a+(?:[ou]+w*|w+)|m+r{2,}|p+u*r{2,}|h+i*s{2,}|n+y+a+n*|g*r{2,})$"
)

#  📁  —  🔍  (🏷️ 🀄)   ·   📦 📁 → 🐾 ∀ 🧱  (#48 ✂️)
𓊵𓉐 = ["𓃠𓐍𓅓", "𓊪𓄿𓐍.py", ".claude/𓆓𓁐.py", ".github/𓊪𓂀𓅓.py"]


def 𓊵𓎗(𓂏):
    #  📁 📜 → 📄 📜  ( 📦 → ∀ `*.py` 🔽 , 🔽📛 )
    𓅕 = []
    for 𓆓 in 𓂏:
        𓊨 = pathlib.Path(𓆓)
        if 𓊨.is_dir():
            𓅕 += sorted(str(𓅘) for 𓅘 in 𓊨.rglob("*.py"))
        else:
            𓅕.append(𓆓)
    return 𓅕


𓊵 = 𓊵𓎗(𓊵𓉐)

#  🙈 📛  —  🐍 🔑 📄 📛  ( 📦 🀄 ‼️ : 🚫 🐈 ✂️ )
𓊵𓅗 = frozenset({"__init__", "__main__"})

#  🈲 ∀🏳️🌐 ¬🇺🇲🇬🇧  🚫🚫🚫  →  🙊❌   (⬜📜 ; 🪞 `.claude/𓆓𓁐.py` ; 📜 🙊📜.md)
#  ✅ : ASCII U+0000-007F (😾🪜) · 𓂀 U+13000-1342F (0️⃣🏛️ ☝️ — ➕A 🚫 : 🖼️🦴🔲 + 🐍<3.12 `Cn`) · 😺🧷 U+200D U+FE0E U+FE0F U+20E3
#       · 😺🔣 ¬`L*` ¬`M*` ¬`Nl` ¬`Nd`  (② ½ → — … ✅ ; 🔢 ⬜📜 `0-9` ☝️)
#  🙊 : ∀🔤 `L*`/`M*`/`Nl`  (🇰🇷🇯🇵🇨🇳🇬🇷🇷🇺🇵🇱🇳🇴 … ∀🏳️) + 🌐🔢 `Nd` ¬ASCII (#70)
#       + 🔤👯 `So` U+249C-24E9 · U+1F110-1F169 (#70 : ⭕🔤 🔲🔤 — 🎭🗣️) + 🪦👅 🤪😹 :
#       U+10000-12FFF (U+12000-1254F , U+10900 …) · U+1D000-1D0FF · U+1D200-1D24F
𓉗𓄤 = frozenset({0x200D, 0xFE0E, 0xFE0F, 0x20E3})
𓉗𓋆 = (
    (0x10000, 0x12FFF), (0x1D000, 0x1D0FF), (0x1D200, 0x1D24F),  # 🪦👅
    (0x249C, 0x24E9), (0x1F110, 0x1F169),                        # 🔤👯 `So` (#70)
)


def 𓉗𓏤(𓋁: str) -> bool:
    # ❓ 🈲🔣   (⬜📜 : ✅ → False)
    𓈙 = ord(𓋁)
    if 𓈙 <= 0x7F or 0x13000 <= 𓈙 <= 0x1342F or 𓈙 in 𓉗𓄤:
        return False                                # 🇺🇲🔤 · 𓂀 · 😺🧷
    if any(𓄿 <= 𓈙 <= 𓃀 for 𓄿, 𓃀 in 𓉗𓋆):
        return True                                 # 🪦👅 + 🔤👯
    𓊍 = unicodedata.category(𓋁)
    return 𓊍[0] in "LM" or 𓊍 in ("Nl", "Nd")       # ∀🏳️🌐 🔤 + 🌐🔢 → 🙊


#  📂 🈲🔍   ·   🙈 🐈📜🏛️ : `.claude/agents/` = 1️⃣📄 ✅ ∀👅  (🪞 𓅗𓆊)
𓉗𓊵 = {".py", ".md", ".sh", ".yml", ".yaml", ".json"}
𓉗𓆊 = re.compile(r"^\.claude/agents/")


def 𓉗𓆑():
    #  🈲 🔍  ∀📂   (🙈 `.git` , `__pycache__` , LICENSE , 🐈📜🏛️)
    𓅾 = []
    for 𓊨 in sorted(pathlib.Path(".").rglob("*")):
        if not 𓊨.is_file() or 𓊨.suffix not in 𓉗𓊵:
            continue
        if ".git" in 𓊨.parts or "__pycache__" in 𓊨.parts:
            continue
        if 𓉗𓆊.match(𓊨.as_posix()):
            continue
        try:
            𓆼 = 𓊨.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for 𓅲, 𓋍 in enumerate(𓆼.split("\n"), 1):
            𓆛 = [𓋁 for 𓋁 in 𓋍 if 𓉗𓏤(𓋁)]
            if 𓆛:
                𓅾.append((str(𓊨), 𓅲, "🙊×%d" % len(𓆛)))
    return 𓅾


#  🗣️🔤 🚧  —  💬🐍 + 📜📄   (🐾5️⃣ #45 : 🔒)
#  🙈-🆓  (📜 🙊📜.md) :
#    `…`   → 🀄 · 🔗 · 📁 · 🪝🀄 · 🐍🏦   (✍️ ⏳ ✍️ ‼️)
#    🔗    → `https://…`
#    📁    → `.py` `.md` …
#    🔣    → `U+0104`
#    ⏫🔤  → LICENSE , YYYYMMDD   (🀄 , 🚫 📜)
#    🐍 🔑 + 🏦   ·   🐈🗣️ 𓊞
𓅗𓊫 = frozenset(keyword.kwlist) | frozenset(dir(builtins))

#  🙈 📂  —  🐈👅 🚫 : `.claude/agents/` (🐈📜 ☝️ ‼️) , 🎛️ (🀄 🗿) , LICENSE
𓅗𓁹 = ("LICENSE",)
𓅗𓆊 = re.compile(r"^(?:\.claude/agents/|\.claude/settings|\.github/workflows/)")

𓅗𓎜 = [
    re.compile(r"^#!.*$", re.M),                     # `#!` 🐍 🛤️
    re.compile(r"```.*?```", re.S),                  # 🀫 📜  (📄)
    re.compile(r"`[^`\n]*`"),                        # 🀄 ☝️
    re.compile(r"https?://\S+|\]\([^)\n]*\)"),       # 🔗
    re.compile(r"\.[A-Za-z0-9]{1,5}\b"),             # 📁
    re.compile(r"\bU\+[0-9A-Fa-f]{4,6}\b"),          # 🔣
]
𓅗𓊖 = re.compile(r"[A-Za-z][A-Za-z'-]{1,}")


def 𓅗𓂺(𓆼):
    #  🚿  🙈-🆓 → 🈳
    for 𓋏 in 𓅗𓎜:
        𓆼 = 𓋏.sub(" ", 𓆼)
    return 𓆼


def 𓅗𓅲(𓊨):
    #  📄 → 👀 𓄽   (🐍 → 💬 ☝️ ; 📄 → 📜 , 🚫 🀫)
    𓆼 = 𓊨.read_text(encoding="utf-8")
    if 𓊨.suffix != ".py":
        return [(𓅲, 𓋍) for 𓅲, 𓋍 in enumerate(𓅗𓂺(𓆼).split("\n"), 1)]
    try:
        return [(𓊙.start[0], 𓅗𓂺(𓊙.string))
                for 𓊙 in tokenize.generate_tokens(io.StringIO(𓆼).readline)
                if 𓊙.type == tokenize.COMMENT]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return []


def 𓅗(𓊨):
    #  🗣️🔤 🔍  →  [(𓅲 , 🔤)]
    𓅾 = []
    for 𓅲, 𓋍 in 𓅗𓅲(𓊨):
        for 𓅓 in 𓅗𓊖.findall(𓋍):
            if 𓅓.isupper() or 𓅓 in 𓅗𓊫 or 𓂺(𓅓):
                continue
            𓅾.append((𓅲, 𓅓))
    return 𓅾


def 𓅗𓆑():
    #  🗣️🔤 🚧  ∀ 🐍 💬 + 📄 📜   (🙈 : 🐈📜 , 🎛️ , LICENSE , `.git`)
    𓅾 = []
    for 𓊨 in sorted(pathlib.Path(".").rglob("*")):
        if not 𓊨.is_file() or 𓊨.suffix not in (".py", ".md"):
            continue
        if ".git" in 𓊨.parts or "__pycache__" in 𓊨.parts:
            continue
        𓉐 = 𓊨.as_posix()
        if 𓉐 in 𓅗𓁹 or 𓅗𓆊.match(𓉐):
            continue
        for 𓅲, 𓅓 in 𓅗(𓊨):
            𓅾.append((𓉐, 𓅲, "😾 " + 𓅓))
    return 𓅾


#  📛 🚧  —  📄 📛 → 𓂀 / 😺 / meow ☝️   ( 🚫🚫🚫 README 😾 ‼️ )
#  🍂 : 🀄 CI 👀 📄 🀄 (💬🐍 + 📜📄) , 🚫 📛 → `README.md` 🐈👅 🀄 → CI ✅ 🕳️
#  🙈 : LICENSE , `.gitignore` , 🎛️ (`.claude/settings` , `.github/workflows/`)
𓉐𓁹 = frozenset({"LICENSE", ".gitignore", ".gitattributes", ".gitmodules",
                 "pyproject.toml"})
𓉐𓆊 = re.compile(r"^(?:\.claude/settings|\.github/workflows/)")


def 𓉐𓆑():
    #  📛 🔍  ∀📄   →  [(📛 , 0 , 📛)]   ( 🀄 📛 = 😾 → 🚫🐈👅 ‼️ )
    𓅾 = []
    for 𓊨 in sorted(pathlib.Path(".").rglob("*")):
        if not 𓊨.is_file():
            continue
        if ".git" in 𓊨.parts or "__pycache__" in 𓊨.parts:
            continue
        𓉐 = 𓊨.as_posix()
        if 𓊨.name in 𓉐𓁹 or 𓉐𓆊.match(𓉐):
            continue
        𓉔 = 𓊨.stem
        if 𓉔 in 𓊵𓅗:                       # `__init__` `__main__` = 🐍 🔑 📛
            continue
        if not 𓐍(𓉔) and not 𓂺(𓉔):       # 🚫 𓂀/😺 ∧ 🚫 🐈🗣️  →  😾
            𓅾.append((𓉐, 0, "📛 " + 𓉔))
    return 𓅾


def 𓎉(𓅓):
    #  ❓  `__x__`
    return 𓅓.startswith("__") and 𓅓.endswith("__")


def 𓂺(𓅓):
    #  ❓  🐈🗣️  (`meow_2` , `mrrr_prrr` , `hisssss` , `miaou` …)
    𓆛 = 𓅓.strip("_").lower()
    if 𓆛 in 𓊞 or 𓊞𓊍.match(𓆛):
        return True
    return all(𓋁 in 𓊞 or 𓊞𓊍.match(𓋁) or 𓋁.isdigit()
               for 𓋁 in 𓆛.split("_") if 𓋁)


def 𓐍(𓅓):
    #  ❓  𓂀 / 😺  →  🚫 ASCII
    return any(ord(𓋁) > 0x7F for 𓋁 in 𓅓)


def 𓎘(𓅓, 𓋴):
    #  🐈 ✅ ❓   (𓋴 = 📦 `import` 🤝)
    if not 𓅓 or 𓅓 == "_":
        return True
    if 𓎉(𓅓) or 𓅓 in 𓋴:
        return True
    return 𓐍(𓅓) or 𓂺(𓅓)


def 𓊟(𓊒):
    #  📦  `import` 🤝  —  🐍🏦 🀄 ASCII , 🚫 🐈 😾
    𓋴 = set()
    for 𓊙 in ast.walk(𓊒):
        if isinstance(𓊙, ast.Import):
            for 𓇬 in 𓊙.names:
                𓋴.add((𓇬.asname or 𓇬.name).split(".")[0])
        elif isinstance(𓊙, ast.ImportFrom):
            for 𓇬 in 𓊙.names:
                𓋴.add(𓇬.asname or 𓇬.name)
    return 𓋴


def 𓋭(𓊒):
    #  🏷️  ∀ 🆕  →  (🏷️ , 𓅲)
    for 𓊙 in ast.walk(𓊒):
        if isinstance(𓊙, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            yield 𓊙.name, 𓊙.lineno
        elif isinstance(𓊙, ast.Name) and isinstance(𓊙.ctx, (ast.Store, ast.Del)):
            yield 𓊙.id, 𓊙.lineno
        elif isinstance(𓊙, ast.arg):
            yield 𓊙.arg, 𓊙.lineno
        elif isinstance(𓊙, ast.ExceptHandler) and 𓊙.name:
            yield 𓊙.name, 𓊙.lineno


#  ⛙📨 🐈👅 👀  —  ⛙💬 `commit` · 🔀📛 PR `title` · ⛙📄 PR `body`   (#76 , 👑𓃠 🔓⚖️)
#  🀄 ⬜📜 + 🤖📎🧱 : `Co-authored-by:` · `Claude-Session:` · `Generated by Claude Code`
#       · 🔗 · `#🔢`/`(#🔢)` · 🐍🔑/🏦 · 📁 · `…` · 🔠 (⏫🔤)   →  🚫 ✅🔴 ♾️
#  🐈✍️ (🔏 `signature` ∨ 📧 `claude`/`noreply`) 🗣️🔤/🈲 → 😾❌ (exit 1)
#  🙋✍️ (👤)                         🗣️🔤/🈲 → 🗒️⚠️ ☝️ (🚫🙅 : 🙋 🙇✅)
#  🕰️📜 🍂 = 🍂 (🚫 ✍️🕰️ , 🚫🔨 `meow`)   ·   🪞 `.claude/𓊗𓆓.py` 📐 (𓉗𓏤 ♻️)

#  🤖📎🧱 + 🔢🔗  —  🚿 ☝️  ( ⛙📨 : 🀄 🐍💬📄 🙈 `𓅗𓎜` ♻️ + 🤖📎 )
𓅘𓊫 = [
    re.compile(r"(?im)^\s*co-authored-by:.*$"),
    re.compile(r"(?im)^\s*claude-session:.*$"),
    re.compile(r"(?i)generated by claude code"),
    re.compile(r"\(#\d+\)|#\d+"),                    # 🔢 🔗
]
#  🐈🔏  —  ✍️ = 🐈 ❓  ( 📎 `signature` ∨ 📧 `noreply`/`claude`/𓃠 )
𓅘𓁹 = re.compile(r"(?i)claude-session:|generated by claude code|co-authored-by:\s*claude")
𓅘𓅂 = re.compile(r"(?i)claude|noreply|𓃠")


def 𓅘𓂺(𓆼):
    #  🚿  🤖📎🧱 + 🔢🔗 → 🈳   ·   ⏳ 🀄 🐍💬📄 🙈 (`𓅗𓂺`)
    for 𓋏 in 𓅘𓊫:
        𓆼 = 𓋏.sub(" ", 𓆼)
    return 𓅗𓂺(𓆼)


def 𓅘(𓆼):
    #  ⛙📨 → (🗣️🔤 [🔤] , 🈲 [🔣])   ( 🗣️🔤 : 🙈🚿 → ¬🔠 ¬🐍🔑 ¬🐈🗣️ )
    𓊥 = [𓅓 for 𓅓 in 𓅗𓊖.findall(𓅘𓂺(𓆼))
         if not (𓅓.isupper() or 𓅓 in 𓅗𓊫 or 𓂺(𓅓))]
    return 𓊥, [𓋁 for 𓋁 in 𓆼 if 𓉗𓏤(𓋁)]


def 𓅘𓅱(𓆼):
    #  ✍️ = 🐈 ❓   ( 🔏 `signature` ∨ 📧 `claude`/`noreply`/𓃠 )
    return bool(𓅘𓁹.search(𓆼[0]) or 𓅘𓅂.search(𓆼[1]))


def 𓅘𓉔():
    #  📥  🐙 🎪 JSON  →  [(🏷️ , 📄 , 🐈❓)]   ( ⛙💬 · 🔀📛 · ⛙📄 )
    𓉐 = os.environ.get("GITHUB_EVENT_PATH")
    if not 𓉐 or not os.path.exists(𓉐):
        return []
    try:
        with open(𓉐, encoding="utf-8") as 𓆑:
            𓂭 = json.load(𓆑)
    except (OSError, ValueError):
        return []
    𓅕 = []
    𓊐 = 𓂭.get("pull_request")
    if isinstance(𓊐, dict):                          # 🔀 : 📛 + 📄  ( ✍️ = f(📄 🔏 ∨ 👤) )
        𓋍, 𓁋 = 𓊐.get("body") or "", str((𓊐.get("user") or {}).get("login", ""))
        𓁉 = 𓅘𓅱((𓋍, 𓁋))
        𓅕.append(("🔀📛", 𓊐.get("title") or "", 𓁉))
        𓅕.append(("⛙📄", 𓋍, 𓁉))
    for 𓊙 in 𓂭.get("commits") or []:                 # 📌 : ⛙💬  ( ✍️ = f(💬 🔏 ∨ 📧) )
        if not isinstance(𓊙, dict):
            continue
        𓋍 = 𓊙.get("message") or ""
        𓇬 = 𓊙.get("author") or {}
        𓅕.append(("⛙💬", 𓋍, 𓅘𓅱((𓋍, str(𓇬.get("email", "")) + " " + str(𓇬.get("name", ""))))))
    return 𓅕


def 𓅘𓆑():
    #  ⛙📨 👀  —  🐈✍️ 🗣️🔤/🈲 → 😾❌ (exit 1)  ·  🙋✍️ → 🗒️⚠️ ☝️   (#76)
    𓊘 = 𓅘𓉔()
    if not 𓊘:
        print("⛙📨 👀 — 🎪 ∅  (🚫 GITHUB_EVENT_PATH)  → 🤫")
        return
    𓅾 = []
    for 𓅘𓉏, 𓆼, 𓁉 in 𓊘:
        𓊥, 𓊤 = 𓅘(𓆼)
        if not (𓊥 or 𓊤):
            print(f"👀 {𓅘𓉏} ({'🐈' if 𓁉 else '🙋'}) — ✅")
            continue
        𓊾 = []
        if 𓊥:
            𓊾.append("🗣️🔤 " + " ".join(sorted(set(𓊥))))
        if 𓊤:
            𓊾.append("🙊×%d" % len(𓊤))
        𓋏 = " · ".join(𓊾)
        if 𓁉:
            print(f"❌ {𓅘𓉏} (🐈) — 😾 {𓋏}")
            𓅾.append((𓅘𓉏, 𓋏))
        else:
            print(f"⚠️ {𓅘𓉏} (🙋) — 🗒️ {𓋏}   (✍️🙋 → 🚫🙅)")
    if 𓅾:
        print(f"\n💥  {len(𓅾)}  ⛙📨 🐈✍️ 🗣️🔤/🈲  —  😾  hiss!  🙊❌")
        print("   🕰️📜 🍂 = 🍂  →  🩹 🆕 ⛙📨 (🚫 ✍️🕰️ , 🚫🔨 `meow`)")
        sys.exit(1)
    print("\n😻🎉  ⛙📨 🐈👅  ✅")


def 𓆑():
    𓅾 = []
    for 𓆓 in 𓊵:
        𓊨 = pathlib.Path(𓆓)
        if not 𓊨.exists():
            print("🙀❓", 𓆓)
            continue
        𓊒 = ast.parse(𓊨.read_text(encoding="utf-8"), filename=𓆓)
        𓋴 = 𓊟(𓊒)
        𓆛 = [(𓆓, 𓅲, 𓅓) for 𓅓, 𓅲 in 𓋭(𓊒) if not 𓎘(𓅓, 𓋴)]
        𓅾 += 𓆛
        print("👀", 𓆓, "—", f"😿 ×{len(𓆛)}" if 𓆛 else "✅")

    #  📁  🀄  —  📄 🏷️  𓂀/😺 ❓   ( 🙈 : `__init__` `__main__` = 🐍 🔑 📛 )
    for 𓆓 in 𓊵:
        𓉐 = pathlib.Path(𓆓).stem
        if 𓉐 in 𓊵𓅗:
            continue
        if not 𓐍(𓉐) and not 𓂺(𓉐):
            𓅾.append((𓆓, 0, 𓉐))

    #  🈲 🔍  ∀📂   (🙊❌ ‼️‼️)
    𓊤 = 𓉗𓆑()
    print("👀 🈲 ∀📂 —", f"🙊 ×{len(𓊤)}" if 𓊤 else "✅")
    𓅾 += 𓊤

    #  🗣️🔤 🔍  💬🐍 + 📜📄   (🐾5️⃣ #45 : 🔒 ‼️)
    𓊥 = 𓅗𓆑()
    print("👀 🗣️🔤 💬🐍+📜📄 —", f"😾 ×{len(𓊥)}" if 𓊥 else "✅")
    𓅾 += 𓊥

    #  📛 🔍  ∀📄   ( 🚫🚫🚫 README 😾 : 📛 = 🀄 → 🚫🐈👅 ‼️ )
    𓊧 = 𓉐𓆑()
    print("👀 📛 ∀📄 —", f"😾 ×{len(𓊧)}" if 𓊧 else "✅")
    𓅾 += 𓊧

    if 𓅾:
        print("\n🙀😾  🗣️🙈 / 🈲  —  🚫🐈👅 :")
        for 𓆓, 𓅲, 𓅓 in sorted(set(𓅾)):
            print(f"  ❌  {𓆓}:{𓅲}  →  {𓅓}")
        print(f"\n💥  {len(set(𓅾))}  —  😾  hiss!  🙊❌")
        sys.exit(1)

    print("\n😻🎉  🐈👅  —  ∀ 🏷️  𓂀/😺/meow  ✅  ·  🚫🈲  ✅  ·  🚫🗣️🔤  ✅  ·  📛 ✅")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "📨":
        𓅘𓆑()                                        # ⛙📨 👀  (#76)
    else:
        𓆑()                                          # 📂 👀  (🏷️ · 🈲 · 🗣️🔤 · 📛)
