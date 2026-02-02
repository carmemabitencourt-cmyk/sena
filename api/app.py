"""Aplicação FastAPI."""

from fastapi import FastAPI

from api.routes.generate import router as generate_router

app = FastAPI(
    title="Motor Monte Carlo",
    description="API para geração de jogos baseada em simulação Monte Carlo.",
    version="0.1.0",
)

app.include_router(generate_router)
