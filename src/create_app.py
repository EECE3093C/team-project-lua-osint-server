from fastapi import FastAPI

from middleware import add_app_middleware
from routes import add_app_routes

# App
app = FastAPI()

# Database stuff??


# Apply middleware
add_app_middleware(app)

# Apply routes
add_app_routes(app)