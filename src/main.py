import uvicorn
from loguru import logger
from create_app import app

# Do more stuff here??

if __name__ == '__main__':
    logger.info("Starting Server...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        root_path=".",
        reload=True
    )