"""Simulação Monte Carlo."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import List

from engine.core.generator import GameGenerator
from engine.scoring.coverage import coverage_metric
from engine.scoring.redundancy import redundancy_metric
from engine.scoring.score import calculate_score
from engine.scoring.stability import stability_metric
from engine.simulation.metrics import SimulationMetrics


@dataclass
class MonteCarloSimulator:
    """Executor de simulações Monte Carlo."""

    generator: GameGenerator

    def run(
        self,
        simulation_size: int,
        number_of_games: int,
        seed: int | None = None,
    ) -> tuple[List[List[int]], SimulationMetrics]:
        """Executa a simulação e retorna jogos e métricas agregadas."""
        rng = random.Random(seed)
        best_games: list[list[int]] = []
        best_score = float("-inf")

        stability_total = 0.0
        coverage_total = 0.0
        redundancy_total = 0.0

        for _ in range(simulation_size):
            games = self.generator.generate(number_of_games, rng=rng)
            stability = stability_metric(games)
            coverage = coverage_metric(games, len(self.generator.universe.elements))
            redundancy = redundancy_metric(games)

            score = calculate_score(stability, coverage, redundancy).value
            if score > best_score:
                best_score = score
                best_games = games

            stability_total += stability
            coverage_total += coverage
            redundancy_total += redundancy

        metrics = SimulationMetrics(
            total_simulations=simulation_size,
            stability_score=stability_total / simulation_size if simulation_size else 0.0,
            coverage_score=coverage_total / simulation_size if simulation_size else 0.0,
            redundancy_score=redundancy_total / simulation_size if simulation_size else 0.0,
        )
        return best_games, metrics
