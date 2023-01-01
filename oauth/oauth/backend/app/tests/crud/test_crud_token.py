from app.crud import token


def test_get(redis_cache):
    token.get(redis_cache, "jduiojdwqoidj")
