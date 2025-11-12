from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

DB_NAME = 'fintech_db'
DB_USER = 'postgres'
DB_PASSWORD = '1234'
DB_HOST = 'localhost'
DB_PORT = '5436'

DB_DIALECT = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(
    DB_DIALECT,
    echo=True,
    pool_pre_ping=True,  # o'lik connectionlarni aniqlash
    poolclass=NullPool  # har bir session uchun alohida connection
)
