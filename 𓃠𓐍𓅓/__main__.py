# 🏁  —  🚀 :  🐍 -m 𓃠𓐍𓅓  [ 🤖 | 🌊 | 🌈 | ⏱️ | 🚀 | 🌱 ]
from __future__ import annotations
import sys

from .𓎋𓊵 import 𓋱𓊞
from .𓆲𓊵 import 𓆲, 𓊪𓏰
from .𓎏𓊵 import 𓊆𓂺


def 𓊪𓅱() -> None:
    # 🏁 🀄 :  🎛️ 👀 → 🤖🎬 ∨ 🕹️🙋‍♀️
        𓊾 = sys.argv[1:]
        𓊍𓏤 = 𓊆𓂺(𓊾)
        𓋉𓏤 = "🌈" in 𓊾                                    # ⚑🌈
        𓋃𓏤 = "⏱️" in 𓊾 or "⏳" in 𓊾                       # ⚑⏱️  ⏳⚔️
        𓋦𓏤 = "🚀" in 𓊾 or "💨" in 𓊾                       # ⚑🚀  🦘 🌟
        𓋱𓏤 = 𓋱𓊞() if ("🌱" in 𓊾 or "🌞" in 𓊾) else None  # ⚑🌱  🎲 ← 🌞🀄
        if any(𓅕 in ("🤖", "🎬", "--🤖") for 𓅕 in 𓊾):
            𓆲(𓊍=𓊍𓏤, 𓋉=𓋉𓏤, 𓋃𓁋=𓋃𓏤, 𓋦𓁋=𓋦𓏤, 𓋱𓉏=𓋱𓏤)
        else:
            𓊪𓏰(𓊍𓏤, 𓋉𓏤, 𓋃𓏤, 𓋦𓏤, 𓋱𓏤)


if __name__ == "__main__":
    𓊪𓅱()
