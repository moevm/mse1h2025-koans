import random
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate
from tasks import SETTINGS_DIR
from tasks.toml_loader import TomlLoader


class StringsSizeofStrlen(Task):

    config_path = (
        SETTINGS_DIR / "settings_strings_task" / "strings_variables.toml"
    )
    config = TomlLoader(config_path).data
    name = 'strings_sizeof_strlen'
    description = '...'
    path_template_toml = 'strings_sizeof_strlen.toml'

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        string_5 = GeneratorTemplate.generate_string(
            self.config['strings_1']
        )
        len_string_5 = str(len(string_5))

        params = {
            # Test 5: sizeof_strlen
            "string_array_5_1": GeneratorTemplate.generate_array_string(
                self.config['strings_2']
            ),
            "string_ptr_5": GeneratorTemplate.generate_string(
                self.config['strings_1']
            ),
            "string_5": string_5,
            "len_string_5": len_string_5,
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
