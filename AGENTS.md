# AGENTS.md

Guidance for AI agents working with this repository.

## Project Overview

**Scuffy APP** — a Flask web application serving a single-page landing page with a Telegram link and a balance display. The UI is in Russian.

## Repository Structure

```
.
├── main.py              # Flask app (routes: /, /health)
├── requirements.txt     # Python dependencies
├── static/
│   ├── style.css        # Main stylesheet (Inter font, dark theme)
│   └── scuffy_banner.png
├── templates/
│   └── index.html       # Landing page template
└── .gitignore           # Ignores data.env
```

## Commands

### Install dependencies

```bash
pip install -r requirements.txt
```

Dependencies: `colorama`, `flask`

### Run the development server

```bash
python main.py
# Override the default port (5000) via the PORT env var:
PORT=8080 python main.py
```

Starts Flask on `0.0.0.0` with the port from the `PORT` env var (default **5000**), debug mode enabled.

### Health check

```bash
curl http://localhost:5000/health
```

Returns `{"status": "ok"}` with HTTP 200.

## Routes

| Route   | Method | Description                     |
|---------|--------|---------------------------------|
| `/`     | GET    | Renders `index.html` landing page |
| `/health` | GET  | JSON health-check endpoint      |

## Key Details

- **Template rendering**: uses Flask's `url_for('static', ...)` to reference CSS and images.
- **External font**: loads Inter from `rsms.me/inter.css`.
- **Telegram link**: the banner image links to `https://t.me/makescuffy`.
- **`.gitignore`**: only `data.env` is ignored — no other secrets or build artifacts are excluded.

## TODO

- [ ] Add a `Dockerfile` or containerisation config if deployment requires it.
- [ ] Document production WSGI server setup (e.g. gunicorn) — currently uses Flask dev server.
- [ ] Add CI/CD pipeline configuration if needed.
