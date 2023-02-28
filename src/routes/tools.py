from fastapi import APIRouter

tool_router = APIRouter(
    prefix='/tools',
    responses={404: {"message" : "Oh, jeez! Where's the tool, Rick!?"}}
)

fake_tools = ['MEGA_TOOL', 'sherlock', 'raygun']

@tool_router.get('/')
async def read_tools():
    return fake_tools