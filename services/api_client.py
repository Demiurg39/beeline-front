# services/api_client.py
import requests
from typing import Dict, Any, Optional

class ApiClient:
    BASE_URL = "http://localhost:8000/api"

    @staticmethod
    def _request(method: str, endpoint: str, json_data: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{ApiClient.BASE_URL}{endpoint}"
        try:
            response = requests.request(method, url, json=json_data, timeout=10)
            response.raise_for_status()  # Вызовет исключение при 4xx/5xx
            return response.json()
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Не удалось подключиться к серверу. Убедитесь, что бэкенд запущен на localhost:8000.")
        except requests.exceptions.HTTPError as e:
            # Пытаемся достать сообщение об ошибке из JSON (формат из спецификации)
            error_data = e.response.json() if e.response.text else {}
            error_msg = error_data.get("message", str(e))
            raise ValueError(f"Ошибка API: {error_msg}")
        except requests.exceptions.Timeout:
            raise TimeoutError("Сервер не отвечает. Попробуйте позже.")

    @staticmethod
    def get_catalog() -> Dict[str, Any]:
        """Получить все справочники (тарифы, доппакеты, абоненты)."""
        return ApiClient._request("GET", "/catalog")

    @staticmethod
    def recommend_by_subscriber(subscriber_id: str, include_explanation: bool = True) -> Dict[str, Any]:
        """Быстрый расчет по готовому абоненту (P01..P10)."""
        payload = {"subscriber_id": subscriber_id, "include_explanation": include_explanation}
        return ApiClient._request("POST", "/recommend", payload)