# from typing import Optional

from pydantic import BaseModel


# Shared properties
class MessageBase(BaseModel):
    content: str


# Properties to receive via API on update
class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    uuid: str
    date: str
    create_user: str
