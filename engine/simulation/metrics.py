"""Métricas de simulação.

Estruturas básicas para métricas agregadas retornadas pelo motor.
"""

from dataclasses import dataclass


@dataclass
class SimulationMetrics:
    """Métricas agregadas da simulação."""

    total_simulations: int
    stability_score: float = 0.0
    coverage_score: float = 0.0
    redundancy_score: float = 0.0
