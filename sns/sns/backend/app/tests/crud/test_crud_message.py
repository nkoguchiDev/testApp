from app import crud
from app.schemas import MessageCreate, UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_message() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)

    content = random_lower_string()
    message_in = MessageCreate(
        content=content)
    message = crud.message.create(obj_in=message_in, user=user)
    assert message.content == content
    assert hasattr(message, "uuid")
    assert hasattr(message, "date")
    assert hasattr(message, "create_user")


def test_get_messages() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)

    content_01 = random_lower_string()
    message_in_01 = MessageCreate(
        content=content_01)
    message_01 = crud.message.create(
        obj_in=message_in_01, user=user)

    content_02 = random_lower_string()
    message_in_02 = MessageCreate(
        content=content_02)
    message_02 = crud.message.create(
        obj_in=message_in_02, user=user)

    messages = crud.message.get(user=user)

    assert message_01 in messages
    assert message_02 in messages


def test_delete_messages() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)

    content_01 = random_lower_string()
    message_in_01 = MessageCreate(
        content=content_01)
    message_01 = crud.message.create(
        obj_in=message_in_01, user=user)

    content_02 = random_lower_string()
    message_in_02 = MessageCreate(
        content=content_02)
    message_02 = crud.message.create(
        obj_in=message_in_02, user=user)
    crud.message.delete(uuid=message_02.uuid, user=user)
    messages = crud.message.get(user=user)

    assert message_01 in messages
    assert message_02 not in messages
