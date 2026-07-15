#  𓊪𓂀𓅓  —  🐈👅 🚧  ·  🚫🗣️  ∀ 🐍 🏷️  →  𓂀 / 😺 / meow
#  ✅ : 𓂀 , 😺 🐾 , 🐈🗣️ (meow, mrr, prrr, nya, hiss, purr)
#  ❌ : 🗣️🙈  ASCII 🔤  (𓎉 `__x__` / 📦 `import` 🤝)
#  ➕ 🈲🗣️ (🇨🇳🇭🇰🇵🇱🇲🇻🇳🇴🇺🇬) → 🙊❌ 💥  ∀📂  (📜 🙊📜.md ; 🙈 LICENSE , `.git`)
#  ➕ 🗣️🔤 (🇺🇲🇬🇧) → 😾 💥  ∀ 💬🐍 + 📜📄  (🐾5️⃣ #45 : 🔒 → 🗣️ ↩️ 🚫🔁)
import ast
import builtins
import io
import keyword
import pathlib
import re
import sys
import tokenize

#  🐈🗣️  —  ASCII 🆗  (𓂺 👀)   ·   🔁 🀄  (🪞 `.claude/𓆓𓁐.py` : `meoooow` = `meow`)
𓊞 = {
    "meow", "meoow", "meooow", "meoooow", "mew", "mrr", "mrrr", "mrrrr",
    "prr", "prrr", "prrrr", "purr", "purrr", "nya", "nyan", "hiss", "hsss",
    "miao", "miau", "mao", "mrow", "mrowr", "yowl", "trill", "chirr",
}
𓊞𓊍 = re.compile(
    r"(?i)^(?:m+e+o+w+|m+e+w+|m+i+a+(?:[ou]+w*|w+)|m+r{2,}|p+u*r{2,}"
    r"|h+i*s{2,}|n+y+a+n*|g*r{2,}|y+o+w+l+|t+r+i+l+|c+h+i+r+)$"
)

#  📁  —  🔍  (🏷️ 🀄)
𓊵 = ["𓃠𓐍𓅓.py", "𓊪𓄿𓐍.py", ".claude/𓆓𓁐.py", ".github/𓊪𓂀𓅓.py"]

#  🈲 🗣️  🚫🚫🚫   (🪞 `.claude/𓆓𓁐.py` ; 🔣 `\u` ✍️)
#  🇨🇳🇭🇰 U+3400-4DBF U+4E00-9FFF U+F900-FAFF U+20000-2EBEF · 🇵🇱 U+0104-0107 U+0118-0119
#  U+0141-0144 U+015A-015B U+0179-017C · 🇲🇻 U+0780-07BF · 🇳🇴 U+00C5 U+00C6 U+00D8
#  U+00E5 U+00E6 U+00F8 · 🇺🇬 U+014A-014B
𓉗 = re.compile(
    "[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002ebef"
    "\u0780-\u07bf"
    "\u0104-\u0107\u0118\u0119\u0141-\u0144\u015a\u015b\u0179-\u017c"
    "\u00c5\u00c6\u00d8\u00e5\u00e6\u00f8"
    "\u014a\u014b]"
)

#  📂 🈲🔍
𓉗𓊵 = {".py", ".md", ".sh", ".yml", ".yaml", ".json"}


def 𓉗𓆑():
    #  🈲 🔍  ∀📂   (🙈 `.git` , `__pycache__` , LICENSE)
    𓅾 = []
    for 𓊨 in sorted(pathlib.Path(".").rglob("*")):
        if not 𓊨.is_file() or 𓊨.suffix not in 𓉗𓊵:
            continue
        if ".git" in 𓊨.parts or "__pycache__" in 𓊨.parts:
            continue
        try:
            𓆼 = 𓊨.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for 𓅲, 𓋍 in enumerate(𓆼.split("\n"), 1):
            𓆛 = 𓉗.findall(𓋍)
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

    #  📁  🀄  —  📄 🏷️  𓂀/😺 ❓
    for 𓆓 in 𓊵:
        𓉐 = pathlib.Path(𓆓).stem
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

    if 𓅾:
        print("\n🙀😾  🗣️🙈 / 🈲  —  🚫🐈👅 :")
        for 𓆓, 𓅲, 𓅓 in sorted(set(𓅾)):
            print(f"  ❌  {𓆓}:{𓅲}  →  {𓅓}")
        print(f"\n💥  {len(set(𓅾))}  —  😾  hiss!  🙊❌")
        sys.exit(1)

    print("\n😻🎉  🐈👅  —  ∀ 🏷️  𓂀/😺/meow  ✅  ·  🚫🈲  ✅  ·  🚫🗣️🔤  ✅")


if __name__ == "__main__":
    𓆑()
