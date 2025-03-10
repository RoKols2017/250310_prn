from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, time
import pytz
from app.services.file_watcher import process_files
from config import SCHEDULER_TIME, TZ

scheduler = BlockingScheduler(timezone=str(TZ))  # Указываем часовой пояс

# Конвертируем строку "HH:MM" в объект времени
hour, minute = map(int, SCHEDULER_TIME.split(":"))
scheduled_time = time(hour=hour, minute=minute)

# Запускаем задачу раз в сутки по московскому времени
scheduler.add_job(process_files, "cron", hour=scheduled_time.hour, minute=scheduled_time.minute)

if __name__ == "__main__":
    print(f"📅 Планировщик запущен. Следующий запуск: {SCHEDULER_TIME} {TZ.zone} каждый день.")
    scheduler.start()
