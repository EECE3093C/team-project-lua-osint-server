from fastapi import FastAPI

from .tools import tool_router

def add_app_routes(app: FastAPI) -> None:
    app.include_router(tool_router)