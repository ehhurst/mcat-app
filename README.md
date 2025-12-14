# MCAT Access Platform

A mission-driven, full-stack web platform designed to help **low-income and underrepresented premedical students** prepare for the MCAT through personalized study planning, free practice questions, and data-driven feedback.

This project focuses on **equity in the medical pipeline**, leveraging modern software engineering practices to reduce barriers to entry for students pursuing careers in healthcare.

---

## Motivation

Preparing for the MCAT is expensive and time-consuming, with many students priced out of traditional prep resources. This platform aims to provide:

- Free, high-quality practice content
- Personalized study plans tailored to individual constraints
- Analytics-driven recommendations to help students study efficiently
- An accessible, mobile-friendly experience designed for low-resource environments

---

## Features

### Personalized Study Planning
- Generate study schedules based on:
  - Target MCAT date
  - Weekly availability
  - Section-level strengths and weaknesses
- Prioritizes high-impact topics under time constraints

### Practice Question Bank
- Original MCAT-style practice questions
- Tagged by section, topic, and difficulty
- Detailed explanations after submission

### Progress & Analytics Dashboard
- Accuracy by section and topic
- Time-on-task vs. performance insights
- Visual trend analysis to track improvement over time

### Smart Recommendations Engine
- Suggests “what to study next” using:
  - Accuracy decay
  - Time since last review
  - Topic importance weighting
- Fully explainable and tunable scoring model

### Accessibility & Equity-First Design
- Mobile-first UI
- Dark mode
- Low-bandwidth friendly
- Screen-reader aware components
- No paywalls for core features

---

## Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | React, TypeScript, Vite, TailwindCSS |
| Backend | FastAPI (Python 3.11) |
| Database | PostgreSQL |
| Auth | JWT (Access + Refresh Tokens) |
| Analytics | Pandas, SQL |
| Charts | Recharts / Chart.js |
| DevOps | Docker, GitHub Actions |
| Deployment | Fly.io / Railway |

---

## Architecture Overview
frontend/ # React + TypeScript client
backend/ # FastAPI application
├── api/ # Route definitions
├── models/ # SQLAlchemy ORM models
├── schemas/ # Pydantic request/response schemas
├── services/ # Business logic (planning, recommendations)
├── core/ # Auth, config, dependencies
├── tests/ # Unit & integration tests
└── main.py
docker-compose.yml


---

## ⚙️ Getting Started (Local Development)

### Prerequisites
- Docker & Docker Compose
- Node.js (18+)
- Python 3.11+

### Clone the Repository
```bash
git clone https://github.com/ehhurst/mcat-app.git
cd mcat-app
```
Environment Variables

Create a .env file:
```
DATABASE_URL=postgresql+psycopg://user:pass@db:5432/mcat
JWT_SECRET=dev_secret_key
JWT_EXPIRE_MIN=15
REFRESH_EXPIRE_MIN=43200
APP_ENV=dev
```
### Run the app
```
docker compose up --build
```

### Testing
Backend
```
docker compose exec api pytest
```

Frontend
```
cd frontend
npm test
```

End-to-End (optional)
```
npm run e2e
```

## Security & Data Ethics

Passwords are securely hashed (argon2/bcrypt)

JWT-based authentication with role-based access control

Uses synthetic data only

Not HIPAA-compliant (educational/portfolio project)

Future work would include encryption at rest, audit trails, and compliance workflows.

 
## Documentation:
- [Product Vision](docs/product-vision.md)
- [Product Plan](docs/product-plan.md)

