import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Setting(BaseSettings):
    STAGE = os.getenv("STAGE")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PWD = os.getenv("MYSQL_PWD")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DB = os.getenv("MYSQL_DB")

    class Config:
        env_file = ".env"


Configs = Setting()
