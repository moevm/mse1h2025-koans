import random
import tomllib
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate
from tasks import SETTINGS_DIR


class StringsFormating(Task):

    config_path = (
        SETTINGS_DIR / "settings_strings_task" / "strings_variables.toml"
    )
    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    name = 'strings_formating'
    description = '...'
    path_template_toml = 'strings_formating.toml'

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
