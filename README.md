# MCAT Platform

A full-stack web platform designed to help **low-income and underrepresented premedical students** prepare for the MCAT through personalized study planning, free practice questions, and data-driven feedback.

This project focuses on **equity in the medical pipeline**, leveraging modern software engineering practices to reduce barriers to entry for students pursuing careers in healthcare.

### Project Board: https://github.com/ehhurst/mcat-app/projects

### Documentation:

- [Vision Statement](docs/product-vision.md)
- [Product Plan](docs/product-plan.md)
- [Requirements Doc](docs/requirements.md)
- [Requirements Tracability Matrix](docs/requirements-tracability-matrix.md)
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

```text
client/                     # React + TypeScript client
├── node_modules/
├── public/
├── src/
└── Dockerfile

docs/
├── product-plan.md
├── product-vision.md
├── requirements.md
└── requirements-tracability-matrix.md

server/                     # FastAPI application
├── Dockerfile
├── requirements.txt
├── alembic.ini
├── Alembic/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/                # Route definitions
│   ├── core/               # Auth, config, dependencies
│   ├── db/
│   ├── models/             # SQLAlchemy ORM models
│   ├── schemas/            # Pydantic request/response schemas
│   ├── services/           # Business logic (planning, recommendations)
│   └── utils/
└── tests/                  # Unit & integration tests

docker-compose.yml
.env.example
.gitignore
LICENSE
README.md
```


## Security & Data Ethics

- Passwords are securely hashed (argon2/bcrypt)
- JWT-based authentication with role-based access control
- Uses synthetic data only
- Not HIPAA-compliant (educational/portfolio project)

---
## Getting Started (Local Development)

This project uses Docker Compose to provide a consistent local development environment.

Make sure you have the following installed:
- Docker Desktop
- Docker Compose (included with Docker Desktop)
- Git


### 1. Clone the repository

```
git clone https://github.com/ehhurst/mcat-app.git
```
```
cd mcat-app
```


### 2. Environment variables

This project uses environment variables for configuration.
Copy the example environment file:

```
cp .env.example .env
```

Update values in .env if needed (defaults work for local development).

### 3. Start the development environment

From the repository root, run:

```
docker compose up --build
```
or
```
docker compose up --build -d
```

This will start:
* PostgreSQL database
* FastAPI server
* React (Vite) client

The first build may take a few minutes.


### 4. Access the application

Once running:
- Client: http://localhost:5173
- Server API: http://localhost:8000
- Server health check: http://localhost:8000/healthcheck
- API version ping: http://localhost:8000/api/v1/ping

If all services are running, you should see JSON responses from the health and ping endpoints.

### 5. Running tests
Tests are executed inside the server container.

After starting the Docker container as per above, run:

#### Server Tests:
```
docker compose exec server pytest
```

Expected output:
```
1 passed
```

#### Client Tests:
```
cd client
npm test
```

#### End-to-End (optional):
```
npm run e2e
```


### 6. Stopping the environment

To stop the containers:

```
docker compose down
```



