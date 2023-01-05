from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

client = AsyncIOMotorClient(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    uuidRepresentation="standard"
)
db = client[settings.DB_NAME]
