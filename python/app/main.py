# python/app/main.py
from fastapi import FastAPI, APIRouter
from mangum import Mangum

app = FastAPI(
    title="Notice Project",
    description="Notice Project",
    version="0.1.0",
    root_path="/v1",
)

api_router = APIRouter(prefix="/api")


@app.get("/")
async def root():
    return {"code": 200, "message": "Hello World", "data": None}

app.include_router(api_router)

handler = Mangum(app)