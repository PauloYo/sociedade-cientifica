import httpx

BACKEND_URL = "http://localhost:8000"


async def get(endpoint: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BACKEND_URL}{endpoint}", timeout=15)
        resp.raise_for_status()
        return resp.json()
