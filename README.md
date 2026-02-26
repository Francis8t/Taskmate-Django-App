# Taskmate

### Production-Ready Django Task Management Platform

Taskmate is a modular, PostgreSQL-backed Django application designed to
demonstrate clean architecture, secure configuration management, and
production deployment readiness.

This project showcases practical backend engineering principles
including:

-   Environment-based configuration
-   Secure authentication flows
-   PostgreSQL integration
-   Static asset management for production
-   Clean app separation
-   Deployment readiness (Gunicorn + WhiteNoise)


## 🏗 Architecture Overview

Client (Browser)\
↓\
Gunicorn (WSGI Server)\
↓\
Django Application\
↓\
PostgreSQL Database

P.S: In production environments without Nginx, static files are served via
WhiteNoise.


## Core Features

### Authentication & User Isolation

-   User registration
-   Login / Logout (POST-based logout for CSRF protection)
-   User-specific task ownership
-   Secure session handling

### Task Management

-   Create, update, delete tasks
-   Paginated task lists
-   Database-backed persistence (PostgreSQL)
-   Owner-based access control

### Configuration Management

-   Environment variable isolation via `.env`
-   Secrets excluded from version control
-   Separation of development vs production settings


## Tech Stack

  Layer             Technology
  ----------------- ---------------------
  Backend           Django
  Language          Python 3.12
  Database          PostgreSQL
  Static Handling   WhiteNoise
  Forms             django-crispy-forms
  Styling           Bootstrap 5
  WSGI Server       Gunicorn


## Project Structure

. ├── manage.py\
├── static/\
├── taskmate/\
│ ├── settings.py\
│ ├── urls.py\
│ ├── wsgi.py\
│ └── templates/\
├── todolist_app/\
│ ├── models.py\
│ ├── views.py\
│ ├── urls.py\
│ └── migrations/\
└── users/\
├── forms.py\
├── views.py\
├── urls.py\
└── templates/


## Security Practices Implemented

-   Environment-based secret management
-   `.env` excluded from version control
-   CSRF protection enforced
-   Logout restricted to POST requests
-   Database credentials isolated from source code
-   DEBUG separated from production configuration


## Local Development Setup

### 1. Clone Repository

`git clone
https://github.com/`<your-username>`{=html}/Taskmate-Django-App.git\
cd Taskmate-Django-App`

### 2. Create Virtual Environment

```python 
python -m venv venv\
source venv/bin/activate
```

### 3. Install Dependencies

`pip install -r requirements.txt`

### 4. Configure Environment Variables

Create `.env` in project root:

```bash
DJANGO_SECRET_KEY=your-secret-key\
DJANGO_DEBUG=True

DB_ENGINE=django.db.backends.postgresql\
DB_NAME=todolist\
DB_USER=your-db-user\
DB_PASSWORD=your-db-password\
DB_HOST=localhost\
DB_PORT=5432
```

### 5. Run Migrations

`python manage.py migrate`

### 6. Start Development Server

`python manage.py runserver`

Access: http://127.0.0.1:8000/


## Production Deployment Notes

-   Set `DJANGO_DEBUG=False`
-   Configure `ALLOWED_HOSTS`
-   Install Gunicorn:

`pip install gunicorn`

-   Run:

`gunicorn taskmate.wsgi:application`

-   Collect static assets:

`python manage.py collectstatic --noinput`

WhiteNoise middleware is configured to serve static assets when no
reverse proxy (like, Nginx) is present.


## Architectural Considerations

This project demonstrates:

-   Separation of concerns
-   Clean configuration layering
-   Secure authentication workflows
-   Database-backed user ownership
-   Production deployment awareness


## Potential Enhancements

-   REST API via Django REST Framework
-   JWT-based authentication
-   Docker containerization
-   CI/CD pipeline integration
-   S3-based static asset storage
-   Role-based access control (RBAC)
-   Background task processing (Celery + Redis)
-   Caching layer (Redis)


## Author

Francis Gathua Kariuki\
Cloud & DevOps Engineer 
