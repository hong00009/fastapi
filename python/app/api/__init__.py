from api.user import user_router
from fastapi import APIRouter

router = APIRouter()

routers = [
    (router, dict(prefix="/api", tags=["User"])),
    (user_router, dict(prefix="/api/auth", tags=["User"])),
]