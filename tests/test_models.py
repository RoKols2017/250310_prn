from app.models.user import User
from app.models.department import Department

def test_create_user(db):
    """Тестируем создание пользователя в БД"""
    department = Department(code="IT", name="IT-отдел")
    db.add(department)
    db.commit()

    user = User(username="testuser", fio="Тестовый Пользователь", department_id=department.id)
    db.add(user)
    db.commit()

    user_in_db = db.query(User).filter_by(username="testuser").first()
    assert user_in_db is not None
    assert user_in_db.fio == "Тестовый Пользователь"
