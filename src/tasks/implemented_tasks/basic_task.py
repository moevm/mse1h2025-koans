import random
import os
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class BasicTask(Task):

    name = 'basic_task'

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        params = {
            "char": GeneratorTemplate.generate_name(),
            "char_ans": GeneratorTemplate.generate_char(),
            "short": GeneratorTemplate.generate_name(),
            "short_ans": GeneratorTemplate.generate_short(),
            "int": GeneratorTemplate.generate_name(),
            "int_ans": GeneratorTemplate.generate_int(),
            "ll": GeneratorTemplate.generate_name(),
            "ll_ans": GeneratorTemplate.generate_long_long(),
            "u_int": GeneratorTemplate.generate_name(),
            "u_int_ans": GeneratorTemplate.generate_unsigned_int(),
            "double_1": GeneratorTemplate.generate_name(),
            "double_1_ans": GeneratorTemplate.generate_double(),
            "double_2": GeneratorTemplate.generate_name(),
            "double_2_ans": GeneratorTemplate.generate_double(),
        }

        return params

    def _generate_condition_task(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'basics_template_condition.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError('Описание задания для basic не найдено.')

        with open(task_path, 'r', encoding='utf-8') as file:
            description = file.read()

        return description

    def _generate_code_template(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'basics_template_code.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError('Код задания для basic не найдено.')

        with open(task_path, 'r', encoding='utf-8') as file:
            template = file.read()

        params = self.__generate_param(seed)

        return substitute_template(template, params)

    def _generate_template_coderunner(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'basic_template_coderunner.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError('Coderunner шаблон для basic не найден.')

        with open(task_path, "r", encoding='utf-8') as file:
            template = file.read()

        params = {'code': self._generate_code_template(seed)}
        return substitute_template(template, params)
