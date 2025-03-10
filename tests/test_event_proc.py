from app.services.event_processor import process_event
from app.db.schemas import PrintEventCreate
from datetime import datetime

def test_process_event(db):
    """Тестируем обработку события печати"""
    test_event = {
        "Properties": [
            {"Value": "101"},  # document_id
            {"Value": "Документ.docx"},  # document_name
            {"Value": "testuser"},  # user
            {}, {},  # Пропускаем ненужные свойства
            {"Value": "Kyocera2040-pd4-ogs-67-1"},  # printer_name
            {"Value": "125000"},  # byte_size
            {"Value": "2"},  # pages
        ],
        "TimeCreated": "/Date(1700000000000)/"  # UNIX timestamp
    }

    process_event(db, test_event)
    event_in_db = db.query(PrintEventCreate).first()

    assert event_in_db is not None
    assert event_in_db.document_name == "Документ.docx"
    assert event_in_db.byte_size == 125000
    assert event_in_db.pages == 2
