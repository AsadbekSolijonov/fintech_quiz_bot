from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from bot.config import settings as stt

DB_DIALECT = f'postgresql+psycopg2://{stt.DB_USER}:{stt.DB_PASSWORD}@{stt.DB_HOST}:{stt.DB_PORT}/{stt.DB_NAME}'
engine = create_engine(
    DB_DIALECT,
    echo=True,
    pool_pre_ping=True,  # o'lik connectionlarni aniqlash
    poolclass=NullPool  # har bir session uchun alohida connection
)
