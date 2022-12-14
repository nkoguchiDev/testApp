from fastapi.encoders import jsonable_encoder

from app import crud
from app.core.security import verify_password
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_user() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")
    assert hasattr(user, "display_name")


def test_authenticate_user() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)
    authenticated_user = crud.user.authenticate(
        email=email, password=password)
    assert authenticated_user
    assert user.email == authenticated_user.email


def test_not_authenticate_user() -> None:
    email = random_email()
    password = random_lower_string()
    user = crud.user.authenticate(email=email, password=password)
    assert user is None


def test_not_authenticate_user_password_not_mache() -> None:
    email = random_email()
    password = random_lower_string()
    invalid_password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)
    user = crud.user.authenticate(email=email, password=invalid_password)
    assert user is None


def test_check_if_user_is_active() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active is True


def test_check_if_user_is_active_inactive() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name,
        is_active=False)
    user = crud.user.create(obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active is False


def test_check_if_user_is_superuser() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(email=email,
                         password=password,
                         display_name=display_name,
                         is_superuser=True)
    user = crud.user.create(obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is True


def test_check_if_user_is_superuser_normal_user() -> None:
    username = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(email=username,
                         display_name=display_name,
                         password=password)
    user = crud.user.create(obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is False


def test_get_user() -> None:
    password = random_lower_string()
    username = random_email()
    display_name = random_lower_string()
    user_in = UserCreate(email=username,
                         password=password,
                         display_name=display_name,
                         is_superuser=True)
    user = crud.user.create(obj_in=user_in)
    user_2 = crud.user.get(uuid=user.uuid)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_update_user() -> None:
    password = random_lower_string()
    email = random_email()
    display_name = random_lower_string()
    user_in = UserCreate(email=email,
                         password=password,
                         display_name=display_name,
                         is_superuser=True)
    user = crud.user.create(obj_in=user_in)
    new_password = random_lower_string()
    new_display_name = random_lower_string()
    user_in_update = UserUpdate(
        password=new_password,
        display_name=new_display_name,
        is_superuser=True)
    crud.user.update(uuid=user.uuid, obj_in=user_in_update)
    user_2 = crud.user.get(uuid=user.uuid)
    assert user_2
    assert user.email == user_2.email
    assert user_2.display_name == new_display_name
    assert verify_password(new_password, user_2.hashed_password)


def test_delete_user() -> None:
    password = random_lower_string()
    username = random_email()
    display_name = random_lower_string()
    user_in = UserCreate(email=username,
                         password=password,
                         display_name=display_name,
                         is_superuser=True)
    user = crud.user.create(obj_in=user_in)
    crud.user.delete(uuid=user.uuid)
    user_2 = crud.user.get(uuid=user.uuid)
    assert user_2 is None
