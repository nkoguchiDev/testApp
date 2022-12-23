from pydantic import BaseModel


# Shared properties
class CredentialBase(BaseModel):
    key: str
    secret: str


# Properties to receive via API on creation
class CredentialCreate(CredentialBase):
    None


# Properties to receive via API on update
class CredentialUpdate(CredentialBase):
    None
