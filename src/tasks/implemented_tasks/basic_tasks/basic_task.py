from tasks.interfaces import ABCTask
from tasks.utils import substitute_template, ValueGenerator, load_toml
from tasks import TEMPLATES_DIR


TEMPLATE_PATH = TEMPLATES_DIR / 'basic_template.toml'


class BasicTask(ABCTask):

    name = 'basic_task'
    description = 'Базовое задание на сравнение чисел'
    _template = load_toml(TEMPLATE_PATH)

    def __generate_param(self) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        ValueGenerator.set_seed(self._seed)

        params = {
            "char_ans": ValueGenerator.generate_char(),
            "short_ans": ValueGenerator.generate_short(),
            "int_ans": ValueGenerator.generate_int(),
            "ll_ans": ValueGenerator.generate_long_long(),
            "u_int_ans": ValueGenerator.generate_unsigned_int(),
            "double_1_ans": ValueGenerator.generate_double(),
            "double_2_ans": ValueGenerator.generate_double(),
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
        template = self._template['template_coderunner']
        params = {'code': self.get_code_template()}
        return substitute_template(template, params)
