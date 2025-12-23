FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project --no-cache

FROM python:3.12-slim
WORKDIR /app

RUN useradd -m appuser && chown -R appuser /app

COPY --from=builder /app/.venv /app/.venv

COPY lab4/app/main.py ./main.py

USER appuser
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
