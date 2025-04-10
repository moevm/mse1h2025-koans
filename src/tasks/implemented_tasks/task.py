from abc import ABCMeta, abstractmethod
from random import randint
import tomllib
from tasks import TEMPLATES_DIR
from tasks.interfaces import ABCTask
from tasks.store_task.store_task import StoreTask
from tasks.toml_loader import TomlLoader


class TaskMeta(ABCMeta):
    """Метакласс для автоматической регистрации классов задач."""
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)

        if namespace.get('__abstract__', False):
            return

        StoreTask.register_task(cls)

        for field in cls.required_fields:
            if field not in namespace:
                raise AttributeError(
                    f"Класс {cls.__name__} должен содержать поле '{field}'"
                )


class Task(ABCTask, metaclass=TaskMeta):

    __abstract__ = True

    required_fields = [
        'name',
        'description',
        'path_template_toml'
    ]

    json_field = [
        'template_condition',
        'template_code',
        'template_coderunner'
    ]

    def __init__(self, seed: int | None = None):
        if seed is None:
            seed = randint(0, 2 ** 32 - 1)

        if seed < 0 or seed >= 2 ** 32:
            seed = abs(seed)
            seed %= 2 ** 32

        self.__seed = seed

        self._load_template()

        self.__data = {
            'condition_task': self._generate_condition_task(seed),
            'code_template': self._generate_code_template(seed),
            'template_coderunner': self._generate_template_coderunner(seed)
        }

    def _load_template(self):
        name_cls = self.__class__.__name__
        path = TEMPLATES_DIR / self.path_template_toml

        self._template = TomlLoader(path).data

        for field in self.json_field:
            if field not in self._template:
                raise ValueError(
                    f"{name_cls}: Файл '{path}' "
                    f'не содержит {field}'
                )

    @abstractmethod
    def _generate_condition_task(self, seed: int) -> str:
        ...

    @abstractmethod
    def _generate_code_template(self, seed: int) -> str:
        ...

    @abstractmethod
    def _generate_template_coderunner(self, seed: int) -> str:
        ...

    def get_seed(self):
        return self.__seed

    def get_condition_task(self):
        return self.__data['condition_task']

    def get_code_template(self):
        return self.__data['code_template']

    def get_template_coderunner(self):
        return self.__data['template_coderunner']
