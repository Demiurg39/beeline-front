import json
import os
from typing import List, Tuple
from models.tariff import Tariff


class DataService:
    @staticmethod
    def load_mock_tariffs() -> Tuple[List[Tariff], str]:
        filepath = "data/mock_tariffs.json"

        if not os.path.exists(filepath):
            return [], f"Файл не найден: {filepath}"

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                tariffs = [Tariff.from_dict(item) for item in data]
                return tariffs, ""
        except Exception as e:
            return [], f"Ошибка при чтении: {str(e)}"