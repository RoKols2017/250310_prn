from sqlalchemy import Column, Integer, String
from .base import Base

class PrinterModel(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)  # Аббревиатура модели из журнала
    manufacturer = Column(String(100), nullable=False)      # Производитель (Kyocera)
    model = Column(String(50), nullable=False)              # Полное название модели (2040)
