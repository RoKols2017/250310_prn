from app.db.database import get_db

def test_database_connection():
    db = next(get_db())
    assert db is not None
