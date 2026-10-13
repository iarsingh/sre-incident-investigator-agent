# AI SRE Incident Investigator

## Overview

An agent lab for incident root cause analysis. Given an alert, it gathers evidence from logs, metrics, git history and Kubernetes state, checks previous incidents, and returns an RCA through `POST /agent/run`. Actions that need a human, such as paging someone or rebooting, are refused, and cluster apply stays false until a person approves. A `/v1` ops API adds workspaces, tenant isolation, job approval and audit records.

- **Built with:** Python, pytest, GitHub Actions
- **Scope:** Laptop proof with tests; no hosted model, and production apply is refused.

<!-- project-guide:start -->
## Project guide

[Project architecture](PROJECT_ARCHITECTURE.md) · [Interview questions and answers](INTERVIEW_QA.md)

Use the architecture document for the component diagram, implementation boundaries, and verification entry points. The interview guide includes source-backed answers and project walkthroughs.

### Implementation map

| Component | Responsibility |
| --- | --- |
| [`src/agentx/main.py`](src/agentx/main.py) | HTTP handlers: `GET /healthz`, `POST /agent/run` |
| [`src/agentx/agent.py`](src/agentx/agent.py) | Functions: `run` |
| [`requirements.txt`](requirements.txt) | Implementation or supporting configuration |
| [`tests/test_agent.py`](tests/test_agent.py) | Executable checks and regression examples |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | GitHub Actions job definitions |
| [`README.md`](README.md) | Project explanations or operating notes |

### Local setup and verification

From the repository root (the commands follow the checked-in manifests):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

To serve the FastAPI application locally, install the server separately if it is not already available:

```bash
python -m pip install uvicorn
PYTHONPATH=src python -m uvicorn agentx.main:app --reload
```

<!-- project-guide:end -->

Phase 6

Skills: alerts, logs, metrics, git, k8s, previous incidents, approval

Alert → SRE agent → logs/metrics/git/k8s → previous incidents → RCA. Remediation needs human language avoided (page/reboot refused).

```bash
pip install -r requirements.txt
pytest -q
```

Laptop proof. No hosted model. Cluster apply stays false until a human approves.

## Ops plane

Workspaces, tenant isolation, job approval, and audit live under `/v1`. Production apply is refused. See `docs/ARCHITECTURE.md`.

## Documentation checks

Project architecture, interview guides, and local source links are checked automatically on pushes and pull requests. Run the same check locally:

```bash
python3 .github/scripts/validate_project_docs.py
```

See [service improvements and local run instructions](docs/UPGRADES.md).
