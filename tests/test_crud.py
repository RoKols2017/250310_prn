from app.db import crud, schemas
from app.models.user import User

def test_create_and_get_user(db):
    """Тестируем CRUD: создание и поиск пользователя"""
    user_data = schemas.UserCreate(username="admin", fio="Администратор", department_id=1)
    user = crud.create_user(db, user_data)

    found_user = crud.get_user(db, "admin")
    assert found_user is not None
    assert found_user.fio == "Администратор"
