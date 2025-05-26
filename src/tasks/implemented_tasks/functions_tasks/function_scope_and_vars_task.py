from tasks.interfaces import ABCTask
from tasks.utils import substitute_template, ValueGenerator, load_toml
from tasks import TEMPLATES_DIR


TEMPLATE_PATH = (TEMPLATES_DIR / 'function'
                 / 'function_scope_and_vars_template.toml')
CODERUNNER_BASE_TEMPLATE = (TEMPLATES_DIR / 'coderunner_template'
                            / 'base_tamplate.toml')


class FunctionScopeAndVarsTask(ABCTask):

    name = 'function_scope_and_vars_task'
    description = 'Знакомство с областью видимости переменных'
    _template = load_toml(TEMPLATE_PATH)
    _coderunner_template = load_toml(CODERUNNER_BASE_TEMPLATE)

    def __generate_param(self) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        ValueGenerator.set_seed(self._seed)

        params = {
            "static_plus_func": ValueGenerator.generate_int_range(-3, 5),
            "static_val_func": ValueGenerator.generate_int_range(-3, 10),
            "global_val": ValueGenerator.generate_int_range(-3, 10),
            "global_plus": ValueGenerator.generate_int_range(-3, 5),
            "static_val": ValueGenerator.generate_int_range(-3, 10),
            "static_plus": ValueGenerator.generate_int_range(-3, 5),
            "local_val": ValueGenerator.generate_int_range(-3, 10),
            "local_plus": ValueGenerator.generate_int_range(-3, 5),
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
