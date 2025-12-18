from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="MCAT Access Platform API")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")
