# Project Umbrella

A multi-tenant SaaS platform built to streamline complex lease management for property owners, featuring a secure, containerized architecture using Django and PostgreSQL.

## Tech Stack

### Backend
* **Python:** The core programming language.
* **Django:** The high-level web framework for the application's structure.
* **Django REST Framework:** For building the application's API.
* **Django-Tenants:** Key library for enabling the multi-tenant architecture.

### Database & Data Stores
* **PostgreSQL:** The primary relational database for data persistence.
* **Redis:** In-memory data store, used as a message broker for Celery.

### Asynchronous Tasks
* **Celery:** Distributed task queue for handling background processes.

### Deployment & Infrastructure
* **Docker:** For containerizing the application and ensuring a consistent environment.
* **Gunicorn:** The WSGI server used to run the Django application in production.
* **Nginx:** High-performance web server used as a reverse proxy.

### Cloud Services (Google Cloud Platform)
* **Google Cloud SQL:** Managed PostgreSQL database service.
* **Google Cloud Storage:** For scalable object storage (e.g., user-uploaded files).
* **Google Secret Manager:** For securely storing and accessing API keys and credentials.

### Developer Tools & Code Quality
* **Git & GitHub:** For version control and source code management.
* **Black & Flake8:** For automated code formatting and linting to maintain code quality.
* **Pre-commit:** For managing and enforcing pre-commit hooks.