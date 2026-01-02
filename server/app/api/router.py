from fastapi import APIRouter
from app.api.v1.api import router as v1_router
from app.api.v1 import auth, users, resources, planning

api_router = APIRouter()
api_router.include_router(v1_router, prefix="/v1")
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(resources.router, prefix="/resources", tags=["resources"])
api_router.include_router(planning.router, prefix="/planning", tags=["planning"])
