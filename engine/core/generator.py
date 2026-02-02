"""Gerador de jogos a partir do universo.

Nesta versão inicial, a lógica é apenas um stub. A implementação futura
poderá levar em conta restrições e perfis de geração.
"""

from dataclasses import dataclass
from typing import List

from engine.core.universe import Universe


@dataclass
class GameGenerator:
    """Gerador de jogos baseado em um universo de elementos."""

    universe: Universe

    def generate(self, quantity: int) -> List[List[int]]:
        """Gera jogos de forma simples.

        Este método deve ser substituído por lógica real de amostragem.
        """
        return [self.universe.elements[:6] for _ in range(quantity)]
