# gcp-agentic-platform

Monorepo for the GCP agentic platform. Node.js runtime, pnpm workspaces, Nx for
task orchestration and caching.

## Layout

```
gcp-agentic-platform/
├── apps/            # Deployable frontends
│   └── ui/          # React UI (placeholder)
├── services/        # Backend services
│   ├── bff/         # Backend-for-frontend (placeholder)
│   └── agent/       # ADK agent (Python) — see services/agent/README.md
├── nx.json          # Nx workspace config
├── pnpm-workspace.yaml
└── package.json     # Root scripts + shared dev tooling
```

Nx maps `apps/` to the workspace's `apps` and `services/` to its `libs`
directory (`workspaceLayout` in `nx.json`), so generators drop new
applications and services in the right place.

## Prerequisites

- Node.js >= 24
- pnpm 12 (pinned via `packageManager`; enable with `corepack enable pnpm`)

## Getting started

```bash
pnpm install
pnpm graph       # visualise the workspace
pnpm build       # run the build target across all projects
pnpm lint        # run lint across all projects
pnpm test        # run tests across all projects
```

## Adding projects

```bash
# React UI
pnpm nx g @nx/react:app ui --directory=apps/ui

# Node service
pnpm nx g @nx/js:lib bff --directory=services/bff

# Agent service
pnpm nx g @nx/js:lib agent --directory=services/agent
```
