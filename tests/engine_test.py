"""Testes iniciais do motor."""

from engine.index import Engine


def test_engine_returns_disclaimer() -> None:
    engine = Engine()
    result = engine.generate(number_of_games=1, simulation_size=10)

    assert result.disclaimer
    assert result.games


def test_engine_is_deterministic_with_seed() -> None:
    engine_a = Engine(seed=123)
    engine_b = Engine(seed=123)

    result_a = engine_a.generate(number_of_games=3, simulation_size=5)
    result_b = engine_b.generate(number_of_games=3, simulation_size=5)

    assert result_a.games == result_b.games
    assert result_a.metrics == result_b.metrics


def test_metrics_are_bounded() -> None:
    engine = Engine(seed=999)
    result = engine.generate(number_of_games=5, simulation_size=8)

    assert 0.0 <= result.metrics.stability_score <= 1.0
    assert 0.0 <= result.metrics.coverage_score <= 1.0
    assert 0.0 <= result.metrics.redundancy_score <= 1.0
