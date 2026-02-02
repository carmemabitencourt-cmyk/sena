# Motor probabilístico de geração de jogos (Monte Carlo)

Este repositório contém um motor probabilístico para geração de jogos baseado em simulação Monte Carlo, exposto por uma API HTTP. O motor oferece **métricas comparativas** e **não faz previsões**: o objetivo é explorar cenários possíveis, respeitando limites estatísticos e éticos.

## Como rodar localmente

1. Crie um ambiente virtual e instale dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copie o arquivo de exemplo de variáveis:

```bash
cp .env.example .env
```

3. Suba a API:

```bash
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
```

## Variáveis de ambiente

- `PORT`: porta do serviço.
- `ENGINE_MAX_SIMULATION_SIZE`: limite superior para simulações.
- `ENGINE_DEFAULT_PROFILE`: perfil padrão (explorador | balanceado | estatistico).

Veja `.env.example` para referência.

## Deploy no Railway

1. Crie um novo projeto no Railway e conecte este repositório.
2. Certifique-se de definir `PORT` nas variáveis do projeto.
3. O Railway usa `railway.toml` para build e deploy. O comando de inicialização é:

```bash
uvicorn api.app:app --host 0.0.0.0 --port $PORT
```

## Estrutura do projeto

- `engine/`: domínio e motor de simulação.
- `api/`: camada HTTP (FastAPI), com controllers, rotas e schemas.
- `docs/`: documentação técnica e limites éticos.
- `tests/`: testes iniciais.

## Observações importantes

Este motor **não promete acerto**, **não prevê resultados** e o score é **apenas comparativo**. Os textos e o código refletem essas limitações.
