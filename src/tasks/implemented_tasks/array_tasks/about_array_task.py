import random
from tasks.implemented_tasks.task import Task
from tasks.utils import substitute_template, GeneratorTemplate


class AboutAttayTask(Task):

    name = "about_array_task"
    description = "Знакомство с массивом"
    path_template_toml = "about_array_template.toml"

    def __generate_param(self, seed: int) -> dict[str, str]:
        """
        функция возвращает словарь (шаблон: подстановка)
        """
        random.seed(seed)
        size_random_array = GeneratorTemplate.generate_int_range(3, 15)
        params = {
            "short_ans": GeneratorTemplate.generate_short(),
            "offset_array": GeneratorTemplate.generate_int_range(1, 4),
            "size_random_array": size_random_array,
            "random_array": GeneratorTemplate.generate_array(
                size_random_array
            ),
            "random_element_array": GeneratorTemplate.generate_int_range(
                1, int(size_random_array) - 1
            ),
            "random_element_string": GeneratorTemplate.generate_int_range(
                0, 11
            ),
        }
        for i in range(5):
            params["int_ans_" + str(i)] = GeneratorTemplate.generate_int_range(-10, 30)

        return params

    def _generate_condition_task(self, seed: int) -> str:
        description = self._template["template_condition"]
        return description

    def _generate_code_template(self, seed: int) -> str:
        template = self._template["template_code"]
        params = self.__generate_param(seed)
        return substitute_template(template, params)

    def _generate_template_coderunner(self, seed: int) -> str:
        template = self._template["template_coderunner"]
        params = {"code": self._generate_code_template(seed)}
        return substitute_template(template, params)
