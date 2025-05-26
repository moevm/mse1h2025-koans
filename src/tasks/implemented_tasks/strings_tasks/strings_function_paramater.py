from tasks.interfaces import ABCTask
from tasks.utils import substitute_template, ValueGenerator, load_toml
from tasks import TEMPLATES_DIR, SETTINGS_DIR


TEMPLATE_PATH = (TEMPLATES_DIR / 'string'
                 / 'strings_function_paramater_template.toml')
CODERUNNER_BASE_TEMPLATE = (TEMPLATES_DIR / 'coderunner_template'
                            / 'base_tamplate.toml')
CONFIG_PATH = (SETTINGS_DIR / 'strings_settings'
               / 'strings_config.toml')


class StringsFunctionParameter(ABCTask):

    name = 'strings_function_paramater_task'
    description = 'Строковые параметры'
    _template = load_toml(TEMPLATE_PATH)
    _coderunner_template = load_toml(CODERUNNER_BASE_TEMPLATE)
    _config = load_toml(CONFIG_PATH)

    def __generate_param(self) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        ValueGenerator.set_seed(self._seed)

        params = {
            # Test 7: function_paramater
            "func_param_string_7": ValueGenerator.generate_array_string_from_struct(
                self._config['strings_3']
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
