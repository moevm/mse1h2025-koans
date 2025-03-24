from abc import ABC, ABCMeta, abstractmethod
from random import randint
from store_task import StoreTask


class TaskMeta(ABCMeta):
    """Метакласс для автоматической регистрации классов задач."""
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if not namespace.get('__abstract__', False):
            StoreTask.register_task(cls)


class Task(ABC, metaclass=TaskMeta):

    __abstract__ = True

    def __init__(self, seed: int | None = None):
        if seed is None:
            seed = randint(0, 2 ** 32 - 1)

        if seed < 0 or seed >= 2 ** 32:
            seed = abs(seed)
            seed %= 2 ** 32

        self.__seed = seed

        self.__data = {
            'condition_task': self._generate_condition_task(seed),
            'code_template': self._generate_code_template(seed),
            'template_coderunner': self._generate_template_coderunner(seed)
        }

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
