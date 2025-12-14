# MCAT Platform

A mission-driven, full-stack web platform designed to help **low-income and underrepresented premedical students** prepare for the MCAT through personalized study planning, free practice questions, and data-driven feedback.

This project focuses on **equity in the medical pipeline**, leveraging modern software engineering practices to reduce barriers to entry for students pursuing careers in healthcare.

---

## Project Board: https://github.com/ehhurst/mcat-app/projects

## Getting Started (development)

### Prerequisites

- Docker & Docker Compose
- Node.js (18+)
- Python 3.11+

### Clone the Repository

```bash
git clone https://github.com/ehhurst/mcat-app.git
cd mcat-app
```

## Running locally

1. Copy `.env.example` to `.env` and fill values
2. Run `docker compose up --build`
3. Open http://localhost:5173

### Testing

Server

```
docker compose exec api pytest
```

Client

```
cd client
npm test
```

End-to-End (optional)

```
npm run e2e
```

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

| Layer      | Technology                           |
| ---------- | ------------------------------------ |
| Client     | React, TypeScript, Vite, TailwindCSS |
| Server     | FastAPI (Python 3.11)                |
| Database   | PostgreSQL                           |
| Auth       | JWT (Access + Refresh Tokens)        |
| Analytics  | Pandas, SQL                          |
| Charts     | Recharts / Chart.js                  |
| DevOps     | Docker, GitHub Actions               |
| Deployment | Fly.io / Railway                     |

---

## Architecture Overview

client/ # React + TypeScript client
├── node_modules/
├── public/
├── src/
└── Dockerfile
docs/
├── product-plan.md
└── product-vision.md
server/ # FastAPI application
├── Dockerfile
├── requirements.txt
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── api/# Route definitions
│ ├── core/ # Auth, config, dependencies
│ ├── db/
│ ├── models/# SQLAlchemy ORM models
│ ├── schemas/ # Pydantic request/response schemas
│ ├── services/ # Business logic (planning, recommendations)
│ └── utils/
└── tests/ # Unit & integration tests
docker-compose.yml
.gitignore
LICENSE
README.md

## Security & Data Ethics

Passwords are securely hashed (argon2/bcrypt)

JWT-based authentication with role-based access control

Uses synthetic data only

Not HIPAA-compliant (educational/portfolio project)

Future work would include encryption at rest, audit trails, and compliance workflows.

## Documentation:

- [Product Vision](docs/product-vision.md)
- [Product Plan](docs/product-plan.md)
