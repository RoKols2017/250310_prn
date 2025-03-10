import os
from dotenv import load_dotenv
import pytz

# Загружаем переменные окружения из .env
load_dotenv()

# Настройки базы данных
# Переключаемся на SQLite для тестов
USE_SQLITE = os.getenv("USE_SQLITE", "True") == "True"

if USE_SQLITE:
    DATABASE_URL = "sqlite:///./test_db.sqlite"
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/print_logs")

# Пути к папкам с журналами
WATCH_FOLDER = os.getenv("WATCH_FOLDER", "instance/new")
PROCESSED_FOLDER = os.getenv("PROCESSED_FOLDER", "instance/processed")

# Настройки планировщика
SCHEDULER_TIME = os.getenv("SCHEDULER_TIME", "03:00")  # Время запуска (HH:MM)
TIMEZONE = os.getenv("TIMEZONE", "Europe/Moscow")  # Часовой пояс

# Настройки часового пояса
TZ = pytz.timezone(TIMEZONE)
