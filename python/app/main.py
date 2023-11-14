# python/app/main.py
from fastapi import FastAPI
from api import routers
from mangum import Mangum
from api.user.router import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Notice Project",
    description="Notice Project",
    version="0.1.0",
    root_path="/v1",
)

# api_router = APIRouter(prefix="/api")


@app.get("/")
async def root():
    return {"code": 200, "message": "Hello World", "data": None}

for router, kwargs in routers:
    app.include_router(router=router, **kwargs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)