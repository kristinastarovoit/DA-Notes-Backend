# Django Notes App (Backend)

A small practice project created as part of the Developer Akademie. A Django REST backend provides an API for a notes app, so that an existing Angular frontend can create, edit, delete and mark notes as favorites. The goal is to practice models, serializers and viewsets. This repository contains only the backend; the frontend is available here: `https://github.com/Developer-Akademie-AA/da_notes_frontend_teilnehmer`.

## Quickstart

### Prerequisites

* Python 3 (a version supported by Django 6.1)
* Dependencies from `requirements.txt`: Django 6.1.3, djangorestframework 3.18.3, django-cors-headers 4.9.0 and more
* The Angular frontend, served on port 4200 (`ng serve`)

### Setup

Run these commands from the project folder (the one containing `manage.py`).

Create and activate a virtual environment (Windows PowerShell):

```
python -m venv .venv
.venv/Scripts/Activate
```

On macOS/Linux, activate it with `source .venv/bin/activate` instead.

Install the dependencies and create the database:

```
pip install -r requirements.txt
python manage.py migrate
```

## Usage

Start the backend:

```
python manage.py runserver
```

The API is now available at `http://127.0.0.1:8000/notes/`. It is a standard `ModelViewSet`, so it supports listing and creating notes at `/notes/` as well as retrieving, updating and deleting a single note at `/notes/<id>/`. Each note has the fields `id`, `title`, `content`, `marked` (favorite) and `trash`.

Then start the Angular frontend with `ng serve` and open `http://localhost:4200`.

## Notes

* The backend only allows cross-origin requests from the Angular dev server. Make sure `CORS_ALLOWED_ORIGINS` in `settings.py` contains `http://localhost:4200` (and `http://127.0.0.1:4200` if you use that address), otherwise the browser blocks the requests.
* The notes are stored in the default local SQLite database, which every user creates on their own with `python manage.py migrate`.