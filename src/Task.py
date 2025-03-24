from abc import ABC, abstractmethod
from StoreTask import StoreTask
class Task(ABC):
    def __init__(self):
        StoreTask.register_instance(self)
        super().__init__()
    @abstractmethod
    def generate_condition_task():
        ...
        "Генерируем условаие задачи"
    
    @abstractmethod
    def generate_code_tempalte():
        ...
        "Генерируем шаблон кода"
        
    @abstractmethod
    def generate_template_coderunner():
        ...
        "Генерируем шаблон code runner"