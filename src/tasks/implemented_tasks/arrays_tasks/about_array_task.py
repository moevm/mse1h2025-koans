from tasks.interfaces import ABCTask
from tasks.utils import substitute_template, ValueGenerator, load_toml
from tasks import TEMPLATES_DIR


TEMPLATE_PATH = TEMPLATES_DIR / 'about_array_template.toml'


class AboutArrayTask(ABCTask):

    name = 'about_array_task'
    description = 'Знакомство с массивом'
    _template = load_toml(TEMPLATE_PATH)

    def __generate_param(self) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        ValueGenerator.set_seed(self._seed)
        size_random_array = ValueGenerator.generate_int_range(3, 15)
        size_random_string = ValueGenerator.generate_int_range(5, 15)
        params = {
            'short_ans': ValueGenerator.generate_short(),
            'offset_array': ValueGenerator.generate_int_range(1, 4),
            'size_random_array': size_random_array,
            'random_array': ValueGenerator.generate_array(
                size_random_array
            ),
            'random_element_array': ValueGenerator.generate_int_range(
                1, int(size_random_array) - 1
            ),
            'random_element_string': ValueGenerator.generate_int_range(
                0, int(size_random_string) - 1
            ),
            'random_string': ValueGenerator.generate_string(size_random_string),
        }
        for i in range(5):
            params[f'int_ans_{i}'] = ValueGenerator.generate_int_range(-10, 30)

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
