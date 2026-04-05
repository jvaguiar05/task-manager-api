from fastapi import FastAPI

from app.api.routes import user as user_router
from app.api.routes.task import router as task_router

app = FastAPI(title="Task Manager API")

app.include_router(user_router.router)
app.include_router(task_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
