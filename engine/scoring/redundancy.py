"""Cálculo de redundância."""

from __future__ import annotations


def redundancy_metric(games: list[list[int]]) -> float:
    """Calcula redundância pela proporção de jogos repetidos."""
    if not games:
        return 0.0

    unique_games = {tuple(game) for game in games}
    total_games = len(games)
    return 1 - (len(unique_games) / total_games)
