import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.db.database import get_db

# Подключаем in-memory SQLite для тестирования
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    """Создает новую тестовую БД для каждого теста."""
    Base.metadata.create_all(bind=engine)  # Создаем таблицы
    session = TestingSessionLocal()
    yield session  # Передаем сессию в тест
    session.close()
    Base.metadata.drop_all(bind=engine)  # Чистим БД после теста
