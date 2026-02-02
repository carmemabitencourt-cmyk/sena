# Arquitetura

## Visão geral

O repositório adota separação por camadas:

- **Domínio (engine/)**: regras, modelos e simulação Monte Carlo.
- **API (api/)**: interface HTTP para consumo externo.
- **Infraestrutura**: configuração de deploy (Railway), variáveis de ambiente e testes.

## Fluxo principal

1. A API recebe a requisição de geração.
2. O controller valida parâmetros e chama o motor.
3. O motor cria um universo simplificado, aplica restrições e executa simulações.
4. O resultado retorna métricas e jogos gerados, sempre com aviso de limites probabilísticos.

## Princípios

- Código modular e legível.
- Contratos explícitos via schemas.
- Sem promessas de previsão: apenas análise comparativa.
