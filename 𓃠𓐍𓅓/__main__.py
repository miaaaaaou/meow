# 🏁  —  🚀 :  🐍 -m 𓃠𓐍𓅓  [ 🤖 | 🌊 | 🌈 | ⏱️ | 🚀 | 🌱 | 🌲🏜️🏔️ ]
from __future__ import annotations
import sys

from .𓎋𓊵 import 𓋱𓊞
from .𓆲𓊵 import 𓆲, 𓊪𓏰
from .𓎏𓊵 import 𓊆𓂺
from .𓊞𓊵 import 𓆵𓊗


def 𓊪𓅱() -> None:
    # 🏁 🀄 :  🎛️ 👀 → 🤖🎬 ∨ 🕹️🙋‍♀️
        𓊾 = sys.argv[1:]
        𓊍𓏤 = 𓊆𓂺(𓊾)
        𓋉𓏤 = "🌈" in 𓊾                                    # ⚑🌈
        𓋃𓏤 = "⏱️" in 𓊾 or "⏳" in 𓊾                       # ⚑⏱️  ⏳⚔️
        𓋦𓏤 = "🚀" in 𓊾 or "💨" in 𓊾                       # ⚑🚀  🦘 🌟
        𓋱𓏤 = 𓋱𓊞() if ("🌱" in 𓊾 or "🌞" in 𓊾) else None  # ⚑🌱  🎲 ← 🌞🀄
        𓆵𓏤 = next((𓅕 for 𓅕 in 𓊾 if 𓅕 in 𓆵𓊗), None)      # 🗺️ 🀫 ☝️  ( ∅ → 🎲 ← 𓊃 )
        if any(𓅕 in ("🤖", "🎬", "--🤖") for 𓅕 in 𓊾):
            𓆲(𓊍=𓊍𓏤, 𓋉=𓋉𓏤, 𓋃𓁋=𓋃𓏤, 𓋦𓁋=𓋦𓏤, 𓋱𓉏=𓋱𓏤, 𓆵𓉏=𓆵𓏤)
        else:
            𓊪𓏰(𓊍𓏤, 𓋉𓏤, 𓋃𓏤, 𓋦𓏤, 𓋱𓏤, 𓆵𓏤)


if __name__ == "__main__":
    𓊪𓅱()
