from typing import Any
import json

from fastapi import APIRouter, status, Depends

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("", status_code=200, response_model=schemas.UserBase)
def get_my_information(
    current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:
    return json.loads(current_user.to_json())


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_my_information(
    current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:
    """
    Remove admin user.
    """
    crud.user.remove(uuid=current_user.uuid)
    return None
