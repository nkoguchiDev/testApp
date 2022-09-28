from app import crud
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_user() -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")


def test_authenticate_user() -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(obj_in=user_in)
    authenticated_user = crud.user.authenticate(
        email=email, password=password)
    assert authenticated_user
    assert user.email == authenticated_user.email
