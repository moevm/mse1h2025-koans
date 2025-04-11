import random
import os
import tomllib
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class StringsTask(Task):

    name = 'strings_task'

    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, "strings", "strings.toml")
    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        string_array_4, string_4 = GeneratorTemplate.generate_string_and_array(
            self.config['strings_1']
        )

        string_5 = GeneratorTemplate.generate_string(
            self.config['strings_1']
        )
        len_string_5 = str(len(string_5))

        string_6 = GeneratorTemplate.generate_string(
            self.config['strings_1']
        )
        len_stirng_6 = str(len(string_6))

        format_8_1 = GeneratorTemplate.generate_string(
            self.config['strings_4']
        )
        format_8_2 = GeneratorTemplate.generate_string(
            self.config['strings_4']
        )
        len_string_8 = str(len(format_8_1) + len(format_8_2) + 5)

        params = {
            # Test 1: what_is_string
            "string_1": GeneratorTemplate.generate_string(
                self.config['strings_1']
            ),
            "index_1": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),

            # Test 2: reference_characters
            "string_2": GeneratorTemplate.generate_string(
                self.config['strings_1']
            ),
            "index_2_1": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_2_2": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_2_3": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_2_4": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),

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

            # Test 4: declaration
            "string_array_4": string_array_4,
            "string_4": string_4,

            # Test 5: sizeof_strlen
            "string_array_5_1": GeneratorTemplate.generate_array_string(
                self.config['strings_2']
            ),
            "string_ptr_5": GeneratorTemplate.generate_string(
                self.config['strings_1']
            ),
            "string_5": string_5,
            "len_string_5": len_string_5,

            # Test 6: copy
            "string_6": string_6,
            "len_string_6": len_stirng_6,
            "index_6": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "char_6": GeneratorTemplate.generate_char(),

            # Test 7: function_paramater
            "func_param_string_7": GeneratorTemplate.generate_array_string(
                self.config['strings_3']
            ),

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
            raise FileNotFoundError('Описание задания для strings не найдено.')

        with open(task_path, 'r', encoding='utf-8') as file:
            description = file.read()

        return description

    def _generate_code_template(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'strings_template_code.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError('Код задания для strings не найдено.')

        with open(task_path, 'r', encoding='utf-8') as file:
            template = file.read()

        params = self.__generate_param(seed)

        return substitute_template(template, params)

    def _generate_template_coderunner(self, seed: int) -> str:
        base_path = os.path.dirname(__file__)
        task_path = os.path.join(base_path, 'templates',
                                 'basic_template_coderunner.txt')

        if not os.path.exists(task_path):
            raise FileNotFoundError('Coderunner шаблон для strings не найден.')

        with open(task_path, "r", encoding='utf-8') as file:
            template = file.read()

        params = {'code': self._generate_code_template(seed)}
        return substitute_template(template, params)