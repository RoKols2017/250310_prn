from app.services.file_watcher import process_files
import os

def test_scheduler():
    """Проверяем, что process_files() вызывается без ошибок"""
    os.makedirs("журналы", exist_ok=True)
    os.makedirs("обработанные", exist_ok=True)

    try:
        process_files()
    except Exception as e:
        assert False, f"Ошибка в process_files: {e}"
