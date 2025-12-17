# Requirements Tracability Matrix (RTM)

---

## 1. Functional Requirements Traceability

| Req ID | Requirement Summary             | GitHub Issue(s)                              | Sprint   | Complete? |
| ------ | ------------------------------- | -------------------------------------------- | -------- | --------- |
| FR-1   | User registration               | Backend: Authentication (JWT access/refresh) | Sprint 1 | [ ]       |
| FR-2   | User login/logout               | Backend: Authentication (JWT access/refresh) | Sprint 1 | [ ]       |
| FR-3   | Password hashing                | Backend: Authentication (JWT access/refresh) | Sprint 1 | [ ]       |
| FR-4   | JWT access + refresh tokens     | Backend: Authentication (JWT access/refresh) | Sprint 1 | [ ]       |
| FR-5   | Protected API endpoints         | Backend: Authentication (JWT access/refresh) | Sprint 1 | [ ]       |
| FR-6   | Add custom study resources      | Client: Custom study resources integration   | Sprint 2 | [ ]       |
| FR-7   | Resource-agnostic support       | Client: Custom study resources integration   | Sprint 2 | [ ]       |
| FR-8   | Tag resources by topic          | Client: Custom study resources integration   | Sprint 2 | [ ]       |
| FR-9   | Edit/remove resources           | Client: Custom study resources integration   | Sprint 2 | [ ]       |
| FR-10  | Generate study plan from inputs | Backend: Study planning engine               | Sprint 1 | [ ]       |
| FR-11  | Deterministic planning output   | Backend: Study planning engine               | Sprint 1 | [ ]       |
| FR-12  | Persist study plans             | Backend: Database models and migrations      | Sprint 1 | [ ]       |
| FR-13  | Plan consists of tasks          | Backend: Database models and migrations      | Sprint 1 | [ ]       |
| FR-14  | Calendar / schedule view        | Client: Study planner UI with drag-and-drop  | Sprint 2 | [ ]       |
| FR-15  | Drag-and-drop task rescheduling | Client: Study planner UI with drag-and-drop  | Sprint 2 | [ ]       |
| FR-16  | Persist rescheduled tasks       | Client: Study planner UI with drag-and-drop  | Sprint 2 | [ ]       |
| FR-17  | Reschedule missed tasks         | Client: Study planner UI with drag-and-drop  | Sprint 2 | [ ]       |
| FR-18  | Client retrieves plans via API  | Client: Study planner UI with drag-and-drop  | Sprint 2 | [ ]       |
| FR-19  | Client updates plans via API    | Client: Study planner UI with drag-and-drop  | Sprint 2 | [ ]       |
| FR-20  | Graceful API error handling     | Client: Study planner UI with drag-and-drop  | Sprint 2 | [ ]       |

---

## 2. Non-Functional Requirements Traceability

| Req ID | Requirement Summary           | GitHub Issue(s)                                             | Sprint   | Complete? |
| ------ | ----------------------------- | ----------------------------------------------------------- | -------- | --------- |
| NFR-1  | Simple, focused UI            | Client: Study planner UI with drag-and-drop                 | Sprint 2 | [ ]       |
| NFR-2  | Minimal clicks for workflows  | Client: Study planner UI with drag-and-drop                 | Sprint 2 | [ ]       |
| NFR-3  | Laptop-friendly layout        | Client: Study planner UI with drag-and-drop                 | Sprint 2 | [ ]       |
| NFR-4  | Reasonable API response times | Sprint 0 Day 2: Health checks and configuration wiring      | Sprint 0 | [ ]       |
| NFR-5  | Responsive drag-and-drop      | Client: Study planner UI with drag-and-drop                 | Sprint 2 | [ ]       |
| NFR-6  | No plaintext passwords        | Backend: Authentication (JWT access/refresh)                | Sprint 1 | [ ]       |
| NFR-7  | Secure token generation       | Backend: Authentication (JWT access/refresh)                | Sprint 1 | [ ]       |
| NFR-8  | Secrets not committed         | Sprint 0 Day 0: Repo scaffold and documentation             | Sprint 0 | [ ]       |
| NFR-9  | Modular server architecture   | Sprint 1 Day 0: Server project structure                    | Sprint 1 | [ ]       |
| NFR-10 | DB migrations supported       | Backend: Database models and migrations                     | Sprint 1 | [ ]       |
| NFR-11 | Automated tests exist         | Sprint 0 Day 3: Test scaffolding and Alembic initialization | Sprint 0 | [ ]       |
| NFR-12 | One-command local startup     | Sprint 0 Day 1: Docker Compose dev environment              | Sprint 0 | [ ]       |
| NFR-13 | Service health checks         | Sprint 0 Day 2: Health checks and configuration wiring      | Sprint 0 | [ ]       |
| NFR-14 | Clear setup documentation     | Docs: Final README and architecture overview                | Sprint 3 | [ ]       |

---

## 3. Sprint Coverage Summary

| Sprint   | Covered Requirement Areas                               | Complete? |
| -------- | ------------------------------------------------------- | --------- |
| Sprint 0 | Infrastructure, config, health, dev experience          | [ ]       |
| Sprint 1 | Data models, migrations, authentication, planning logic | [ ]       |
| Sprint 2 | Client UI, scheduling UX, integration                   | [ ]       |
| Sprint 3 | CI, documentation, polish                               | [ ]       |
