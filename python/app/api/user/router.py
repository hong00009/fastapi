from fastapi import APIRouter, HTTPException, status # status 추가

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

@router.get("/user/me",
    summary="현재 사용자정보 출력",
)
async def read_me():
    return {'account': '현재 접속중'}

# @router.get(
#     "/logout",
#     summary="로그아웃",
# )
# async def logout(_logout: schema.Logout):
#     try:
#         response = templates.TemplateResponse(
#             "login.html", {"code": 200, "message": "logout success", "data":_logout}
#         )
#         return response

#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)



# @router.patch(
#     "/user",
#     summary="정보변경",
# )
# async def user_update(_user_update: schema.UserUpdate):
#     try:
#         user = crud.get_existing_user(_user_create)
#         if user:
#             raise HTTPException(
#                 status_code=status.HTTP_409_CONFLICT, detail="내용3"
#             )

#         crud.create_user(_user_create)

#         return {"code": 200, "message": "success", "data": []}
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)




@router.delete(
    "/user",
    summary="탈퇴",
)
async def user_delete(_user_delete: schema.UserDelete):
    # 탈퇴과정
    # 1. 탈퇴할 계정으로 로그인한 상태 > ? 
    # 2. 탈퇴요청
    # 3. db account,password일치여부 확인
    # 4. db 삭제
    try:
        user = crud.get_existing_user(_user_delete)
        if user:
            crud.delete_user(_user_delete)

        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="유저없음"
            )


        return {"code": 200, "message": "delete success", "data": []}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)



@router.post(
    "/post",
    summary="게시물 작성",
)
async def post_create(_post_create: schema.PostCreate):
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