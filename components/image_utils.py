import base64

def get_image_base64(path: str) -> str:
    """Читает картинку и возвращает строку base64 для вставки в HTML."""
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        return "" # Если файла нет, вернем пустоту