import fastapi
import uvicorn
import config
from Controllers import MovieMetadataController


app = fastapi.FastAPI()

#including the routers within MovieMetadataController to app
app.include_router(MovieMetadataController.router)


#without this, uvicorn runs at import time causing errors
if __name__ == "__main__":
    uvicorn.run(app, host=config.GATEWAY_IP, port=config.GATEWAY_PORT)