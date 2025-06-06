from tasks.interfaces import ABCTask
from tasks.utils import substitute_template, ValueGenerator, load_toml
from tasks import TEMPLATES_DIR, SETTINGS_DIR


TEMPLATE_PATH = (TEMPLATES_DIR / 'string'
                 / 'strings_reference_characters_template.toml')
CODERUNNER_BASE_TEMPLATE = (TEMPLATES_DIR / 'coderunner_template'
                            / 'base_tamplate.toml')
CONFIG_PATH = (SETTINGS_DIR / 'strings_settings'
               / 'strings_config.toml')


class StringsReferenceCharacters(ABCTask):

    name = 'strings_reference_characters_task'
    description = 'Виды доступа к символам строки'
    _template = load_toml(TEMPLATE_PATH)
    _coderunner_template = load_toml(CODERUNNER_BASE_TEMPLATE)
    _config = load_toml(CONFIG_PATH)

    def __generate_param(self) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        ValueGenerator.set_seed(self._seed)

        params = {
            # Test 2: reference_characters
            "string_2": ValueGenerator.generate_string_from_struct(
                self._config['strings_1']
            ),
            "index_2_1": ValueGenerator.generate_index_from_struct(
                self._config['strings_1']
            ),
            "index_2_2": ValueGenerator.generate_index_from_struct(
                self._config['strings_1']
            ),
            "index_2_3": ValueGenerator.generate_index_from_struct(
                self._config['strings_1']
            ),
            "index_2_4": ValueGenerator.generate_index_from_struct(
                self._config['strings_1']
            ),
        }

        return params

    def get_condition_task(self) -> str:
        description = self._template['template_condition']
        return description

    def get_code_template(self) -> str:
        template = self._template['template_code']
        params = self.__generate_param()
        return substitute_template(template, params)

    def get_template_coderunner(self) -> str:
        template = self._coderunner_template['template_coderunner']
        params = {'code': self.get_code_template()}
        params |= {'ban_words': str(self._template['ban_words'])}
        params |= {'error_messages': str(self._template['error_messages'][0])}
        return substitute_template(template, params)
