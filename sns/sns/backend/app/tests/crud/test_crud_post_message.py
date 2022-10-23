from app import crud
from app.schemas import PostMessageCreate, UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_post_message() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)

    message = random_lower_string()
    user_in = PostMessageCreate(
        message=message)
    post_message = crud.post_message.create(obj_in=user_in, post_user=user)
    assert post_message.message == message


def test_get_post_messages() -> None:
    email = random_email()
    password = random_lower_string()
    display_name = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        display_name=display_name)
    user = crud.user.create(obj_in=user_in)

    message_01 = random_lower_string()
    message_in_01 = PostMessageCreate(
        message=message_01)
    post_message_01 = crud.post_message.create(
        obj_in=message_in_01, post_user=user)

    message_02 = random_lower_string()
    message_in_02 = PostMessageCreate(
        message=message_02)
    post_message_02 = crud.post_message.create(
        obj_in=message_in_02, post_user=user)

    messages = crud.post_message.get(post_user=user)

    assert post_message_01 in messages
    assert post_message_02 in messages
