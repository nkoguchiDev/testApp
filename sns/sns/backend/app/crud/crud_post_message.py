from uuid import uuid4


# from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models import PostMessage, User
from app.schemas import PostMessageCreate


class CRUDUser(CRUDBase[PostMessage, PostMessageCreate, PostMessageCreate]):

    def get(self, post_user: User) -> PostMessage:
        return PostMessage.objects(user=post_user)

    def create(
            self,
            obj_in: PostMessageCreate,
            post_user: User) -> PostMessage:
        uuid = uuid4().hex
        db_obj = PostMessage(
            uuid=uuid,
            message=obj_in.message,
            user=post_user,
        )
        db_obj.save()
        return PostMessage.objects(uuid=uuid).first()


post_message = CRUDUser(PostMessage)
