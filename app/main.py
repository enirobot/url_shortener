from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from app.api import shorten, redirect, stats
from app.core.db import init_db

@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield
    pass

app = FastAPI(lifespan=lifespan, version="1.0.0")

# 422 Unprocessable Entity를 제거하기 위한 custom_openapi 함수
def custom_openapi():
    if not app.openapi_schema:
        app.openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for _, method_item in app.openapi_schema.get('paths').items():
            for _, param in method_item.items():
                responses = param.get('responses')
                if '422' in responses:
                    del responses['422']
    return app.openapi_schema

app.openapi = custom_openapi

# 아래 구성은 개발 환경에서만 사용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(shorten.router, prefix="/api")
app.include_router(redirect.router)
app.include_router(stats.router, prefix="/api")
