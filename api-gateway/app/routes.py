from fastapi import APIRouter, Request
import httpx

router = APIRouter()
services = {
    "auth": "http://auth-service:8000",
    "product": "http://product-service:8001",
    "cart": "http://cart-service:8002",
    "order": "http://order-service:8003",
    "payment": "http://payment-service:8004",
    "review": "http://review-service:8005"
}

@router.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):
    if service not in services:
        return {"error": "Unknown service"}

    async with httpx.AsyncClient() as client:
        url = f"{services[service]}/{path}"
        headers = dict(request.headers)
        method = request.method.lower()
        body = await request.body()
        response = await client.request(method, url, headers=headers, content=body)

    return response.json()
