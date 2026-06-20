# 🚀 FastAPI Journey — Developer → AI Engineer

> Tracking my path from full-stack dev (PERN) to AI Engineer, backend layer first.
> Coach: **Cipher** | Stack target: **Python + FastAPI + PostgreSQL + Docker**

---

## 📺 Primary Course

| Field | Detail |
|---|---|
| **Course** | FastAPI Full Course |
| **Link** | [Watch on YouTube](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=30353s) |
| **Duration** | ~19 hours |
| **Resume Timestamp** | `30353s` → **8h 25m 53s** |
| **Status** | 🟡 In Progress |

```
Progress: [█████████░░░░░░░░░░░] 44%
```

---

## 🗺️ Learning Path (Full Roadmap)

| # | Stage | Status |
|---|---|---|
| 1 | Python + Git + Linux | ✅ Done |
| 2 | Math for AI | ⬜ Pending |
| 3 | ML Fundamentals | ⬜ Pending |
| 4 | Deep Learning | ⬜ Pending |
| 5 | LLMs / RAG / Agents / Fine-tuning | ⬜ Pending |
| 6 | MLOps + Deployment | ⬜ Pending |
| 7 | End-to-End AI Systems | ⬜ Pending |
| — | **FastAPI (this repo)** | 🟡 In Progress |

---

## 📂 Repo Structure

```
fastapi-journey/
├── 01-basics/          # routing, path/query params, status codes
├── 02-pydantic/         # schemas, validation, response models
├── 03-database/         # SQLAlchemy, PostgreSQL, sessions
├── 04-auth/             # OAuth2, JWT, password hashing
├── 05-async/            # async/await, background tasks
├── 06-testing/          # pytest, TestClient
├── 07-deployment/       # Docker, Uvicorn/Gunicorn, env config
├── notes/                # per-module Cipher-style notes
└── README.md
```

---

## ✅ Module Progress Tracker

| Module | Topic | Notes Written | Project Applied |
|---|---|---|---|
| 01 | Routing & Path/Query Params | ✅ | ✅ Posts API |
| 02 | Pydantic Models & Validation | ✅ | ✅ Posts API |
| 03 | SQLAlchemy + PostgreSQL | ✅ | ✅ Posts API |
| 04 | Auth (OAuth2 + JWT) | ⬜ | ⬜ |
| 05 | Async & Background Tasks | ⬜ | ⬜ |
| 06 | Testing (pytest) | ⬜ | ⬜ |
| 07 | Docker + Deployment | 🟡 | 🟡 Portfolio backend |

---

## 🧠 Concept Notes (Cipher Format)

Each topic below follows: **Core Concept → Mental Model → Gotchas → Project Link.**

### Example: Dependency Injection (`Depends`)

| Layer | Detail |
|---|---|
| **Core Concept** | A function FastAPI calls *before* your route runs, and injects the result as an argument. |
| **Mental Model** | Think of it as middleware-per-parameter — reusable logic (DB session, current user, auth check) plugged into any route. |
| **Gotcha** | `Depends()` runs on every request — don't put heavy compute inside it without caching. |
| **Used In** | `get_db()` session injection across Posts API. |

> Add one block like this per concept as you progress — keeps notes scannable instead of a wall of text.

---

## 🛠️ Tech Stack

`Python` `FastAPI` `Pydantic` `SQLAlchemy` `PostgreSQL` `Docker` `Uvicorn` `Postman`

---

## 🚧 Projects Built Along the Way

| Project | Description | Status |
|---|---|---|
| **Posts API** | CRUD API with FastAPI + SQLAlchemy + Postman collection | ✅ Done |
| **Portfolio Backend** | rahulshakya.com FastAPI service (Docker Compose + PostgreSQL) | 🟡 Active |

---

## 🔗 Resources

- 🎥 [FastAPI Full Course (19h) — primary reference](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=30353s)
- 📖 [Official FastAPI Docs](https://fastapi.tiangolo.com/)

---

## 📌 Update Log

| Date | Update |
|---|---|
| 2026-06-20 | Repo + README initialized, resumed course at 8h25m |

---

*Last updated: June 20, 2026*
