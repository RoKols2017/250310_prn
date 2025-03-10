from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class PrintEvent(Base):
    __tablename__ = "print_events"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, nullable=False, index=True)
    document_name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    printer_id = Column(Integer, ForeignKey("printers.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    byte_size = Column(Integer, nullable=False)
    pages = Column(Integer, nullable=False)

    user = relationship("User")
    printer = relationship("Printer")
