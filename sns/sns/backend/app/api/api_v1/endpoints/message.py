from typing import Any, List
import json

from fastapi import APIRouter, HTTPException, Depends

from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get("", status_code=200, response_model=List[schemas.MessageBase])
def get_message_list(current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:

    if current_user is None:
        raise HTTPException(
            status_code=403,
            detail="no permission.",
        )

    message_list = crud.message.get(user=current_user)
    return json.loads(message_list.to_json())


@router.post("", status_code=201, response_model=schemas.MessageBase)
def post_message(
    message_in: schemas.MessageCreate,
    current_user: models.User = Depends(
        deps.get_current_active_user)) -> Any:

    if current_user is None:
        raise HTTPException(
            status_code=403,
            detail="no permission.",
        )

    message_in = schemas.MessageCreate(
        content=message_in.content)
    message = crud.message.create(obj_in=message_in, user=current_user)
    return json.loads(message.to_json())
