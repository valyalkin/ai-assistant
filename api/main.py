
from fastapi import FastAPI, File, UploadFile, HTTPException
import logging

from apis import chat, documents

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def configure_application():
    application = FastAPI(
        title='AI Assistant',
        debug=False,
    )

    # Routers
    application.include_router(chat.router)
    application.include_router(documents.router)

    # Logging
    logger = logging.getLogger("uvicorn.error")
    logger.propagate = False

    return application

app = configure_application()


