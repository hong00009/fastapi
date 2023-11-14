from sqlalchemy import *
from sqlalchemy.orm import *
from configs import Configs
from urllib.parse import quote_plus

config = dict(
    host=Configs.MYSQL_HOST,
    port=Configs.MYSQL_PORT,
    user=Configs.MYSQL_USER,
    password=Configs.MYSQL_PWD,
    database=Configs.MYSQL_DB,
)

for key, value in config.items():
    config[key] = quote_plus(value)

DB_URL = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8mb4"

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)

    def session(self):
        return sessionmaker(bind=self.engine)()

    def connection(self):
        return self.engine.connect()