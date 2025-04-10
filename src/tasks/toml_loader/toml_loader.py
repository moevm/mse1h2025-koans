from typing import Any
import tomllib
from pathlib import Path


class TomlLoader:

    def __init__(self, file_path: Path):
        self.__path = file_path
        self.__config: dict[str, Any] | None = None

    @property
    def data(self) -> dict[str, Any] | None:
        name_cls = self.__class__.__name__
        path = self.__path

        if self.__config is None:
            try:
                with open(self.__path, 'rb') as f:
                    self.__config = tomllib.load(f)
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"{name_cls}: Toml-файл по пути '{path}' не найден"
                ) from None

            except tomllib.TOMLDecodeError as e:
                raise ValueError(
                    f"{name_cls}: Toml-файл '{path}' содержит "
                    f"некорректный TOML: {str(e)}"
                ) from None

            except Exception as e:
                raise RuntimeError(
                    f"{name_cls}: Ошибка загрузки toml-файла: {str(e)}"
                ) from None

        return self.__config
