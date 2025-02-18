FROM docker.io/python:3.12-slim AS deps
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY README.md README.md
RUN uv sync
FROM deps AS build
COPY . .
RUN uv run manage.py collectstatic --noinput
FROM build AS runner
WORKDIR /app
USER root
RUN chmod -R 755 /app
ENTRYPOINT ["/app/entrypoint.sh"]