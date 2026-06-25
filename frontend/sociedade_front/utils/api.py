import httpx
from os import getenv
from dotenv import load_dotenv

load_dotenv()
BACKEND_URL = getenv("BACKEND_URL")


async def get(endpoint: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BACKEND_URL}{endpoint}", timeout=15)
        resp.raise_for_status()
        return resp.json()


async def post(endpoint: str, data: dict) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{BACKEND_URL}{endpoint}", json=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
