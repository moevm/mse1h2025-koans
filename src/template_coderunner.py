import os
from code_generator import generate_param, substitute_template


def generate_template_coderunner(seed):
    base_path = os.path.dirname(__file__)
    task_path = os.path.join(base_path, 'tasks',
                             'basic_template_coderunner.txt')

    with open(task_path, "r") as file:
        template = file.read()

    params = generate_param(seed)
    return substitute_template(template, params)


if __name__ == '__main__':
    print(generate_template_coderunner(1337))
