# Agent Guide

## Project Overview

This project is a Django + Vue commercial website scaffold.

- Backend: Django 4.2, project package `config`, app `website`
- Admin UI: Django Simple UI, with Chinese admin language enabled
- Frontend: Vue 3 + Vite in `frontend/`
- Database: local SQLite file `db.sqlite3`
- Python virtual environment: `.venv/`

## Key URLs

- Vue frontend: http://127.0.0.1:5173/
- Django backend root: http://127.0.0.1:8000/ redirects to the Vue frontend
- Django admin: http://127.0.0.1:8000/admin/

## Admin Account

- Username: `andyduan26`
- Email: `andyduanxiaoga@163.com`
- Display name stored in `first_name`: `钱多多`
- Role: staff and superuser

## Backend Setup

Activate the virtual environment before running Django commands:

```bash
source .venv/bin/activate
```

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver 127.0.0.1:8000
```

Check Django configuration:

```bash
python manage.py check
```

## Frontend Setup

Install Node dependencies:

```bash
cd frontend
npm install --ignore-scripts
```

The `--ignore-scripts` flag avoids optional native dependency build hangs observed with the current local Node/npm environment while preserving required Vite/Rolldown native packages.

Start the Vue development server:

```bash
cd frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

Build the frontend:

```bash
cd frontend
npm run build
```

## Important Files

- `config/settings.py`: Django settings, installed apps, language, timezone
- `config/urls.py`: Django URL routing; `/` redirects to Vue
- `requirements.txt`: Python dependencies
- `frontend/src/App.vue`: Vue homepage
- `frontend/src/style.css`: Vue homepage styles
- `frontend/vite.config.js`: Vite config and `/api` proxy to Django
- `.gitignore`: ignores local environment, database, Node modules, and build output

## Current Conventions

- Keep Django admin at `/admin/`.
- Keep public frontend work in `frontend/`.
- Use Django for backend/admin/API behavior.
- Use Vue for public website pages and interactive frontend UI.
- For future APIs, expose Django endpoints under `/api/...`; Vite already proxies `/api` to `http://127.0.0.1:8000`.
- Do not commit `.venv/`, `db.sqlite3`, `frontend/node_modules/`, or `frontend/dist/`.

## Verification Checklist

Before handing off changes, run:

```bash
source .venv/bin/activate
python manage.py check
cd frontend
npm run build
```

Expected result:

- Django reports `System check identified no issues`.
- Vite build completes successfully.
