import fastapi
import uvicorn
import config

from Routers import StorageRouter
from Routers import MetadataRouter

from Exceptions import GlobalExceptionHandler


app = fastapi.FastAPI(redirect_slashes=False)


#including the routers within MovieMetadataController to app
app.include_router(StorageRouter.router)
app.include_router(MetadataRouter.router)


#registering all exceptions in GlobalExceptionHandler
GlobalExceptionHandler.register_exception_handlers(app)


#without this, uvicorn runs at import time causing errors
if __name__ == "__main__":
    uvicorn.run(app, host=config.GATEWAY_IP, port=config.GATEWAY_PORT)

    