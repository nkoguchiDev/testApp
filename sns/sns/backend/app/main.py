from fastapi import FastAPI
from mongoengine import connect, disconnect

from app.api.api_v1.api import api_router

from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,
              openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
def on_startup():
    connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        uuidRepresentation="standard",
        alias='mongodb'
    )


@app.on_event("shutdown")
def shutdown_event():
    disconnect(alias='mongodb')


@app.get("/health")
def root():
    return {"status": "ok"}
