# 💾🏆 📜🔝  —  📥 · 📤 · 🪣🌱 · 🖼️
from __future__ import annotations
import json
import datetime

from .𓊞𓊵 import 𓊆𓈖

# ─────────── 💾🏆 📜🔝 ───────────
𓎋𓊪 = "🏆📜.json"    # 💾 🏁🏁 🛤️  (🏛️)
𓎋𓊪𓋃 = "🏆📜⏳.json"  # 💾 ⏱️ ⏳⚔️ 🛤️  (🏁 🀄 → 📜🔝 ✂️)
𓎋𓊪𓋱 = "🏆📜🌱.json"  # 💾 🌱🌞🎲 🛤️  (∀🐈 🟰 🗺️ / 🌞 → 📜🔝 ✂️)
𓎋𓈖 = 10             # 📜🔝 ⏫-N 💾


def 𓋱𓊞() -> str:
    # 🌞  ⏰ → `%Y%m%d` 🀄  (∀🐈 🟰 🗺️ / 🌞 → 🤝 ⚔️)
    return datetime.date.today().strftime("%Y%m%d")


def 𓋱(𓅔: str) -> tuple[int, int]:
    # 🌱  🌞🀄 → (🎲 , 🌊) :  🌊 = 1 + 🀄 % 9  (🌞 → 🌈 🗺️)
    𓊈 = int(𓅔)
    return 𓊈, 1 + 𓊈 % 𓊆𓈖


def 𓎋(𓊪𓉏: str = 𓎋𓊪) -> list[dict]:
    # 📥  📜🔝  (🙀💔 → 📜🕳️)
    try:
        with open(𓊪𓉏, encoding="utf-8") as 𓆑:
            𓂭 = json.load(𓆑)
        if isinstance(𓂭, list):
            return [𓅘 for 𓅘 in 𓂭 if isinstance(𓅘, dict)]
    except (OSError, ValueError):
        pass
    return []


def 𓎌(𓆳: dict, 𓊪𓉏: str = 𓎋𓊪, 𓈖: int = 𓎋𓈖) -> list[dict]:
    # 📤  ➕🆕 → 🔽🏆 (🟰 → 🔼⏱️) → ✂️ ⏫-N → 💾
    𓂏 = 𓎋(𓊪𓉏)
    𓂏.append(𓆳)
    𓂏.sort(key=lambda 𓅘: (-𓅘.get("🏆", 0), 𓅘.get("⏱️", 0)))
    𓂏 = 𓂏[:𓈖]
    with open(𓊪𓉏, "w", encoding="utf-8") as 𓆑:
        json.dump(𓂏, 𓆑, ensure_ascii=False)
    return 𓂏


def 𓎌𓋱(𓆳: dict, 𓅔: str, 𓈖: int = 𓎋𓈖) -> list[dict]:
    # 📤 🌱 :  ➕ → 🪣/🌞 → ⏫-N / 🪣 → 💾  (👴🌞 💾 ✅ , 🚫 ↔️🌞 🚮)
    #   → ↩️ 🎯 🌞 (𓅔) ☝️ , 🔽🏆  (🖼️ 🟢)
    𓂏 = 𓎋(𓎋𓊪𓋱)
    𓂏.append(𓆳)
    𓆒: dict[str, list[dict]] = {}
    for 𓅘 in 𓂏:
        𓆒.setdefault(str(𓅘.get("🌱", "")), []).append(𓅘)
    𓂏 = []
    for 𓅕 in 𓆒.values():
        𓅕.sort(key=lambda 𓅘: (-𓅘.get("🏆", 0), 𓅘.get("⏱️", 0)))
        𓂏.extend(𓅕[:𓈖])
    with open(𓎋𓊪𓋱, "w", encoding="utf-8") as 𓆑:
        json.dump(𓂏, 𓆑, ensure_ascii=False)
    return [𓅘 for 𓅘 in 𓂏 if str(𓅘.get("🌱", "")) == 𓅔]


def 𓎍(𓂏: list[dict], 𓅔: str | None = None) -> str:
    # 🖼️  📜🔝  (𓅔 = 🌱 🕸️ : 🎯 🟰 🌞 → 👴🌞 🙈)
    if 𓅔 is not None:
        𓂏 = [𓅘 for 𓅘 in 𓂏 if str(𓅘.get("🌱", "")) == 𓅔]
    if not 𓂏:
        return "📜🕳️" if 𓅔 is None else f"🏆📜🔝🌱{𓅔}\n📜🕳️"
    𓂐 = ["🏆📜🔝" if 𓅔 is None else f"🏆📜🔝🌱{𓅔}"]
    for 𓇋, 𓆳 in enumerate(𓂏, 1):
        𓋏 = f"  ⏳{𓆳['⏳']}" if "⏳" in 𓆳 else ""   # ⏱️ 🏁 → ⏳ ↩️
        𓂐.append(
            f"{𓇋}. 🏆{𓆳.get('🏆', 0)}  🎚️{𓆳.get('🎚️', 1)}  ⏱️{𓆳.get('⏱️', 0)}"
            f"  🐟{𓆳.get('🐟', 0)}  🥛{𓆳.get('🥛', 0)}"
            f"  🐦{𓆳.get('🐦', 0)}  😿{𓆳.get('😿', 0)}{𓋏}"
        )
    return "\n".join(𓂐)
