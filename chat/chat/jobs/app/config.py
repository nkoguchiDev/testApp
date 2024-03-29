from pydantic import BaseSettings


class Settings(BaseSettings):

    # db settings
    db_host: str = "localhost"
    db_port: int = 443

    # app settings
    voice_api_host: str = "localhost"
    voice_api_port: int = 50021
    voice_api_protocol: str = "http"
    app_base_dir: str = "app"

    voice_query_endpoint: str \
        = f"{voice_api_protocol}://{voice_api_host}:{voice_api_port}/audio_query"

    voice_generator_endpoint: str \
        = f"{voice_api_protocol}://{voice_api_host}:{voice_api_port}/synthesis"

    chara_name: str = "ZUN"
    # openai settings
    gpt_api_key: str
    gpt_ai_engine: str = "text-davinci-003"


settings = Settings()
