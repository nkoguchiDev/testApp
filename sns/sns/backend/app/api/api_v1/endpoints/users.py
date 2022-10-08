from typing import Any, Union

from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse

from app import crud, schemas, models
from app.api import deps

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
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=response.dict(exclude_unset=True))


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def remove_admin_user(
    current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:
    """
    Remove admin user.
    """
    crud.user.remove(uuid=current_user.uuid)
    return None
