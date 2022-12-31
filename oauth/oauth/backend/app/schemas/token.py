from pydantic import BaseModel, EmailStr


class TokenCreate(BaseModel):
    accesskey: EmailStr
    secret: str


class TokenPayload(BaseModel):
    token: str = None
    refreh_token: str = None
