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
            "char_ans": GeneratorTemplate.generate_char(),
            "short_ans": GeneratorTemplate.generate_short(),
            "int_ans": GeneratorTemplate.generate_int(),
            "ll_ans": GeneratorTemplate.generate_long_long(),
            "u_int_ans": GeneratorTemplate.generate_unsigned_int(),
            "double_1_ans": GeneratorTemplate.generate_double(),
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
