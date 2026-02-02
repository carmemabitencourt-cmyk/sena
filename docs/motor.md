# Motor Monte Carlo

## Resumo do modelo matemático

O motor usa amostragem Monte Carlo para gerar conjuntos de jogos candidatos a partir de um universo hipotético de possibilidades. A cada iteração, um conjunto é avaliado com métricas comparativas (score), sem qualquer garantia de previsão.

## Função de score

A função de score combina dimensões qualitativas como:

- **Estabilidade**: consistência do conjunto entre simulações.
- **Cobertura**: diversidade do conjunto em relação ao universo.
- **Redundância**: penalização de repetições.

> O score é **apenas comparativo** e não implica probabilidade real de acerto.

## Limites do motor

- Não prevê resultados futuros.
- Métricas são aproximadas e dependem do tamanho da simulação.
- A saída é uma exploração estatística, não uma afirmação determinística.
