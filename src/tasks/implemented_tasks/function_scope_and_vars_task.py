import random
from tasks.implemented_tasks.task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class FunctionScopeAndVarsTask(Task):

    name = 'function_scope_and_vars_task'
    description = 'Знакомство с областью видимости переменных'
    path_template_toml = 'function_scope_and_vars_template.toml'

    def __generate_param(self, seed: int) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        params = {
            "static_plus_func": GeneratorTemplate.generate_int_range(-3, 5),
            "static_val_func": GeneratorTemplate.generate_int_range(-3, 10),
            "global_val": GeneratorTemplate.generate_int_range(-3, 10),
            "global_plus": GeneratorTemplate.generate_int_range(-3, 5),
            "static_val": GeneratorTemplate.generate_int_range(-3, 10),
            "static_plus": GeneratorTemplate.generate_int_range(-3, 5),
            "local_val": GeneratorTemplate.generate_int_range(-3, 10),
            "local_plus": GeneratorTemplate.generate_int_range(-3, 5),
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
