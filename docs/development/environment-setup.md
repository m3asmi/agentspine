# Environment Setup

This document is the authoritative install guide for the local development environment.
Update it whenever a new service, tool, or credential is added.

---

## Prerequisites

| Tool | Required version | Install |
|------|-----------------|---------|
| Python | 3.12.13 | via `pyenv` or system |
| uv | latest | `curl -Ls https://astral.sh/uv/install.sh \| sh` |
| PostgreSQL | 15+ | system package |
| pgvector | matching pg version | see below |
| Ollama | latest | `curl -fsSL https://ollama.ai/install.sh \| sh` |
| Langfuse | v3 (self-hosted) | see below |

---

## 1. Python environment

The project uses `uv` with a pinned Python version.

```bash
# Install dependencies (creates .venv automatically)
uv sync

# Verify
uv run python --version   # should print 3.12.x
uv run pytest             # should pass
```

`.python-version` pins to `3.12.13`. Do not change this without updating `pyproject.toml`.

---

## 2. PostgreSQL

### Status (local)

PostgreSQL is running on `localhost:5432`. The superuser is `rachid` (no password for local connections — trust auth).

### Create the project database

```bash
psql -h localhost -U rachid -c "CREATE DATABASE agent_framework;"
```

Database `agent_framework` was created on 2026-03-15.

### pgvector

pgvector is **not yet installed** on this machine. It must be installed before running migrations.

```bash
# Ubuntu/Debian — match your PostgreSQL major version (this machine runs PG 18)
sudo apt install postgresql-18-pgvector

# Then enable the extension in the project database
psql -h localhost -U rachid -d agent_framework -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

Extension is installed and enabled as of 2026-03-15.

---

## 3. Ollama

### Status (local)

Ollama is running on `http://localhost:11434`. Available models:

| Model | Use |
|-------|-----|
| `qwen3:8b` | default / plan agent |
| `qwen2.5-coder:14b` | build agent |
| `qwen2.5:14b` | general |
| `nomic-embed-text:latest` | embeddings |
| `private-assistant:latest` | personal |

### Pull required models

```bash
ollama pull qwen3:8b
ollama pull qwen2.5-coder:14b
ollama pull nomic-embed-text:latest
```

---

## 4. Langfuse

### Status

Using **Langfuse Cloud** (free tier) at `https://cloud.langfuse.com`. No local install needed.
Connection verified: `auth_check: True` on 2026-03-15.

### Setup (already done)

1. Created account at https://cloud.langfuse.com
2. Created project `agent-framework`
3. Generated API key pair → copied into `.env` as `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY`

### Add new keys

Go to **cloud.langfuse.com → project → Settings → API Keys → Create new API key**.

> **SDK env var**: the Langfuse Python SDK reads `LANGFUSE_HOST` (not `LANGFUSE_BASE_URL`).
> Always use `LANGFUSE_HOST=https://cloud.langfuse.com` in `.env`.

---

## 5. Telegram

A Telegram bot token is required for the channel integration (Phase 1+). It is **not needed for Phase 0**.

```bash
# 1. Open Telegram, search for @BotFather
# 2. Send /newbot and follow prompts
# 3. Copy the token — paste into .env as TELEGRAM_BOT_TOKEN
```

For `TELEGRAM_WEBHOOK_SECRET`, generate any random string:

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

---

## 6. Odoo (optional — Phase 2+)

Not required until Phase 2. When ready, configure against the local `odoo19_ma` instance.

```
ODOO_BASE_URL=http://localhost:8069
ODOO_DATABASE=odoo19_ma
ODOO_LOGIN=<your odoo login>
ODOO_API_KEY=<generate from Odoo Settings > Technical > API Keys>
```

---

## 7. .env file

Copy the example and fill in values:

```bash
cp .env.example .env
```

Pre-filled values for this machine (safe to copy as-is for Phase 0):

```dotenv
# Database — pre-created 2026-03-15
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=agent_framework
POSTGRES_USER=rachid
POSTGRES_PASSWORD=

# Langfuse — fill after setting up (see section 4)
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_HOST=https://cloud.langfuse.com

# Ollama — running locally
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=qwen3:8b

# OpenAI-compatible remote fallback — optional, leave blank to use Ollama only
OPENAI_BASE_URL=
OPENAI_API_KEY=
OPENAI_MODEL=

# Telegram — not needed until Phase 1
TELEGRAM_BOT_TOKEN=
TELEGRAM_WEBHOOK_SECRET=

# Odoo — not needed until Phase 2
ODOO_BASE_URL=
ODOO_DATABASE=
ODOO_API_KEY=
ODOO_LOGIN=
```

> `POSTGRES_PASSWORD` is empty because local trust auth is used. If you change pg auth mode, set a real password here.

---

## 8. Phase readiness checklist

| Service | Status | Needed from |
|---------|--------|-------------|
| Python 3.12 + uv | ✅ ready | Phase 0 |
| PostgreSQL | ✅ running, DB created | Phase 0 |
| pgvector extension | ✅ installed | Phase 0 exit gate |
| Ollama + models | ✅ running | Phase 0 |
| Langfuse Cloud | ✅ connected | Phase 0 (observability) |
| Telegram bot token | ❌ pending | Phase 1 |
| Odoo connection | ❌ pending | Phase 2 |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-03-15 | Initial setup. Created `agent_framework` DB. Documented pgvector blocker and Langfuse gap. |
| 2026-03-15 | Langfuse Cloud configured and connection verified (`auth_check: True`). Fixed SDK env var: `LANGFUSE_HOST`. |
| 2026-03-15 | Installed `postgresql-18-pgvector`. Enabled `vector` extension in `agent_framework` database. |
