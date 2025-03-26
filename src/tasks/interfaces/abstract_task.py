from abc import ABC, abstractmethod


class ABCTask(ABC):

    name: str

    @abstractmethod
    def __init__(self, seed: int | None):
        ...

    @abstractmethod
    def get_seed(self):
        return self.__seed

    @abstractmethod
    def get_condition_task(self):
        ...

    @abstractmethod
    def get_code_template(self):
        ...

    @abstractmethod
    def get_template_coderunner(self):
        ...
