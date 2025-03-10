import json
import os
from datetime import datetime

def load_json(file_path: str):
    """ Чтение и парсинг JSON-файла """
    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Ошибка чтения JSON: {e}")
        return None

def parse_printer_name(printer_name: str):
    """ Разбираем название принтера, например Kyocera2040-pd4-ogs-67-1 """
    try:
        parts = printer_name.split("-")
        model_code = parts[0]               # Kyocera2040
        building_code = parts[1]            # pd4
        department_code = parts[2]          # ogs
        room_number = parts[3]              # 67 (vможет быть слово zamena)
        printer_index = int(parts[4])       # 1
        return model_code, building_code, department_code, room_number, printer_index
    except Exception:
        print(f"Ошибка разбора принтера: {printer_name}")
        return None, None, None, None, None
