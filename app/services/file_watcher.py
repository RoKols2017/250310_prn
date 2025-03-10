import os
import shutil
from sqlalchemy.orm import Session
from app.services.json_loader import load_json
from app.services.event_processor import process_event
from app.db.database import SessionLocal
from config import WATCH_FOLDER, PROCESSED_FOLDER


def process_files():
    """Проверяет наличие новых файлов и обрабатывает их"""
    files = [f for f in os.listdir(WATCH_FOLDER) if f.endswith(".json")]

    if not files:
        print("Нет новых файлов для обработки.")
        return

    db: Session = SessionLocal()

    for file in files:
        file_path = os.path.join(WATCH_FOLDER, file)
        data = load_json(file_path)

        if data:
            for event in data:
                process_event(db, event)

        # Перемещаем обработанный файл
        shutil.move(file_path, os.path.join(PROCESSED_FOLDER, file))
        print(f"Файл {file} обработан и перемещен в {PROCESSED_FOLDER}")

    db.close()
