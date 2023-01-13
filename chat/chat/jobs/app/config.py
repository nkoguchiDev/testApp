from pydantic import BaseSetting


class Settings(BaseSetting):
    db_host: str
    db_port: int

    voice_api_host: str = "localhost"
    voice_api_port: int = 80
    voice_api_protocol: str = "http"

    voice_query_endpoint: str \
        = f"{voice_api_protocol}://{voice_api_host}:{voice_api_port}/audio_query"

    voice_generator_endpoint: str \
        = f"{voice_api_protocol}://{voice_api_host}:{voice_api_port}/synthesis"


settings = Settings()
