
from typing import Generator

import pytest

from app.db.session import db, cache


@pytest.fixture(scope="session")
def get_db() -> Generator:
    yield db


@pytest.fixture(scope="session")
def get_cache() -> Generator:
    yield cache
