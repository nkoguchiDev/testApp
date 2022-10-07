from fastapi import APIRouter

from app.api.api_v1.endpoints import users, session

api_router = APIRouter()
api_router.include_router(session.router, prefix="/session", tags=["session"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
