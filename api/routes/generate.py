"""Rotas de geração."""

from fastapi import APIRouter, HTTPException

from api.controllers.engine_controller import EngineController
from api.schemas.request_schema import GenerateRequest

router = APIRouter()
controller = EngineController()


@router.post("/generate")
def generate_games(payload: GenerateRequest) -> dict:
    """Gera jogos com base em simulação Monte Carlo."""
    try:
        return controller.generate(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
