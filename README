# Task Manager API

A simple Task Manager API built to learn and practice a modern Python backend stack using:

* FastAPI
* SQLAlchemy 2.0
* Alembic
* PostgreSQL

---

## 🚀 Purpose

This project is a hands-on learning exercise to understand:

* How to build APIs with FastAPI
* How SQLAlchemy 2.0 works outside of Django ORM
* How to manage database migrations using Alembic
* How to structure a backend project without a full framework

---

## 🧱 Tech Stack

* **FastAPI** – Web framework
* **SQLAlchemy 2.0** – ORM
* **Alembic** – Database migrations
* **PostgreSQL** – Relational database
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server

---

## 📁 Project Structure

```
app/
├── api/            # Route definitions
├── core/           # Config and database setup
├── db/             # Base metadata (Alembic integration)
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── services/       # Business logic layer
└── main.py         # FastAPI entrypoint

alembic/            # Migration scripts
.env                # Environment variables (not committed)
requirements.txt
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd task-manager-api
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the root:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/task_manager
```

Make sure the database exists.

---

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

Access:

* API: http://127.0.0.1:8000
* Docs (Swagger): http://127.0.0.1:8000/docs

---

## 🗄️ Database Migrations (Alembic)

### Generate a migration

```bash
alembic revision --autogenerate -m "your message"
```

### Apply migrations

```bash
alembic upgrade head
```

---

## 🧪 Development Workflow

Typical development cycle:

1. Update or create SQLAlchemy models
2. Generate a migration with Alembic
3. Apply migration
4. Implement/update schemas
5. Create/update routes
6. Test via Swagger (`/docs`)

---

## 📌 Notes

* This project uses **sync SQLAlchemy** for simplicity and learning clarity
* Session management is handled via FastAPI dependencies
* Alembic is configured to read metadata from the app

---

## 📚 Future Improvements

* Authentication (JWT)
* Async support
* Docker setup
* Unit and integration tests
* CI/CD pipeline

---

## 👨‍💻 Author

João Vítor Aguiar da Silva
