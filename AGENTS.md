# AGENTS.md

Guidance for AI agents working in this repository.

## Project Overview

**Scuffy APP** is a small Flask web application that serves a single-page
landing page (`/`) rendered from `templates/index.html`, plus a JSON
health-check endpoint (`/health`). The UI is in Russian (`lang="ru"`).

## Repository Structure

```
main.py              # Flask app: routes / and /health
requirements.txt     # Python dependencies (flask, colorama)
templates/
  index.html         # Landing page template
static/
  style.css          # Stylesheet (Inter font, dark theme)
  scuffy_banner.png  # Banner image
.gitignore           # Ignores data.env
```

## Commands

### Install dependencies

```bash
pip install -r requirements.txt
```

Dependencies: `flask`, `colorama` (see `requirements.txt`).

> TODO: `colorama` is declared in `requirements.txt` but is not imported
> anywhere in the code. Confirm it is still needed or remove it.

### Run the development server

```bash
python main.py
# Override the default port (5000) via the PORT env var:
PORT=8080 python main.py
```

Starts Flask on `0.0.0.0` with the port from the `PORT` env var
(default **5000**), debug mode enabled.

### Health check

```bash
curl http://localhost:5000/health
```

Returns `{"status": "ok"}` with HTTP 200 (verified).

## Environment Variables

| Variable | Default | Description                       |
| -------- | ------- | --------------------------------- |
| `PORT`   | `5000`  | Port the Flask server listens on. |

> `data.env` is gitignored and intended to hold secrets or environment
> configuration. It is not committed to the repository.

## Routes

| Route     | Method | Description                        |
| --------- | ------ | ---------------------------------- |
| `/`       | GET    | Renders `index.html` landing page. |
| `/health` | GET    | JSON health-check endpoint.        |

## Lint / Typecheck / Tests

<!-- TODO: No linter, type checker, or test suite is currently configured.
     Add tooling (e.g. ruff, pytest) and document the commands here. -->

No lint, typecheck, or test commands are configured in this repository.

## Notes

- The app runs Flask in debug mode (`debug=True`); this should not be used in
  production.
- Template rendering uses Flask's `url_for('static', ...)` to reference CSS
  and images.
- The banner image links to `https://t.me/makescuffy`.
- The external Inter font is loaded from `rsms.me/inter.css`, but the
  stylesheet `<link>` href in `templates/index.html` (line 10) is malformed:
  `https://rsms.meinter/inter.css` — likely intended to be
  `https://rsms.me/inter/inter.css`. The `<link rel="preconnect">` on line 9
  correctly references `https://rsms.me`.

## TODO

- [ ] Add a `Dockerfile` or containerisation config if deployment requires it.
- [ ] Document production WSGI server setup (e.g. gunicorn).
- [ ] Add CI/CD pipeline configuration if needed.
