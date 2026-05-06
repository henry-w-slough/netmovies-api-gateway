import fastapi
import httpx
import config


#the router used for grouping HTTP requests under a certain URL for shared use cases
router = fastapi.APIRouter(prefix="/metadata")


@router.api_route("/{path:path}", methods=["GET", "POST"])
async def metadata_gateway(path:str, request:fastapi.Request):
    async with httpx.AsyncClient() as http:
        #the request sent to the .net backend
        response = await http.request(
            method=request.method,
            url=f"{config.METADATA_URL}/{path}",
            content=await request.body(),
            headers=request.headers
        )                  
    return fastapi.Response(content=response.content, status_code=response.status_code)
        

    async def storage_gateway(self) -> None:
        pass