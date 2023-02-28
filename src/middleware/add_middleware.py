from fastapi import FastAPI
from .cors import add_cors_middleware

def add_app_middleware(app: FastAPI) -> None:
    add_cors_middleware(app)
    