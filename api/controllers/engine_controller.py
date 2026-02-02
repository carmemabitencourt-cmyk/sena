"""Controller responsável por orquestrar a geração."""

from engine.index import Engine
from api.schemas.request_schema import GenerateRequest


class EngineController:
    """Controller do motor."""

    def __init__(self) -> None:
        self.engine = Engine()

    def generate(self, payload: GenerateRequest) -> dict:
        """Executa o motor com base no payload recebido."""
        result = self.engine.generate(
            number_of_games=payload.number_of_games,
            simulation_size=payload.simulation_size,
        )
        return {
            "jogos": result.games,
            "metricas": {
                "simulacoes": result.metrics.total_simulations,
                "stability": result.metrics.stability_score,
                "coverage": result.metrics.coverage_score,
                "redundancy": result.metrics.redundancy_score,
                "score": result.score,
            },
            "aviso": result.disclaimer,
        }
