import random
import os
import tomllib
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate
from tasks import SETTINGS_DIR


class StringsAssignment(Task):

    config_path = (
        SETTINGS_DIR / "settings_strings_task" / "strings_variables.toml"
    )
    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    name = 'strings_assignment'
    description = '...'
    path_template_toml = 'strings_assignment.toml'

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        params = {
            # Test 3: assignment
            "string_3": GeneratorTemplate.generate_string(
                self.config['strings_1']
            ),
            "index_3_1": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_3_2": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_3_3": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_3_4": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "char_3_1": GeneratorTemplate.generate_char(),
            "char_3_2": GeneratorTemplate.generate_char(),
            "char_3_3": GeneratorTemplate.generate_char(),
        }

        return params

    def _generate_condition_task(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'strings_template_condition.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError(
                'Описание задания для strings_3 не найдено.'
            )

        with open(task_path, 'r', encoding='utf-8') as file:
            description = file.read()

        return description

    def _generate_code_template(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'strings_3_template_code.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError('Код задания для strings_3 не найдено.')

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
                'Coderunner шаблон для strings_3 не найден.'
            )

        with open(task_path, "r", encoding='utf-8') as file:
            template = file.read()

        params = {'code': self._generate_code_template(seed)}
        return substitute_template(template, params)
