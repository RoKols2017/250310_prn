from pydantic import BaseModel
from datetime import datetime

# Схемы для Buildings
class BuildingBase(BaseModel):
    code: str
    name: str

class BuildingCreate(BuildingBase):
    pass

class BuildingResponse(BuildingBase):
    id: int

    class Config:
        from_attributes = True

# Схемы для Departments
class DepartmentBase(BaseModel):
    code: str
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True

# Схемы для Users
class UserBase(BaseModel):
    username: str
    fio: str
    department_id: int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# Схемы для Models
class ModelBase(BaseModel):
    code: str
    manufacturer: str
    model: str

class ModelCreate(ModelBase):
    pass

class ModelResponse(ModelBase):
    id: int

    class Config:
        from_attributes = True

# Схемы для Printers
class PrinterBase(BaseModel):
    model_id: int
    building_id: int
    department_id: int
    room_number: str
    printer_index: int

class PrinterCreate(PrinterBase):
    pass

class PrinterResponse(PrinterBase):
    id: int

    class Config:
        from_attributes = True

# Схемы для PrintEvents
class PrintEventBase(BaseModel):
    document_id: int
    document_name: str
    user_id: int
    printer_id: int
    timestamp: datetime
    byte_size: int
    pages: int

class PrintEventCreate(PrintEventBase):
    pass

class PrintEventResponse(PrintEventBase):
    id: int

    class Config:
        from_attributes = True
