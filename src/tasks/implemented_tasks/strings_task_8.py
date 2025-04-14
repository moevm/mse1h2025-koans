import random
import os
import tomllib
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class StringsTask8(Task):

    name = 'strings_task_8'

    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, "strings", "strings.toml")
    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        format_8_1 = GeneratorTemplate.generate_string(
            self.config['strings_4']
        )
        format_8_2 = GeneratorTemplate.generate_string(
            self.config['strings_4']
        )
        len_string_8 = str(len(format_8_1) + len(format_8_2) + 5)

        params = {
            # Test 8: formating_strings
            "format_8_1": format_8_1,
            "format_8_2": format_8_2,
            "len_string_8": len_string_8,
        }

        return params

    def _generate_condition_task(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'strings_template_condition.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError(
                'Описание задания для strings_8 не найдено.'
            )

        with open(task_path, 'r', encoding='utf-8') as file:
            description = file.read()

        return description

    def _generate_code_template(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'strings_8_template_code.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError('Код задания для strings_8 не найдено.')

        with open(task_path, 'r', encoding='utf-8') as file:
            template = file.read()

        params = self.__generate_param(seed)

        return substitute_template(template, params)

    def _generate_template_coderunner(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'basic_template_coderunner.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError(
                'Coderunner шаблон для strings_8 не найден.'
            )

        with open(task_path, "r", encoding='utf-8') as file:
            template = file.read()

        params = {'code': self._generate_code_template(seed)}
        return substitute_template(template, params)
