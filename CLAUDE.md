# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`lado-dashboard`: a FastAPI web app (Python 3.12) managed with **uv**. Server-rendered HTML via Jinja2; pandas + openpyxl are available for reading/processing Excel data. Not yet a git repository.

## Commands

Always go through uv (it manages `.venv/` and `uv.lock`); don't use `pip` directly.

- Install/sync deps: `uv sync`
- Add a dependency: `uv add <pkg>` (dev-only: `uv add --dev <pkg>`)
- Dev server (auto-reload): `uv run fastapi dev src/lado_dashboard/main.py` → http://127.0.0.1:8000 (API docs at `/docs`)
- Tests: `uv run pytest`
- Single test: `uv run pytest tests/test_main.py::test_health`

## Layout

- src layout: the package is `src/lado_dashboard/`, installed into the venv by `uv sync`, so tests import it as `lado_dashboard`.
- `src/lado_dashboard/main.py` defines the `app` and routes; Jinja2 templates live in `src/lado_dashboard/templates/` (path resolved relative to `main.py`).
- Tests use `fastapi.testclient.TestClient` (needs `httpx`, a dev dependency).
- `app/main.py` is a leftover hello-world script (just a `print`) and is not part of the app; don't confuse it with `src/lado_dashboard/main.py`.

## Conventions

- The user communicates in Korean; respond in Korean.
