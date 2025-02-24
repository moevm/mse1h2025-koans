import subprocess
import random
from string import ascii_uppercase, ascii_lowercase, ascii_letters


test_dict = {
    "about_something": {
        "C_VAL": {
            "function": "generate_char",
            "parameters": {
                "case": "upper"
            }
        },
        "INT_VAL": {
            "function": "generate_int",
            "parameters": {
                "min_value": 1,
                "max_value": 100
            }
        },
    }
}


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


def compile_with_parameters(test_name):
    '''
    Функция компелирует Си файл с заданными define параметрами.
    '''
    current_dict = test_dict[test_name]

    defines = [
        f"-D{variable[0]}={globals()[variable[1]['function']]
                           (**variable[1]['parameters'])}"
        for variable in current_dict.items()
    ]

    print(defines)

    compile_command = [
        "gcc", "-o",
        f"bin/{test_name}",
        f"src/{test_name}.c",
        "-lcriterion"
    ] + defines

    '''
    Пока не работает с мейкфайлом, потом сделаю нормально
    Сейчас исполняемый файл генерируется с gcc
    Из-за этого не получается подключить головной файл c_koans.h
    '''
    # compile_command = [
    #     "make",
    #     f"SRC_FILE_NAME={test_name}.c",
    #     f"DFLAGS={' '.join(defines)}"
    # ]

    subprocess.run(compile_command)


if __name__ == '__main__':

    test_name = 'about_something'

    # Компелируем код файла about_something.c
    compile_with_parameters(test_name)

    # Запускаем исполняемый файл
    subprocess.run([f"./bin/{test_name}"])
