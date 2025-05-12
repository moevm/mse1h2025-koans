from .task import Task


class SomeTask(Task):

    name = 'some_task'
    description = 'some_task'
    path_template_toml = 'any'

    def _generate_condition_task(self, seed: int) -> str:
        return ''

    def _generate_code_template(self, seed: int) -> str:
        return ''

    def _generate_template_coderunner(self, seed: int) -> str:
        return ''
