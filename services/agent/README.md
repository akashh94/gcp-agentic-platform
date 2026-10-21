# agent

A minimal [ADK](https://adk.dev/) agent in Python, following the official
[ADK Python quickstart](https://adk.dev/get-started/python/).

The agent is defined in [`agent.py`](./agent.py) as `root_agent`, and
[`__init__.py`](./__init__.py) re-exports it so the ADK tooling discovers the
package.

```
services/agent/
├── __init__.py       # re-exports root_agent
├── agent.py          # the agent (root_agent)
├── requirements.txt
└── .env.example
```

## Prerequisites

- Python 3.10+

## Setup

```bash
cd services/agent
python -m venv .venv
.venv\Scripts\activate          # Windows (cmd/PowerShell)
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
cp .env.example .env            # then fill in your key
```

## Run

Run from `services/` (the parent directory of `agent/`):

```bash
cd ..                           # services/
adk run agent                   # interactive CLI
adk web --port 8000             # web UI at http://localhost:8000
```

> ADK Web is for development only — not for production deployments.

## Notes

This service is Python while the rest of the monorepo is Node/pnpm, so it is not
part of the Nx task graph. Install and run it with `pip`/`venv` as shown above.
