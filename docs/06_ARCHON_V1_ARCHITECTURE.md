# **Archon V1: Productized MVP - Architectural Vision**

**Date:** 2025-11-10

**Objective:** To define the high-level architecture for the Archon V1 web application. This document serves as the foundational blueprint for the next "Build" cycle.

---

## **1. Core Principles**

*   **Monolithic but Modular:** We will build a single Flask application (a "monolith") for simplicity and speed of development. However, the code will be organized into logical modules (e.g., `auth`, `teams`, `compasses`) to make it easy to refactor into microservices in the distant future if necessary.
*   **API-First:** The backend will be a pure RESTful API that serves JSON. The frontend will be a completely separate, single-page application (SPA) built in React. This separation of concerns is critical for maintainability.
*   **Standard & "Boring" Technology:** We will adhere to the chosen stack (Flask, PostgreSQL, React) and use well-established libraries to minimize technical risk and maximize development velocity.

---

## **2. Data Models (PostgreSQL Schema)**

This defines the core database schema.

### **`users`**
*   `id` (PK, UUID)
*   `email` (VARCHAR, UNIQUE, NOT NULL)
*   `password_hash` (VARCHAR, NOT NULL)
*   `full_name` (VARCHAR)
*   `created_at` (TIMESTAMP)

### **`teams`**
*   `id` (PK, UUID)
*   `team_name` (VARCHAR, NOT NULL)
*   `created_at` (TIMESTAMP)

### **`team_memberships`** (Join Table)
*   `user_id` (FK to `users.id`)
*   `team_id` (FK to `teams.id`)
*   `role` (VARCHAR, e.g., 'owner', 'member')

### **`compasses`**
*   `id` (PK, UUID)
*   `team_id` (FK to `teams.id`)
*   `title` (VARCHAR, e.g., "Q4 2025 Strategy")
*   `data` (JSONB, NOT NULL) - This field will store the entire `compass.json` document. Using JSONB allows us to query the contents if needed.
*   `created_at` (TIMESTAMP)
*   `updated_at` (TIMESTAMP)

---

## **3. Core Features & API Endpoints**

This defines the minimum viable feature set for the Productized MVP.

### **Authentication**
*   **`POST /api/auth/register`**: Create a new user account.
*   **`POST /api/auth/login`**: Authenticate a user and return a JWT (JSON Web Token).
*   **`GET /api/auth/me`**: Get the profile of the currently authenticated user.

### **Teams**
*   **`POST /api/teams`**: Create a new team.
*   **`GET /api/teams`**: Get all teams the current user is a member of.
*   **`POST /api/teams/{team_id}/members`**: Invite a new member to a team.

### **Compasses**
*   **`POST /api/teams/{team_id}/compasses`**: Create a new, blank Compass document for a team.
*   **`GET /api/teams/{team_id}/compasses`**: Get a list of all Compasses for a team.
*   **`GET /api/compasses/{compass_id}`**: Get the full data for a single Compass document.
*   **`PUT /api/compasses/{compass_id}`**: Save/update the data for a Compass document.
*   **`DELETE /api/compasses/{compass_id}`**: Delete a Compass document.

---

## **4. High-Level System Design**

*   **Backend (Flask):**
    *   A single Flask application.
    *   Use Blueprints to organize routes by feature (auth, teams, compasses).
    *   Use SQLAlchemy as the ORM for interacting with the PostgreSQL database.
    *   Use a library like `Flask-JWT-Extended` for handling JSON Web Tokens.
*   **Frontend (React):**
    *   A standard `create-react-app` project.
    *   Use a state management library (like Redux Toolkit or Zustand) to manage application state.
    *   Use a routing library (like React Router) to handle navigation.
    *   Communicate with the backend via RESTful API calls using `axios` or `fetch`.
*   **Deployment (Initial):**
    *   The entire application (Flask backend, React frontend, PostgreSQL database) will be containerized using Docker and defined in a `docker-compose.yml` file.
    *   This will make local development simple and provides a clear path to deploying on any modern cloud provider (e.g., AWS, GCP, DigitalOcean).
