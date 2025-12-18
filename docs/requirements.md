# MCAT Access Platform
## Software Requirements Document (SRD)

#### Project Name: MCAT Platform
#### Repository: ehhurst/mcat-app
#### Document Version: 1.0
#### Last Updated: (today)

## 1. Purpose
The purpose of the MCAT Access Platform is to provide low-income and underrepresented premedical students with a flexible, resource-agnostic study planning system that helps them prepare for the MCAT using materials they already have access to.

The platform focuses on:
- personalized study planning
- schedule flexibility
- integration of user-chosen study resources
- reducing reliance on expensive, rigid prep programs

This document defines the functional and non-functional requirements for the system.


## 2. Scope
In Scope:
- Web-based client application
- Server-side API and business logic
- User authentication and persistence
- Study plan generation and modification
- Custom resource integration
- Drag-and-drop schedule management

Out of Scope (for initial releases):
- Native mobile applications
- Payment processing
- Partnerships with prep companies
- Automated content scraping from proprietary platforms


## 3. Users & Personas
* 3.1 Primary User: MCAT Student
   - Preparing for the MCAT
   - Often balancing school, work, family, or caregiving responsibilities
   - Uses a mix of free and paid resources (e.g., Kaplan books, Jack Westin, Blueprint videos, Anki)
   - Needs flexibility when plans change

* 3.2 Secondary User: Developer / Contributor
   - Runs the system locally
   - Contributes features or fixes
   - Needs clear setup, testing, and documentation


## 4. System Architecture Overview
The system follows a client–server architecture:
   * Client: React + TypeScript web application
   * Server: FastAPI (Python) REST API
   * Database: PostgreSQL
   * Infrastructure: Docker Compose for local development

All components must be runnable locally with a single command.

## 5. Functional Requirements
* 5.1 User Accounts & Authentication
   - FR-1 The system shall allow users to register with email and password.
   - FR-2 The system shall allow users to log in and log out securely.
   - FR-3 The system shall use hashed passwords and JWT-based authentication.
   - FR-4 The system shall support access tokens and refresh tokens.
   - FR-5 Protected endpoints shall require authentication.

* 5.2 Study Resource Management
   - FR-6 Users shall be able to add custom study resources.
   - FR-7 Resources shall be user-defined and platform-agnostic (e.g., Kaplan, Jack Westin, Blueprint, Anki).
   - FR-8 Resources shall be taggable by MCAT topic and section (e.g., CARS, Bio/Biochem).
   - FR-9 Users shall be able to edit or remove their resources.

* 5.3 Study Planning Engine
   - FR-10 The system shall generate a study plan based on:
      - MCAT exam date
      - Weekly availability
      - Selected topics
      - Selected resources
   - FR-11 Study plans shall be deterministic given the same inputs.
   - FR-12 Study plans shall be stored persistently.
   - FR-13 Plans shall consist of individual scheduled study tasks.

5.4 Scheduling & Flexibility

FR-14 Users shall be able to view their study plan in a calendar or schedule format.
FR-15 Users shall be able to drag and drop study tasks to different days.
FR-16 When a task is moved, the updated schedule shall be saved automatically.
FR-17 Users shall be able to reschedule missed tasks without regenerating the entire plan.

5.5 Client–Server Interaction

FR-18 The client shall retrieve study plans from the server via API calls.
FR-19 The client shall update study plans via authenticated API requests.
FR-20 The client shall handle API errors gracefully and display meaningful feedback.

6. Non-Functional Requirements
   6.1 Usability

NFR-1 The UI shall be simple and distraction-free.
NFR-2 Core workflows (view plan, reschedule task) shall require minimal clicks.
NFR-3 The interface shall be usable on standard laptop screen sizes.

6.2 Performance

NFR-4 API responses for plan retrieval shall complete within reasonable time for local development.
NFR-5 Drag-and-drop interactions shall feel responsive.

6.3 Security

NFR-6 Passwords shall never be stored in plaintext.
NFR-7 Authentication tokens shall be securely generated and validated.
NFR-8 Sensitive configuration values shall not be committed to source control.

6.4 Maintainability

NFR-9 The server codebase shall follow a modular structure:

api for routes

services for business logic

models for database models

schemas for request/response validation

NFR-10 The system shall support database migrations via Alembic.
NFR-11 The project shall include basic automated tests.

6.5 Developer Experience

NFR-12 The entire system shall be runnable locally using:

docker compose up --build

NFR-13 Health checks shall exist for server and database services.
NFR-14 Clear documentation shall exist for setup and contribution.

7. Constraints

The system must support user-chosen study content, not proprietary content redistribution.

The project must remain feasible for a solo developer over a limited timeline.

The system must prioritize flexibility over rigid schedules.

8. Assumptions

Users have access to at least some study materials.

Users may miss study days and need easy rescheduling.

The platform is primarily used during MCAT preparation windows (weeks to months).

9. Future Enhancements (Non-Required)

Anki deck import/export support

Analytics on study consistency

Multi-device sync

Mobile-friendly UI

Advisor or mentor dashboards

10. Definition of Success

The project is considered successful if:

A user can create an account

Add their own study resources

Generate a personalized study plan

Adjust that plan dynamically as life changes

Run the full system locally with minimal setup
