from uuid import uuid4
import datetime

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

        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)

        uuid = uuid4().hex
        db_obj = Message(
            uuid=uuid,
            content=obj_in.content,
            user=user,
            date=now.strftime('%Y-%m-%d %H:%M'),
            create_user=user.display_name
        )
        db_obj.save()
        return Message.objects(uuid=uuid).first()

    def delete(
            self,
            uuid: str,
            user: User) -> Message:
        return Message.objects(uuid=uuid, user=user).delete()


message = CRUDMessage(Message)
