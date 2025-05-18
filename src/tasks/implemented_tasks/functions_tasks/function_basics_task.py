import random
from tasks.implemented_tasks.task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class FunctionBasicsTask(Task):

    name = 'function_basics_task'
    description = 'Базовое знакомство с функциями'
    path_template_toml = 'function_basics_template.toml'

    def __generate_param(self, seed: int) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        params = {
            "int_ans": GeneratorTemplate.generate_int(),
            "fib_val": GeneratorTemplate.generate_int_range(1, 5),
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
