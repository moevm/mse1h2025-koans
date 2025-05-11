import random
import tomllib
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate
from tasks import SETTINGS_DIR


class StringsCopy(Task):

    config_path = (
        SETTINGS_DIR / "settings_strings_task" / "strings_variables.toml"
    )
    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    name = 'strings_copy'
    description = '...'
    path_template_toml = 'strings_copy.toml'

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        string_6 = GeneratorTemplate.generate_string(
            self.config['strings_1']
        )
        len_stirng_6 = str(len(string_6))

        params = {
            # Test 6: copy
            "string_6": string_6,
            "len_string_6": len_stirng_6,
            "index_6": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "char_6": GeneratorTemplate.generate_char(),
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
