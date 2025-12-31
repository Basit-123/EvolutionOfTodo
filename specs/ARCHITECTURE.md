# Technical Specification: The Evolution of Todo

## 1. Project Overview
"The Evolution of Todo" is a 5-phase journey from a simple CLI application to a distributed, AI-powered, cloud-native system. It demonstrates the power of Spec-Driven Development (SDD) using the Agentic Dev Stack.

### Phase Summary
- **Phase I**: In-memory Python CLI (UV, Python 3.13)
- **Phase II**: Full-Stack Web (Next.js 16, FastAPI, Neon DB, Better Auth)
- **Phase III**: AI Integration (Chatbot, OpenAI Agents SDK, MCP)
- **Phase IV**: Local K8s (Minikube, Helm, AIOps)
- **Phase V**: Enterprise Cloud (DOKS, Kafka, Dapr)

## 2. Tech Stack Final Decisions
| Component | Technology | Version |
| :--- | :--- | :--- |
| **Language (Backend)** | Python | 3.13+ |
| **Language (Frontend)** | TypeScript | 5.x+ |
| **Backend Framework** | FastAPI | Recent Stable |
| **Frontend Framework** | Next.js | 16+ (App Router) |
| **Database** | PostgreSQL (Neon) | Serverless |
| **ORM** | SQLModel | Recent Stable |
| **Authentication** | Better Auth | Recent Stable |
| **AI SDK** | OpenAI Agents SDK | Recent Stable |
| **Event Bus** | Apache Kafka | Latest |
| **Distributed Runtime**| Dapr | Latest |
| **Infrastructure** | Docker, K8s, Helm | Latest |

## 3. Database Schema (SQLModel)
```python
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TodoStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    email: str = Field(index=True, unique=True)
    name: str
    todos: List["Todo"] = Relationship(back_populates="user")

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="user.id")
    title: str
    description: Optional[str] = None
    status: TodoStatus = Field(default=TodoStatus.PENDING)
    priority: Priority = Field(default=Priority.MEDIUM)
    due_date: Optional[datetime] = None
    tags: List[str] = Field(default=[], sa_column=Column(JSON))
    recurring_rule: Optional[str] = None # iCal RRULE format

    user: User = Relationship(back_populates="todos")
```

## 4. Monorepo Structure
```text
/
├── apps/
│   ├── web/                # Next.js Frontend
│   ├── api/                # FastAPI Backend
│   ├── chatbot/            # AI Agent Service
│   └── cli/                # Phase I Console App
├── packages/
│   ├── core/               # Shared logic & types
│   └── ui/                 # Shared shadcn/ui components
├── specs/
│   ├── phase-1-cli.md
│   ├── phase-2-web.md
│   └── ... (specs history)
├── blueprints/             # Helm charts, K8s manifests
├── scripts/                # Dev orchestration
├── CONSTITUTION.md         # Project governance
└── CLAUDE.md               # Claude-specific instructions
```

## 5. API Routes (Phase II+)
- `POST /auth/register`: Register user
- `POST /auth/login`: Login & get JWT
- `GET /todos`: List todos (Filter: priority, status, search)
- `POST /todos`: Create todo
- `PATCH /todos/{id}`: Update todo
- `DELETE /todos/{id}`: Delete todo
- `POST /todos/{id}/toggle`: Toggle completion

## 6. AI Chatbot Flow
The chatbot integrates via MCP (Model Context Protocol) to interact with the Todo API.
1. **User Prompt**: "Set a meeting for tomorrow at 10 AM"
2. **OpenAI Agent SDK**: Parses intent, extract entities (title: "Meeting", date: "tomorrow").
3. **MCP Tool Call**: Calls `create_todo` tool.
4. **FastAPI**: Validates JWT from Bot-as-User, writes to Neon DB.
5. **Response**: Bot confirms in Urdu/English (bonus logic).

## 7. Deployment Blueprints (Phase IV/V)
- **Helm Charts**: One for each service (`api`, `web`, `chatbot`).
- **Kafka**: Managed by Dapr components for event publishing on todo completion.
- **Monitoring**: Prometheus/Grafana (Blueprints).

## 8. Bonuses Implementation
- **Urdu/Multi-language**: Use System Prompts in OpenAI Agents for multilingual support.
- **Voice**: Web Speech API for frontend capture.
- **Subagents**: Custom Claude Code instructions for specialized tasks (e.g., `gen-schema`).
