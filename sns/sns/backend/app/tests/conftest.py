import pytest

from typing import Generator
from mongoengine import connect, disconnect

from app.core.config import settings


@pytest.fixture(scope='session', autouse=True)
def scope_session():
    connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        db=settings.DB_NAME,
        uuidRepresentation="standard",
        alias='mongodb'
    )
    yield
    disconnect(alias='mongodb')


# @pytest.fixture(scope="session")
# def get_cache() -> Generator:
#     yield cache
