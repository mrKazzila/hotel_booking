<h1 align="center">
  Hotel booking project
</h1>

<h4 align="center">
    The project for study FastApi
    <br>
    <a href="https://stepik.org/course/153849/info" target="_blank">
      FastAPI - an immersion into backend development in Python
    </a>
</h4>

<div align="center">

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)


</div>
<hr>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech stack</a> •
  <a href="#how-to-use">How To Use</a>
</p>


## Features
- User registration
- User authentication using JWT token
- Hotel room booking
- User notification of room booking
- Image processing with hotels
- Admin panel for convenience


## Tech stack
- [Python 3.11](https://www.python.org/downloads/)
- [FastApi](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://pypi.org/project/alembic/)
- [Poetry](https://python-poetry.org/docs/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Redis](https://redis.io/)
- [Sentry](https://sentry.io/)
- [Sqladmin](https://aminalaee.dev/sqladmin/)


## How To Use
<details>

<summary><strong>Local run</strong></summary>

1. Firstly clone repo
   ```bash
   git clone git@github.com:mrKazzila/hotel_booking.git
   ```

2. SetUp poetry
   ```bash
   poetry config virtualenvs.in-project true
   poetry shell
   poetry install
   ```

3. Copy env example settings to env and fill them in
   ```bash
   cp env/.env.example env/.env
   ```

4. Run app
   ```bash
   uvicorn app.main:app --reload --log-config=app/settings/logger_config.yaml  --env-file=env/.env
   ```

</details>


<br>
<br>
<p align="center">
  <a href="https://github.com/mrKazzila">GitHub</a> •
  <a href="https://mrkazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
