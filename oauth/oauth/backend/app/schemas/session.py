from pydantic import BaseModel, EmailStr


class SessionCreate(BaseModel):
    email: EmailStr
    password: str


class SessionPayload(BaseModel):
    sub: str = None
