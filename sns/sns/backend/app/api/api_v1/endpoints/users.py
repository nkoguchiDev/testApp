from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.post("/", response_model=schemas.UserBase)
def create_user(user_in: schemas.UserCreate) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(obj_in=user_in)
    return schemas.UserBase(email=user.email,
                            is_active=user.is_active,
                            is_superuser=user.is_superuser,
                            full_name=user.full_name,)
