# LITReview

LITReview is a Django web application for posting reading tickets and reviews, following other users, and browsing a personalized feed.

## Prerequisites

- Python `3.10` or newer
- `pip` or `uv`
- PowerShell, Command Prompt, or a Unix shell

This repository includes a Django project in `LITReviewProject/` and uses SQLite for local development.

## Environment Setup

### Option 1: Using `uv` (recommended)

From the repository root:

```powershell
uv sync
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Option 2: Using `venv` and `pip`

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

## Database Setup

Move into the Django project folder and apply migrations:

```powershell
cd .\LITReviewProject\
python manage.py migrate
```

The project uses a local SQLite database stored at `LITReviewProject/db.sqlite3`.

## Run the Application

Start the Django development server from `LITReviewProject/`:

```powershell
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Create a User

You can create an account in either of these ways:

1. Start the server and register from the `/signup/` page.
2. Create an admin account from the terminal:

```powershell
python manage.py createsuperuser
```

The Django admin is available at `/admin/`.

## Useful Commands

Run a Django health check:

```powershell
python manage.py check
```

Run the test suite:

```powershell
python manage.py test
```

## Local Development Notes

- `DEBUG` is enabled in `config/settings.py`.
- Uploaded media files are stored in `LITReviewProject/media/`.
- Static files are served by Django during local development.
