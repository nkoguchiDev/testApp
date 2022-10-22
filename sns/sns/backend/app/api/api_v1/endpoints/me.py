from typing import Any

from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("", status_code=200, response_model=schemas.UserBase)
def get_my_information(
    current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:
    return jsonable_encoder(
        schemas.UserBase(
            email=current_user.email,
            display_name=current_user.display_name,
            is_active=current_user.is_active,
            is_superuser=current_user.is_active
        )
    )


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_my_information(
    current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:
    """
    Remove admin user.
    """
    crud.user.remove(uuid=current_user.uuid)
    return None
