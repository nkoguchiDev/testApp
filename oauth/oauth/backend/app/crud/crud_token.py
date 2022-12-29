from uuid import uuid4


from app.crud.base import CRUDBase
from app.models import Token
from app.schemas.credential import TokenCreate, TokenUpdate
from app.core.security import create_oauth_token


class CRUDToken(CRUDBase[Token, TokenCreate, TokenUpdate]):

    def create(self, cache) -> str:
        oauth_token = create_oauth_token()
        cache.set(oauth_token, {"user_id": "id"})
        return oauth_token


token = CRUDToken(Token)
