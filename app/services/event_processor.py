from sqlalchemy.orm import Session
from datetime import datetime
import pytz
from app.db import crud, schemas
from app.services.json_loader import parse_printer_name
from config import TZ


def process_event(db: Session, event: dict):
    """Обработка одного события печати"""

    # Разбор имени принтера
    model_code, building_code, department_code, room_number, printer_index = parse_printer_name(
        event["Properties"][4]["Value"])

    if not all([model_code, building_code, department_code, room_number, printer_index]):
        print(f"Ошибка разбора принтера для события {event['Id']}")
        return

    # Проверяем и создаем объекты (здания, отделы, пользователи, принтеры)
    db_building = crud.get_building(db, building_code) or crud.create_building(db, schemas.BuildingCreate(
        code=building_code, name="Неизвестно"))
    db_department = crud.get_department(db, department_code) or crud.create_department(db, schemas.DepartmentCreate(
        code=department_code, name="Неизвестно"))
    db_model = crud.get_model(db, model_code) or crud.create_model(db, schemas.ModelCreate(code=model_code,
                                                                                           manufacturer="Неизвестно",
                                                                                           model="Неизвестно"))

    db_printer = crud.get_printer(db, db_model.id, db_building.id, db_department.id, room_number, printer_index) or \
                 crud.create_printer(db, schemas.PrinterCreate(
                     model_id=db_model.id,
                     building_id=db_building.id,
                     department_id=db_department.id,
                     room_number=str(room_number),
                     printer_index=printer_index
                 ))

    username = event["Properties"][2]["Value"]
    fio = "Неизвестно"
    db_user = crud.get_user(db, username) or crud.create_user(db, schemas.UserCreate(username=username, fio=fio,
                                                                                     department_id=db_department.id))

    # Конвертируем timestamp события в часовой пояс Москвы
    timestamp_utc = datetime.utcfromtimestamp(int(event["TimeCreated"][6:-2]) / 1000)
    timestamp_moscow = timestamp_utc.replace(tzinfo=pytz.utc).astimezone(TZ)

    document_id = int(event["Properties"][0]["Value"])
    document_name = event["Properties"][1]["Value"]
    byte_size = int(event["Properties"][6]["Value"])
    pages = int(event["Properties"][7]["Value"])

    # Проверяем, существует ли событие
    existing_event = crud.get_print_event(db, document_id, db_user.id, db_printer.id, timestamp_moscow)
    if existing_event:
        print(f"Событие {document_id} уже существует в базе.")
        return

    # Записываем событие в БД
    crud.create_print_event(db, schemas.PrintEventCreate(
        document_id=document_id,
        document_name=document_name,
        user_id=db_user.id,
        printer_id=db_printer.id,
        timestamp=timestamp_moscow,
        byte_size=byte_size,
        pages=pages
    ))

    print(f"✅ Добавлено новое событие печати: {document_id} ({timestamp_moscow.strftime('%Y-%m-%d %H:%M:%S %Z')})")
