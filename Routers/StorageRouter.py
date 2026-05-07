import fastapi
import httpx
import config


#the router used for grouping HTTP requests under a certain URL for shared use cases
router = fastapi.APIRouter(prefix="/storage")


@router.api_route("/{path:path}", methods=["GET", "POST", "DELETE"])
async def storage_gateway(path:str, request:fastapi.Request):
    print(f"Forwarding {request.method} to {config.STORAGE_URL}/{path}")
    async with httpx.AsyncClient() as http:
        #the request sent to the .net backend
        response = await http.request(
            method=request.method,
            url=f"{config.STORAGE_URL}/{path}",
            content=await request.body(),
            headers=request.headers
        )                  
    return fastapi.Response(content=response.content, status_code=response.status_code)