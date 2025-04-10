import random
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class BasicTask(Task):

    name = 'basic_task'
    description = 'Базовое задание на сравнение чисел'
    path_template_toml = 'basic_template.toml'

    def __generate_param(self, seed: int) -> dict[str, str]:
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
        description = self._template['template_condition']
        return description

    def _generate_code_template(self, seed: int) -> str:
        template = self._template['template_code']
        params = self.__generate_param(seed)
        return substitute_template(template, params)

    def _generate_template_coderunner(self, seed: int) -> str:
        template = self._template['template_coderunner']
        params = {'code': self._generate_code_template(seed)}
        return substitute_template(template, params)
