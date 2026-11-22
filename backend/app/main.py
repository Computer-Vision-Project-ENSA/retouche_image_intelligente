from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.app.api.routes import router

app = FastAPI(title="IntelliRetouch API")

app.include_router(router, prefix="/api")

# Chemin vers le build React
BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIST = BASE_DIR / "frontend" / "dist"

if FRONTEND_DIST.is_dir():
    app.mount(
        "/",
        StaticFiles(directory=FRONTEND_DIST, html=True),
        name="frontend",
    )
