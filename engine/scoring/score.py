"""Composição de score.

Define a função que agrega métricas em um score comparativo.
"""

from dataclasses import dataclass


@dataclass
class ScoreResult:
    """Resultado comparativo do score."""

    value: float
    note: str = "Score comparativo, não preditivo."


def calculate_score(stability: float, coverage: float, redundancy: float) -> ScoreResult:
    """Calcula um score simples baseado em pesos fixos (placeholder)."""
    value = (stability * 0.4) + (coverage * 0.4) + (1 - redundancy) * 0.2
    return ScoreResult(value=value)
