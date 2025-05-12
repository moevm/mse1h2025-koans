import random
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class PointersAndAddressesTask(Task):
    name = 'pointers_and_addresses_task'
    description = 'Знакомство с указателями и адресами'
    path_template_toml = 'pointers_and_addresses_template.toml'

    def __generate_param(self, seed: int) -> dict[str, str]:
        random.seed(seed)
        params = {
            "int_val": GeneratorTemplate.generate_int(),
            "another_int_val": GeneratorTemplate.generate_int(),
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