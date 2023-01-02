from app.crud import token


def test_get(redis_cache):
    res = token.get(redis_cache, "jduiojdwqoidj")
    assert res == {}


def test_create(redis_cache):
    user_id = "fhowejoepwjfopewj"
    token_str = token.create(redis_cache, user_id)
    res = token.get(redis_cache, token_str)

    assert res.get("user_id", None) == user_id
