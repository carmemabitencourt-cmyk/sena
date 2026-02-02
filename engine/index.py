"""Interface principal do motor."""

from dataclasses import dataclass

from engine.core.constraints import Constraints
from engine.core.generator import GameGenerator
from engine.core.universe import Universe
from engine.scoring.score import calculate_score
from engine.simulation.monte_carlo import MonteCarloSimulator
from engine.simulation.metrics import SimulationMetrics


@dataclass
class EngineResult:
    """Resultado da execução do motor."""

    games: list[list[int]]
    metrics: SimulationMetrics
    score: float
    disclaimer: str


class Engine:
    """Motor probabilístico de geração de jogos.

    Não faz previsões: apenas gera cenários com métricas comparativas.
    """

    def __init__(self, constraints: Constraints | None = None) -> None:
        self.constraints = constraints or Constraints()
        self.universe = Universe.default()
        self.generator = GameGenerator(self.universe)
        self.simulator = MonteCarloSimulator(self.generator)

    def generate(self, number_of_games: int, simulation_size: int) -> EngineResult:
        """Executa a geração de jogos e métricas."""
        self.constraints.validate(number_of_games, simulation_size)
        games, metrics = self.simulator.run(simulation_size, number_of_games)
        score_result = calculate_score(
            metrics.stability_score,
            metrics.coverage_score,
            metrics.redundancy_score,
        )
        return EngineResult(
            games=games,
            metrics=metrics,
            score=score_result.value,
            disclaimer=score_result.note,
        )
