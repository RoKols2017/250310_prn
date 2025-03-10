import os
import shutil
from app.services.file_watcher import process_files

def test_process_files(mocker):
    mock_listdir = mocker.patch("os.listdir", return_value=["test.json"])
    mock_load_json = mocker.patch("app.services.json_loader.load_json", return_value=[{"Id": "123"}])
    mock_move = mocker.patch("shutil.move")

    process_files()

    mock_listdir.assert_called_once()  # ✅ Проверяем, что os.listdir() вызывался ровно один раз
    mock_move.assert_called_once()  # ✅ Проверяем, что shutil.move() вызывался ровно один раз
