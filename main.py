import fastapi
import httpx
import uvicorn
import uuid
import os
import config
from Controllers import MovieMetadataController


app = fastapi.FastAPI()

app.include_router(MovieMetadataController.router)


#without this, uvicorn runs at import time causing errors
if __name__ == "__main__":
    uvicorn.run(app, host=config.GATEWAY_IP, port=config.GATEWAY_PORT)