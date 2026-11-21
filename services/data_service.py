import json
import os
from typing import List, Tuple, Dict
from models.tariff import Tariff, Addon
from services.api_client import ApiClient

class DataService:
    @staticmethod
    def load_tariffs() -> Tuple[List[Tariff], str]:
        filepath = "data/tariffs.json" # Убедитесь, что файл так называется
        if not os.path.exists(filepath):
            return [], f"Файл не найден: {filepath}"
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                tariffs_data = data.get("tariffs", [])
                tariffs = [Tariff.from_dict(item) for item in tariffs_data]
                return tariffs, ""
        except Exception as e:
            return [], f"Ошибка при чтении тарифов: {str(e)}"

    @staticmethod
    def load_addons() -> Tuple[List[Addon], str]:
        filepath = "data/addons.json" # Убедитесь, что файл так называется
        if not os.path.exists(filepath):
            return [], f"Файл не найден: {filepath}"
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                addons = [Addon.from_dict(item) for item in data]
                return addons, ""
        except Exception as e:
            return [], f"Ошибка при чтении доппакетов: {str(e)}"

    @staticmethod
    def get_tariff_name(tariff_id: str) -> str:
        """Возвращает название тарифа по ID (T01 -> 'Старт')."""
        # Пытаемся взять из API
        try:
            catalog = ApiClient.get_catalog()
            for t in catalog["tariffs"]:
                if t["id"] == tariff_id:
                    return t["name"]
        except Exception:
            pass # Если API нет, идем в fallback

        # Fallback (локальный словарь)
        fallback_names = {"T01": "Старт", "T02": "Комфорт", "T03": "Онлайн", "T04": "Ночной", "T05": "Максимум"}
        return fallback_names.get(tariff_id, tariff_id)