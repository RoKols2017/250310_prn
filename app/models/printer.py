from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Printer(Base):
    __tablename__ = "printers"

    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("models.id"), nullable=False)
    building_id = Column(Integer, ForeignKey("buildings.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    room_number = Column(String(10), nullable=False)
    printer_index = Column(Integer, nullable=False)

    model = relationship("PrinterModel")
    building = relationship("Building")
    department = relationship("Department")
