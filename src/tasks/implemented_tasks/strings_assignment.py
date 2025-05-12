import random
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate
from tasks import SETTINGS_DIR
from tasks.toml_loader import TomlLoader


class StringsAssignment(Task):

    config_path = (
        SETTINGS_DIR / "settings_strings_task" / "strings_variables.toml"
    )
    config = TomlLoader(config_path).data
    name = 'strings_assignment'
    description = '...'
    path_template_toml = 'strings_assignment.toml'

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        params = {
            # Test 3: assignment
            "string_3": GeneratorTemplate.generate_string(
                self.config['strings_1']
            ),
            "index_3_1": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_3_2": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_3_3": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "index_3_4": GeneratorTemplate.generate_index(
                self.config['strings_1']
            ),
            "char_3_1": GeneratorTemplate.generate_char(),
            "char_3_2": GeneratorTemplate.generate_char(),
            "char_3_3": GeneratorTemplate.generate_char(),
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
