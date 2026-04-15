# Tech Stack Lock v1

## Runtime

- Python: 3.12.13
- Package manager: uv
- Build backend: hatchling

## Core libraries

- FastAPI
- Uvicorn
- Pydantic v2
- LangGraph
- SQLAlchemy
- Alembic
- Psycopg 3
- pgvector
- OpenAI Python SDK
- Ollama Python client
- httpx
- python-telegram-bot
- Langfuse

## Current policy

- prefer stable minor ranges
- commit `uv.lock`
- do not widen versions without test run + review
- if provider SDK behavior changes, adapt only inside `llm_gateway/`
