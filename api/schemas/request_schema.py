"""Schemas de requisição."""

from typing import Literal

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """Payload esperado para geração de jogos."""

    number_of_games: int = Field(..., ge=1, le=100, description="Quantidade de jogos")
    profile: Literal["explorador", "balanceado", "estatistico"] = Field(
        ..., description="Perfil de geração"
    )
    simulation_size: int = Field(..., ge=1, le=10000, description="Tamanho da simulação")
