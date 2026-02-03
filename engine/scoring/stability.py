"""Cálculo de estabilidade."""

from __future__ import annotations

import itertools


def stability_metric(games: list[list[int]]) -> float:
    """Calcula estabilidade pela similaridade média entre jogos.

    Usa a média de similaridade de Jaccard para cada par de jogos.
    Retorna valores entre 0 e 1.
    """
    if not games:
        return 0.0
    if len(games) == 1:
        return 1.0

    total_similarity = 0.0
    comparisons = 0
    for left, right in itertools.combinations(games, 2):
        left_set = set(left)
        right_set = set(right)
        union = left_set | right_set
        if not union:
            continue
        similarity = len(left_set & right_set) / len(union)
        total_similarity += similarity
        comparisons += 1

    return total_similarity / comparisons if comparisons else 0.0
