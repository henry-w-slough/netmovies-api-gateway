from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import httpx



def register_exception_handlers(app: FastAPI):
    """Adds all exceptions handlers to FastAPI app given including custom exceptions."""


    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError):
        return JSONResponse(status_code=422, content={"error": "The format of the HTTP request received is invalid.", "detail": str(exc)})
    
    @app.exception_handler(httpx.ConnectTimeout)
    async def connect_timeout(request: Request, exc: httpx.ConnectTimeout):
        return JSONResponse(status_code=504, content={"error": "Connection with backend timed out before a response was given."})
    
    @app.exception_handler(httpx.ReadTimeout)
    async def read_timeout(request: Request, exc: httpx.ReadTimeout):
        return JSONResponse(status_code=504, content={"error": "Backend service took too long to respond."})

    @app.exception_handler(httpx.ConnectError)
    async def connect_error(request: Request, exc: httpx.ConnectError):
        return JSONResponse(status_code=503, content={"error": "Connection with backend is unreachable.", "detail": str(exc)})

    @app.exception_handler(Exception)
    async def general_error(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"error": "Unhandled exception caught in the backend.", "detail": str(exc)})
