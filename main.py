import fastapi
import uvicorn
import config
import socket

from Routers import StorageRouter
from Routers import MetadataRouter


app = fastapi.FastAPI(redirect_slashes=False)

#including the routers within MovieMetadataController to app
app.include_router(StorageRouter.router)
app.include_router(MetadataRouter.router)

#without this, uvicorn runs at import time causing errors
if __name__ == "__main__":
    uvicorn.run(app, host=config.GATEWAY_IP, port=config.GATEWAY_PORT)

    