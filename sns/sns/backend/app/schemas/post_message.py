# from typing import Optional

from pydantic import BaseModel


# Shared properties
class PostMessageBase(BaseModel):
    message: str


# Properties to receive via API on update
class PostMessageCreate(PostMessageBase):
    pass
