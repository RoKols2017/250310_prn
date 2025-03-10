from app.services.json_loader import parse_printer_name

def test_parse_printer_name():
    """Проверяем, что принтер разбирается корректно"""
    printer_str = "Kyocera2040-pd4-ogs-67-1"
    model_code, building_code, department_code, room_number, printer_index = parse_printer_name(printer_str)

    assert model_code == "Kyocera2040"
    assert building_code == "pd4"
    assert department_code == "ogs"
    assert room_number == 67
    assert printer_index == 1
