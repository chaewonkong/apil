from fastapi import FastAPI
from core.router import router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=router)

    return app