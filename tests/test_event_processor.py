from app.services.event_processor import process_event
from app.models.print_event import PrintEvent

def test_process_event(db_session, mocker):  # ✅ mocker должен передаваться как аргумент
    mocker.patch("app.services.json_loader.parse_printer_name", return_value=("Kyocera2040", "A1", "IT", "101", 1))

    event_data = {
        "Id": "12345",
        "Properties": [
            {"Value": "111"},  # Document ID
            {"Value": "Test Document"},  # Document Name
            {"Value": "user1"},  # Username
            {"Value": "Kyocera2040-A1-IT-101-1"},  # Printer Name
            {"Value": "500"},  # Byte Size
            {"Value": "10"}  # Pages
        ],
        "TimeCreated": "/Date(1672531199000)/"  # Timestamp
    }

    process_event(db_session, event_data)
    assert db_session.query(PrintEvent).count() == 1
