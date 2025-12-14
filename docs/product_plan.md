# Product Plan — MCAT Access Platform

## Product Goal
Deliver a web-based, full-stack platform that generates and adapts MCAT study plans based on:
- user-owned resources
- time availability
- real-life commitments
- performance data

---

## Core Systems

The platform consists of six tightly integrated systems.

---

## 1. User Onboarding & Context

### User Inputs
- MCAT test date
- weekly study availability
- fixed commitments (classes, work, etc.)
- prep resources owned
- preferred resources per section
- optional diagnostic strengths/weaknesses

### Output
A personalized study context that drives planning and recommendations.

---

## 2. Topic & Resource Intelligence Layer

### Canonical Topic Taxonomy
- MCAT sections → topics → subtopics
- yield weighting per topic

### Resource Mapping
- book chapters
- videos
- practice templates
- flashcards

Only metadata is stored — no copyrighted content.

---

## 3. Resource Library (Bring Your Own Content)

Users can add:
- Kaplan chapters
- Jack Westin daily passages
- Blueprint videos
- Khan Academy links
- YouTube videos
- PDFs or personal notes

Each resource includes:
- topic tags
- section
- estimated time
- usage notes

Resources become reusable planning components.

---

## 4. Study Plan Generator

### Inputs
- test date
- weekly hours
- busy blocks
- resource preferences
- topic priorities

### Outputs
- weekly plans
- daily study tasks
- content → practice → review sequencing

Plans can be regenerated at any time.

---

## 5. Scheduling & Drag-and-Drop Adjustment

### Features
- weekly board view
- drag tasks between days
- reorder tasks within a day
- “move missed tasks to tomorrow”
- optional auto-reschedule

Plans are designed to survive real life.

---

## 6. Practice, Analytics & Recommendations

### Practice
- question attempts
- flashcards (including Anki imports)
- review tracking

### Analytics
- accuracy by topic and section
- time spent vs improvement
- trend analysis

### Recommendations
Explainable priority scoring based on:
- performance
- recency
- topic importance

The system provides clear next steps.

---

## MVP Scope (3-Week Build)

### Included
- onboarding & auth
- resource library
- topic taxonomy
- study plan generation
- weekly plan UI
- drag-and-drop rescheduling
- practice tracking
- analytics dashboard
- recommendation engine
- deployment with demo data

### Explicitly Excluded
- full-length exams
- proprietary content redistribution
- AI tutoring
- external scraping
- native mobile apps

---

## Ethical & Legal Boundaries

- no copyrighted content stored
- no score guarantees
- synthetic or user-provided data only
- transparent limitations documented

---

## Long-Term Extensions (Optional)

- Google Calendar import
- deeper Anki syncing
- public resource templates
- mentor Q&A
- offline-first PWA
- advanced spaced repetition models

---

## Success Criteria

The product is successful if users can:
- build a plan using their own materials
- adjust when they fall behind
- understand *why* something is scheduled
- feel supported rather than overwhelmed

---
