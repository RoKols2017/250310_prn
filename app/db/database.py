from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.base import Base
from config import DATABASE_URL, USE_SQLITE
import os

# Настройки для SQLite
connect_args = {"check_same_thread": False} if USE_SQLITE else {}

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Создание таблиц в БД
def init_db():
    Base.metadata.create_all(bind=engine)
