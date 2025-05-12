import random
from src.tasks.implemented_tasks.task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class FunctionPointersTask(Task):
    name = 'function_pointers_task'
    description = 'Указатели на функции'
    path_template_toml = 'function_pointers_template.toml'

    def __generate_param(self, seed: int) -> dict[str, str]:
        random.seed(seed)
        params = {
            "val1": GeneratorTemplate.generate_int_range(1, 10),
            "val2": GeneratorTemplate.generate_int_range(1, 10),
            "val3": GeneratorTemplate.generate_int_range(1, 10),
        }
        return params

    def _generate_condition_task(self, seed: int) -> str:
        return self._template['template_condition']

    def _generate_code_template(self, seed: int) -> str:
        template = self._template['template_code']
        params = self.__generate_param(seed)
        return substitute_template(template, params)

    def _generate_template_coderunner(self, seed: int) -> str:
        template = self._template['template_coderunner']
        params = {'code': self._generate_code_template(seed)}
        return substitute_template(template, params)