from passlib.context import CryptContext
from api.user.schema import UserCreate, UserDelete, PostCreate
from database import engineconn
from models import (
    User, Post
)
from datetime import datetime

engine = engineconn()
session = engine.session()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create Read Update Delete 
def create_user(user_create: UserCreate):
    # UserCreate 클래스
    # account: str
    # password1: str
    # password2: str
    # name: str
    # location: str
    # user_type: str
    # createAt: datetime
    
    # User 클래스
    # id = Column(INTEGER, primary_key=True)  # 사용자 고유번호
    # account = Column(String(255))  # 계정/ID
    # password = Column(String(255))  # 비밀번호
    # name = Column(String(255))  # 이름
    # user_type = Column(CHAR(1))  # 회원유형 0일반회원/1기업회원
    # createdAt = Column(DateTime)  # 가입일자
    # location = Column(String(255))  # 근무지

    db_user = User(  # db에 저장할 정보
        account=user_create.account,
        password=pwd_context.hash(user_create.password1),
        name=user_create.name,
        user_type=user_create.user_type,
        createdAt=datetime.now().strftime(format="%Y-%m-%d %H:%M:%S"),
        location=user_create.location,
    )
    session.add(db_user)
    session.commit()

def get_existing_user(user_create: UserCreate):
    return session.query(User).filter(User.account == user_create.account).first()


def get_user(account: str):
    result = session.query(User).filter(User.account == account).first()
    return result


# 회원탈퇴 
def delete_user(user_delete: UserDelete):
    session.query(User).filter(User.account == user_delete.account).delete()
    session.commit()
    
# 게시물 작성
def create_post(post_create: PostCreate):
    # PostCreate 클래스
    # ahthor_id: int
    # title: str
    # content: str
    # createdAt: datetime
    # career: str
    # edu: str
    # start_date: datetime
    # end_date: datetime
    # is_public: str
    # analyze_result: str
    # use_template: str
    # category: str

    # Post 모델클래스
    # post_id = Column(INTEGER, primary_key=True)  # 게시물 고유번호
    # author_id = Column(INTEGER, ForeignKey(User.id))  #  작성자id
    # title = Column(String(255))  # 게시물 제목
    # content = Column(Text)  # 게시물 내용
    # createdAt = Column(DateTime)  # 게시물작성일
    # career = Column(CHAR(1))  # 경력: 경력무관0,신입1,경력2
    # edu = Column(CHAR(1))  # 최종학력: 학력무관0,고졸1,초대졸2,대졸3,석사4,박사5
    # start_date = Column(DateTime)  # 채용접수 시작일
    # end_date = Column(DateTime)  # 채용접수 마감일
    # is_public = Column(Boolean)  # 게시물 공개/비공개 여부
    # analyze_result = Column(Text)  # 분석결과(직무12가지 퍼센티지%)
    # use_template = Column(Boolean)  # 직무 템플릿 사용/비사용(커스텀)

    db_post = Post(
        # author_id=
        # title=post_create
        # content=post_create
        createdAt=datetime.now().strftime(format="%Y-%m-%d %H:%M:%S"),
        # career=post_create
        # edu=post_create
        # start_date=post_create
        # end_date=post_create
        # is_public=post_create
        # analyze_result=post_create
        # use_template=post_create.
    )

    session.add(db_post)
    session.commit()
