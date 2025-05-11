import random
import tomllib
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate
from tasks import SETTINGS_DIR


class StringsDeclaration(Task):

    config_path = (
        SETTINGS_DIR / "settings_strings_task" / "strings_variables.toml"
    )
    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    name = 'strings_declaration'
    description = '...'
    path_template_toml = 'strings_declaration.toml'

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        string_array_4, string_4 = GeneratorTemplate.generate_string_and_array(
            self.config['strings_1']
        )

        params = {
            # Test 4: declaration
            "string_array_4": string_array_4,
            "string_4": string_4,
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
