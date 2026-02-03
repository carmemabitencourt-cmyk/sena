"""Cálculo de cobertura."""

from __future__ import annotations


def coverage_metric(games: list[list[int]], universe_size: int) -> float:
    """Calcula cobertura relativa do universo."""
    if universe_size <= 0:
        return 0.0
    if not games:
        return 0.0

    unique_elements = {element for game in games for element in game}
    return len(unique_elements) / universe_size
