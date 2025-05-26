from typing import Any, Generic, TypeVar
from pathlib import Path
import tomllib


KT = TypeVar('KT')
VT = TypeVar('VT')


class ReadOnlyTomlData(Generic[KT, VT]):
    def __init__(self, data: dict[KT, VT], filepath: Path,
                 nested_level: list[KT] | None = None):
        self._data = data
        self._filepath = filepath
        self._nested_level = [] if nested_level is None else nested_level

    def __getitem__(self, key: KT) -> VT | 'ReadOnlyTomlData[KT, VT]':
        if key not in self._data:
            nested_level = ':'.join(map(str, self._nested_level))
            raise KeyError(
                f"В toml '{self._filepath}'[{nested_level}] отсутствует ключ '{key}'"
            )
        value = self._data[key]
        if isinstance(value, dict):
            return ReadOnlyTomlData(value, self._filepath,
                                    self._nested_level + [key])
        return value

    def __setitem__(self, key: KT, value: VT):
        raise RuntimeError(
            f"Данные только для чтения (загружены из файла: '{self._filepath}')"
        )

    def get(self, key: KT, default: VT | None = None):
        if key not in self._data:
            return default
        return self[key]

    def __contains__(self, key: KT) -> bool:
        return key in self._data

    def __iter__(self):
        for item in self._data:
            yield item

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"ReadOnlyTomlData({self._data}, filepath='{self._filepath}')"

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def to_dict(self):
        return self._data


def load_toml(file_path: Path) -> ReadOnlyTomlData[str, Any]:
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

    return ReadOnlyTomlData(data, file_path)
