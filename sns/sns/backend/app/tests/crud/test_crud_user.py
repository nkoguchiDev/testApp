from app import crud
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_user(get_db) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(get_db, obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")
