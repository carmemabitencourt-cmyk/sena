"""Testes iniciais do motor."""

from engine.index import Engine


def test_engine_returns_disclaimer() -> None:
    engine = Engine()
    result = engine.generate(number_of_games=1, simulation_size=10)

    assert result.disclaimer
    assert result.games
