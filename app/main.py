from fastapi import FastAPI

from app.api.routes import user as user_router

app = FastAPI(title="Task Manager API")

app.include_router(user_router.router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
