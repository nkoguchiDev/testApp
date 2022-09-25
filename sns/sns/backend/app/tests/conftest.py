
from typing import Generator

import pytest

from app.db
from app.cache


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="session")
def cache() -> Generator:
    yield SessionLocal()
