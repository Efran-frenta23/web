#!/bin/bash
GRANIAN_WORKERS=$(nproc --all) uv run granian shoppinglist.asgi:application --host 0.0.0.0 --interface asgi