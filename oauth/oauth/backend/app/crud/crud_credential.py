from uuid import uuid4


from app.crud.base import CRUDBase
from app.models import User, Credential
from app.schemas.credential import CredentialCreate, CredentialUpdate
from app.core.security import get_hash_string


class CRUDCredential(CRUDBase[Credential, CredentialCreate, CredentialUpdate]):

    def create(
            self,
            key: str,
            secret: str,
            user: User,
            is_active: bool) -> Credential:
        uuid = uuid4().hex
        db_obj = Credential(
            uuid=uuid,
            key=get_hash_string(key),
            secret=get_hash_string(secret),
            user=user,
            is_active=is_active,
        )
        db_obj.save()
        return Credential.objects(uuid=uuid).first()

    def is_active(self, credential: Credential) -> bool:
        return credential.is_active


credential = CRUDCredential(Credential)
