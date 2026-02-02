"""Simulação Monte Carlo.

Placeholder para o algoritmo de simulação. Aqui apenas organizamos a
interface para evoluir o modelo futuramente.
"""

from dataclasses import dataclass
from typing import List

from engine.core.generator import GameGenerator
from engine.simulation.metrics import SimulationMetrics


@dataclass
class MonteCarloSimulator:
    """Executor de simulações Monte Carlo."""

    generator: GameGenerator

    def run(self, simulation_size: int, number_of_games: int) -> tuple[List[List[int]], SimulationMetrics]:
        """Executa a simulação e retorna jogos e métricas (stub)."""
        games = self.generator.generate(number_of_games)
        metrics = SimulationMetrics(total_simulations=simulation_size)
        return games, metrics
