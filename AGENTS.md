# AGENTS.md

Guidance for AI agents working in this repository.

## Project Overview

scuffy-app is a small Flask web application. It serves a single page (`/`)
rendered from `templates/index.html` with static assets in `static/`, plus a
JSON health-check endpoint (`/health`).

## Commands

### Install dependencies

```bash
pip install -r requirements.txt
```

Dependencies: `flask`, `colorama` (see `requirements.txt`).

### Run the app

```bash
python main.py
```

Starts the Flask development server bound to `0.0.0.0` with `debug=True`.
The port is read from the `PORT` environment variable (default `5000`).

### Health check

```bash
curl http://localhost:5000/health
```

Returns `{"status": "ok"}` with HTTP 200.

## Environment Variables

| Variable | Default | Description                                |
| -------- | ------- | ------------------------------------------ |
| `PORT`   | `5000`  | Port the Flask server listens on.          |

> Note: `data.env` is gitignored and intended to hold secrets/environment
> configuration. It is not committed to the repository.

## Project Structure

```
main.py              # Flask app: routes / and /health
requirements.txt     # Python dependencies
templates/
  index.html         # Main page template
static/
  style.css          # Stylesheet
  scuffy_banner.png  # Banner image
.gitignore           # Ignores data.env
```

## Lint / Typecheck / Tests

<!-- TODO: No linter, type checker, or test suite is currently configured.
     Add tooling (e.g. flake8/ruff, pytest) and document the commands here. -->

No lint, typecheck, or test commands are configured in this repository.

## Notes

- The app runs Flask in debug mode (`debug=True`); this should not be used in
  production.
- The UI is Russian-language (`lang="ru"`); HTML comments are in Russian.
