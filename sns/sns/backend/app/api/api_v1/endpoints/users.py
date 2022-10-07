from typing import Any

from fastapi import APIRouter, Header, status, HTTPException
from fastapi.responses import JSONResponse

from app import crud, schemas

router = APIRouter()


@router.post("", response_model=schemas.UserBase)
def create_user(user_in: schemas.UserCreate, admin: bool = False) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system.",
        )

    if admin:
        user_in.is_superuser = admin

    user = crud.user.create(obj_in=user_in)
    response = schemas.UserBase(
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        full_name=user.full_name,
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=response.dict(exclude_unset=True))


@router.delete("")
def remove_admin_user(
        user_agent: Union[str, None] = Header(default=None)) -> Any:
    """
    Remove admin user.
    """
    user = crud.user.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system.",
        )

    if admin:
        user_in.is_superuser = admin

    user = crud.user.create(obj_in=user_in)
    response = schemas.UserBase(
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        full_name=user.full_name,
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=response.dict(exclude_unset=True))
