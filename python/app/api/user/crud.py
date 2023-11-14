from passlib.context import CryptContext
from api.user.schema import UserCreate
from database import engineconn
from models import (
    User,
)
from datetime import datetime

engine = engineconn()
session = engine.session()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create Read Update Delete 
def create_user(user_create: UserCreate):
    db_user = User(
        user_id=user_create.user_id,
        password=pwd_context.hash(user_create.password1),
        name=user_create.name,
        location=user_create.location,
        createdAt=datetime.now().strftime(format="%Y-%m-%d %H:%M:%S"),
    )
    session.add(db_user)
    session.commit()

def get_existing_user(user_create: UserCreate):
    return session.query(User).filter(User.username == user_create.username).first()


def get_user(username: str):
    result = session.query(User).filter(User.username == username).first()
    return result