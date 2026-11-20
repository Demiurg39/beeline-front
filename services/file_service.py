import pandas as pd
from typing import Tuple, Optional


class FileService:
    @staticmethod
    def validate_csv(uploaded_file) -> Tuple[bool, str, Optional[pd.DataFrame]]:
        if uploaded_file is None:
            return False, "Файл не загружен.", None

        if not uploaded_file.name.endswith('.csv'):
            return False, "Неверный формат. Ожидается CSV.", None

        try:
            df = pd.read_csv(uploaded_file)

            if df.empty:
                return False, "Файл пустой.", None

            required = {'date', 'type', 'amount'}
            if not required.issubset(df.columns):
                return False, f"Отсутствуют столбцы: {', '.join(required - set(df.columns))}", None

            return True, "Успешно.", df
        except Exception as e:
            return False, f"Ошибка чтения: {str(e)}", None