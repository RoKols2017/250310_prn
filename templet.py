import json
from datetime import datetime, timezone, timedelta

# Укажите путь к файлу
file_path = "instance/new/PrintedEvents_20250310_091753.json"

# Читаем данные из файла, используя utf-8-sig для корректной обработки BOM
with open(file_path, "r", encoding="utf-8-sig") as file:
    events = json.load(file)

# Часовой пояс UTC+3
tz_offset = timezone(timedelta(hours=3))

# Счетчики
total_jobs = 0  # Количество заданий печати
total_pages = 0  # Общее количество напечатанных страниц

# Выводим на печать каждое событие
for event in events:
    # Преобразование времени
    timestamp_ms = int(event['TimeCreated'][6:-2])  # Убираем "/Date(" и ")/"
    dt = datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)  # Время в UTC
    dt = dt.astimezone(tz_offset)  # Перевод в UTC+3
    formatted_time = dt.strftime("%d-%m-%Y %S:%M:%H")  # Измененный формат даты

    # Извлекаем данные о документе
    job_id = event['Id']
    user = event['Properties'][2]['Value']
    computer = event['Properties'][3]['Value']
    printer = event['Properties'][4]['Value']
    document = event['Properties'][1]['Value']
    pages = int(event['Properties'][7]['Value'])  # Количество страниц

    # Обновляем счетчики
    total_jobs += 1
    total_pages += pages

    # Вывод информации о событии
    print(f"ID события: {job_id}")
    print(f"Дата и время (UTC+3): {formatted_time}")
    print(f"Пользователь: {user}")
    print(f"Компьютер: {computer}")
    print(f"Принтер: {printer}")
    print(f"Документ: {document}")
    print(f"Страниц: {pages}")
    print("-" * 80)

# Вывод статистики
print(f"Всего заданий печати: {total_jobs}")
print(f"Всего страниц напечатано: {total_pages}")
