from fastapi import APIRouter, HTTPException

from database import engineconn
from api.user import crud, schema

router = APIRouter()

@router.post(
    "/user",
    summary="사용자 생성",
)
async def user_create(_user_create: schema.UserCreate):
    try:
        user = crud.get_existing_user(_user_create)
        if user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다."
            )

        crud.create_user(_user_create)

        return {"code": 200, "message": "success", "data": []}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
