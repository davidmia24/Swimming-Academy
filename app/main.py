from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401  (importarlo registra las tablas)
from app.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  # se ejecuta una vez al arrancar el servidor
    yield


app = FastAPI(title="Academia de Natación", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}
