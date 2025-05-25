import random
from .task import Task
from tasks.utils import substitute_template, GeneratorTemplate
from tasks import SETTINGS_DIR
from tasks.toml_loader import TomlLoader


class StringsReferenceCharacters(Task):

    config_path = (
        SETTINGS_DIR / "settings_strings_task" / "strings_variables.toml"
    )
    config = TomlLoader(config_path).data
    name = 'strings_reference_characters'
    description = '...'
    path_template_toml = 'strings_reference_characters.toml'

    def __generate_param(self, seed):
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)

        params = {
            # Test 2: reference_characters
            "string_2": GeneratorTemplate.generate_string_from_struct(
                self.config['strings_1']
            ),
            "index_2_1": GeneratorTemplate.generate_index_from_struct(
                self.config['strings_1']
            ),
            "index_2_2": GeneratorTemplate.generate_index_from_struct(
                self.config['strings_1']
            ),
            "index_2_3": GeneratorTemplate.generate_index_from_struct(
                self.config['strings_1']
            ),
            "index_2_4": GeneratorTemplate.generate_index_from_struct(
                self.config['strings_1']
            ),
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
