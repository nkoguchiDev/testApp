from uuid import uuid4

from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_email(self, email: str) -> Optional[User]:
        return User.objects.get(email=email)

    def create(self, obj_in: UserCreate) -> User:
        db_obj = User(
            uuid=uuid4().hex,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        db_obj.save()

        return db_obj

    def authenticate(self,
                     email: str,
                     password: str) -> Optional[User]:
        user = self.get_by_email(email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user = CRUDUser(User)
