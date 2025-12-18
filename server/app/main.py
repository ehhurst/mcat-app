from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="MCAT Access Platform API")

@app.get("/healthcheck")
def healthz():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")
