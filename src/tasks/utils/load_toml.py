from typing import Any
from pathlib import Path
import tomllib


def load_toml(file_path: Path) -> dict[str, Any]:
    try:
        with open(file_path, 'rb') as f:
            data = tomllib.load(f)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Toml-файл по пути '{file_path}' не найден"
        ) from None

    except tomllib.TOMLDecodeError as e:
        raise ValueError(
            f"Toml-файл '{file_path}' содержит "
            f"некорректный TOML: {str(e)}"
        ) from None

    except Exception as e:
        raise RuntimeError(
            f"Ошибка загрузки toml-файла: {str(e)}"
        ) from None

    return data
