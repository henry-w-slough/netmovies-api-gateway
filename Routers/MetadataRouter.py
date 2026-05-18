import fastapi
import httpx

import config


#the router used for grouping HTTP requests under a certain URL for shared use cases
router = fastapi.APIRouter(prefix="/metadata")


@router.api_route("/{path:path}", methods=["GET", "POST", "DELETE"])
async def metadata_gateway(path:str, request:fastapi.Request):
    
    async with httpx.AsyncClient() as http:
        response = await http.request(
            method=request.method,
            url=f"{config.METADATA_ADDRESS}/{path}",
            content=await request.body(),
            headers={"Content-Type": request.headers.get("Content-Type", "application/json")}
        )

    return fastapi.Response(content=response.content, status_code=response.status_code, media_type=response.headers.get("content-type"))

