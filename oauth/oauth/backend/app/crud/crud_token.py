from app.core.security import create_oauth_token


class CRUDToken:

    def get(self, cache, token: str) -> dict:
        return cache.hgetall(token)

    def create(self, cache, user_id: str) -> str:
        oauth_token = create_oauth_token()
        cache.hmset(oauth_token, {"user_id": user_id}, ex=60)
        return oauth_token

    def delete(self, cache, token: str) -> None:
        cache.delete(token)
        return


token = CRUDToken()
