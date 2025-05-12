from abc import ABC, abstractmethod
from random import randint


class ABCTask(ABC):

    name: str
    description: str

    def __init__(self, seed: int | None = None):
        if seed is None:
            seed = randint(0, 2 ** 32 - 1)

        if seed < 0 or seed >= 2 ** 32:
            seed = abs(seed)
            seed %= 2 ** 32

        self._seed = seed

    def get_seed(self):
        return self._seed

    @abstractmethod
    def get_condition_task(self):
        ...

    @abstractmethod
    def get_code_template(self):
        ...

    @abstractmethod
    def get_template_coderunner(self):
        ...
