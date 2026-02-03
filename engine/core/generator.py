"""Gerador de jogos a partir do universo."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import List

from engine.core.universe import Universe


@dataclass
class GameGenerator:
    """Gerador de jogos baseado em um universo de elementos."""

    universe: Universe
    game_size: int = 6

    def generate(self, quantity: int, rng: random.Random | None = None) -> List[List[int]]:
        """Gera jogos a partir do universo.

        Cada jogo é uma combinação única de elementos (sem repetição),
        com ordenação determinística para facilitar comparação.
        """
        if quantity <= 0:
            return []
        if self.game_size > len(self.universe.elements):
            raise ValueError("game_size maior do que o universo disponível")

        rng = rng or random.Random()
        games: list[list[int]] = []
        for _ in range(quantity):
            game = rng.sample(self.universe.elements, self.game_size)
            games.append(sorted(game))
        return games
