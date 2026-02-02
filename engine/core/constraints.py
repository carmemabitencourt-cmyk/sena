"""Restrições do domínio.

Define limites básicos para a simulação e geração. As restrições são
simplificadas e devem ser detalhadas posteriormente.
"""

from dataclasses import dataclass


@dataclass
class Constraints:
    """Restrições aplicadas ao motor."""

    max_simulation_size: int = 10000
    min_games: int = 1
    max_games: int = 100

    def validate(self, number_of_games: int, simulation_size: int) -> None:
        """Valida parâmetros básicos do motor."""
        if not (self.min_games <= number_of_games <= self.max_games):
            raise ValueError("number_of_games fora dos limites permitidos")
        if simulation_size > self.max_simulation_size:
            raise ValueError("simulation_size acima do limite")
