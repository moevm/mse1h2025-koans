import subprocess
import random
from string import ascii_uppercase, ascii_lowercase, ascii_letters


def generate_int(min_value, max_value):
    return random.randint(min_value, max_value)


def generate_char(case='upper'):
    if case == 'upper':
        result = random.choice(ascii_uppercase)
    elif case == 'lower':
        result = random.choice(ascii_lowercase)
    else:
        result = random.choice(ascii_letters)
    # Символ строки должен быть в ковычках
    return "'" + result + "'"


# Словарь с информацией о заданиях
task_dict = {
    "about_something": {
        "char_variable": {
            "type": "char",
            "function": "generate_char",
            "parameters": {
                "case": "upper"
            },
            "tests": [
                {
                    "name": "cr_assert_eq",
                    "message": "Some message1"
                }
            ]
        },
        "int_variable": {
            "type": "int",
            "function": "generate_int",
            "parameters": {
                "min_value": 1,
                "max_value": 100
            },
            "tests": [
                {
                    "name": "cr_assert_eq",
                    "message": "Some message2"
                }
            ]
        },
    }
}


task_name = 'about_something'

# Генерируем значения для всех переменных
generated_values = [
    globals()[params['function']](**params['parameters'])
    for params in task_dict[task_name].values()
]


def student_code_parser(student_code):
    '''
    Будущий парсер кода студента,
    чтобы вставлять нужную часть в тесты.
    '''

    return f"""
    char char_variable = {generated_values[0]};
    int int_variable = {generated_values[1]};
    """


def get_test_code(task_name, student_code):
    '''
    Функция формирует код на Си для тестирования.
    '''
    current_task = task_dict[task_name]
    tests = []
    i = 0

    for var, params in current_task.items():
        # var_type = params['type']
        
        # Тут используем заранее сгенерированные значения
        generated_value = generated_values[i]
        i += 1
        var_tests = params['tests']

        for test in var_tests:
            test_string = \
                f'{test["name"]}({generated_value}, {var}, "{test["message"]}");'
            tests.append(test_string)

    # Формируем код из кода студента и тестов
    code = f"""
    #include <criterion/criterion.h>

    Test(about_control_statements, if_statements) {{
        {student_code_parser(student_code)}

        {'\n'.join(tests)}
    }}
    """

    return code


def compile_and_run(task_name, student_code):
    '''
    Функция компелирует Си файл с заданными define параметрами.
    '''

    c_code = get_test_code(task_name, student_code)
    c_file = f'./src/{task_name}.c'
    compiled_file = f'./bin/{task_name}'

    with open(c_file, "w") as f:
        f.write(c_code)

    subprocess.run([
        "gcc", c_file, "-o", compiled_file, "-lcriterion"
    ])

    subprocess.run([f"./bin/{task_name}"])


if __name__ == '__main__':

    student_code = f"""
    #include <stdio.h>

    def main() {{
        char char_variable = {generated_values[0]};
        int int_variable = {generated_values[1]};

        return 0;
    }}
    """

    print(generated_values)

    compile_and_run('about_something', student_code)
