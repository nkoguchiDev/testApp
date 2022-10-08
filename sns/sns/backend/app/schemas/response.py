from pydantic import BaseModel


class Unauthorized_401(BaseModel):
    message: str = "Authentication failed."


class Unauthorized_403(BaseModel):
    message: str = "Authentication denied."


class Unauthorized_404(BaseModel):
    message: str = "Resource not found."


class Unauthorized_409(BaseModel):
    message: str = "Request conflicted with current information."
