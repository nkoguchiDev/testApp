from uuid import uuid4


# from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models import Message, User
from app.schemas import MessageCreate


class CRUDMessage(CRUDBase[Message, MessageCreate, MessageCreate]):

    def get(self, user: User) -> Message:
        return Message.objects(user=user)

    def create(
            self,
            obj_in: MessageCreate,
            user: User) -> Message:
        uuid = uuid4().hex
        db_obj = Message(
            uuid=uuid,
            content=obj_in.content,
            user=user,
        )
        db_obj.save()
        return Message.objects(uuid=uuid).first()


message = CRUDMessage(Message)
