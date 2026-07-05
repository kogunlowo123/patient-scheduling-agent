# Patient Scheduling Agent

[![CI](https://github.com/kogunlowo123/patient-scheduling-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/patient-scheduling-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Healthcare | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Patient scheduling agent that manages appointment bookings, optimizes provider schedules, handles cancellations and waitlists, sends appointment reminders, and reduces no-show rates.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `find_available_slots` | Find available appointment slots for a provider or specialty |
| `book_appointment` | Book a patient appointment with a provider |
| `manage_waitlist` | Add patient to waitlist and notify on availability |
| `send_reminder` | Send appointment reminder via SMS, email, or phone |
| `optimize_schedule` | Optimize provider schedule for utilization and patient access |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/patient-scheduling/process` | Process request |
| `POST` | `/api/v1/patient-scheduling/query` | Query data |
| `POST` | `/api/v1/patient-scheduling/validate` | Validate |
| `POST` | `/api/v1/patient-scheduling/report` | Generate report |
| `GET` | `/api/v1/patient-scheduling/audit` | Get audit trail |

## Features

- Patient
- Scheduling
- Compliance
- Interoperability

## Integrations

- Epic Ehr
- Cerner Ehr
- Allscripts
- Fhir Server
- Clearinghouse

## Architecture

```
patient-scheduling-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── patient_scheduling_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**EHR + Healthcare Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
