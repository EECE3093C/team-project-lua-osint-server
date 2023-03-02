from fastapi import APIRouter

root_router = APIRouter(
    responses={404: {"message" : "Oh, jeez! Where's the root, Rick!?"}}
)

@root_router.get('/')
async def hello_world():
    return {"message":"Hello, world!"}