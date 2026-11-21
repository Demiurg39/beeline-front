# services/data_service.py
import json
import os
from typing import List, Tuple
from models.tariff import Tariff, Addon

class DataService:
    @staticmethod
    def load_tariffs() -> Tuple[List[Tariff], str]:
        filepath = "data/tariffs (3).json"
        if not os.path.exists(filepath):
            return [], f"Файл не найден: {filepath}"
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                # В файле корневой элемент - объект с ключом "tariffs"
                tariffs_data = data.get("tariffs", [])
                tariffs = [Tariff.from_dict(item) for item in tariffs_data]
                return tariffs, ""
        except Exception as e:
            return [], f"Ошибка при чтении тарифов: {str(e)}"

    @staticmethod
    def load_addons() -> Tuple[List[Addon], str]:
        filepath = "data/addons (3).json"
        if not os.path.exists(filepath):
            return [], f"Файл не найден: {filepath}"
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                addons = [Addon.from_dict(item) for item in data]
                return addons, ""
        except Exception as e:
            return [], f"Ошибка при чтении доппакетов: {str(e)}"