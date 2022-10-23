import json
from typing import Any

from fastapi import APIRouter, HTTPException, Depends

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.post("", response_model=schemas.UserBase, status_code=201)
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
    return json.loads(user.to_json())


@router.delete("", status_code=204)
def remove_admin_user(
    current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:
    """
    Remove admin user.
    """
    crud.user.remove(uuid=current_user.uuid)
    return None
