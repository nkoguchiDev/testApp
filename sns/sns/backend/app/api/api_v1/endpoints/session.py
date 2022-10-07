from typing import Any
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Response, status
from fastapi.responses import JSONResponse

from app import crud, schemas
from app.core import security
from app.core.config import settings

router = APIRouter()


@router.post("")
def create_session(session: schemas.SessionCreate, response: Response) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        email=session.email,
        password=session.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password")

    if not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    cookie = security.create_access_token(
        user.uuid,
        expires_delta=access_token_expires
    )
    response = JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=None)
    response.set_cookie(key="session_cookie", value=cookie)
    return response
