FROM python:3.12-slim AS deps
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync
FROM deps AS build
COPY . .
RUN uv run manage.pyproject collectstatic --noinput
FROM build AS runner
WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]