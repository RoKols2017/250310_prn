from app.services.file_watcher import process_files
from app.db.database import init_db

if __name__ == "__main__":
    init_db()  # Создаем таблицы, если их нет
    process_files()
