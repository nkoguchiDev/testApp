from fastapi import APIRouter

from app.api.api_v1.endpoints import users, session, me, message

api_router = APIRouter()
api_router.include_router(session.router, prefix="/session", tags=["session"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(me.router, prefix="/me", tags=["me"])
api_router.include_router(message.router, prefix="/messages", tags=["message"])
