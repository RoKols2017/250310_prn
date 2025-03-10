from sqlalchemy.orm import Session
from app.models import building, department, user, model, printer, print_event
from app.db import schemas

# CRUD для Buildings
def get_building(db: Session, code: str):
    return db.query(building.Building).filter(building.Building.code == code).first()

def create_building(db: Session, building_data: schemas.BuildingCreate):
    db_building = building.Building(**building_data.dict())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building

# CRUD для Departments
def get_department(db: Session, code: str):
    return db.query(department.Department).filter(department.Department.code == code).first()

def create_department(db: Session, department_data: schemas.DepartmentCreate):
    db_department = department.Department(**department_data.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

# CRUD для Users
def get_user(db: Session, username: str):
    return db.query(user.User).filter(user.User.username == username).first()

def create_user(db: Session, user_data: schemas.UserCreate):
    db_user = user.User(**user_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# CRUD для Models
def get_model(db: Session, code: str):
    return db.query(model.PrinterModel).filter(model.PrinterModel.code == code).first()

def create_model(db: Session, model_data: schemas.ModelCreate):
    db_model = model.PrinterModel(**model_data.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

# CRUD для Printers
def get_printer(db: Session, model_id: int, building_id: int, department_id: int, room_number: str, printer_index: int):
    return db.query(printer.Printer).filter(
        printer.Printer.model_id == model_id,
        printer.Printer.building_id == building_id,
        printer.Printer.department_id == department_id,
        printer.Printer.room_number == room_number,
        printer.Printer.printer_index == printer_index
    ).first()

def create_printer(db: Session, printer_data: schemas.PrinterCreate):
    db_printer = printer.Printer(**printer_data.dict())
    db.add(db_printer)
    db.commit()
    db.refresh(db_printer)
    return db_printer

# CRUD для PrintEvents
def get_print_event(db: Session, document_id: int, user_id: int, printer_id: int, timestamp: str):
    return db.query(print_event.PrintEvent).filter(
        print_event.PrintEvent.document_id == document_id,
        print_event.PrintEvent.user_id == user_id,
        print_event.PrintEvent.printer_id == printer_id,
        print_event.PrintEvent.timestamp == timestamp
    ).first()

def create_print_event(db: Session, event_data: schemas.PrintEventCreate):
    db_event = print_event.PrintEvent(**event_data.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
