from app.services.json_loader import load_json, parse_printer_name

def test_load_json(mocker):
    mocker.patch("builtins.open", mocker.mock_open(read_data='{"Id": "123"}'))
    data = load_json("test.json")
    assert data["Id"] == "123"

def test_parse_printer_name():
    parsed = parse_printer_name("Kyocera2040-A1-IT-101-1")
    assert parsed == ("Kyocera2040", "A1", "IT", "101", 1)
