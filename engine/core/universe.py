"""Definição do universo de possibilidades.

Este módulo descreve o espaço amostral básico do motor. A implementação
real deve encapsular regras do jogo, limites de combinação e metadados.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Universe:
    """Estrutura que representa o universo de possibilidades.

    Neste estágio é apenas um contêiner simples para possíveis elementos.
    """

    elements: List[int]

    @classmethod
    def default(cls) -> "Universe":
        """Cria um universo padrão (placeholder)."""
        return cls(elements=list(range(1, 61)))
