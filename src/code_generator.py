import random
import re
from string import ascii_letters, ascii_lowercase


def generate_name():
    """
    Возвращаем случайное название переменной,
    состоящее из одной буквы в нижнем регистре.
    """
    return random.choice(ascii_lowercase)


def generate_char():
    """
    Возвращаем случайное значение переменной char.
    """
    return "'" + random.choice(ascii_letters) + "'"


def generate_int():
    return str(random.randint(-2147483648, 2147483647))


def generate_short():
    return str(random.randint(-32768, 32767))


def generate_long_long():
    return str(random.randint(-9223372036854775808, 9223372036854775807))


def generate_unsigned_int():
    return str(random.randint(0, 4294967295))


def generate_double():
    return str(round(random.uniform(-150, 150), 3))


def generate_param(seed):
    """
    функция возвращает словарь, который хранит информацию,
    какой $$шаблон$$ на что заменить
    """
    random.seed(seed)

    params = {
        "char": generate_name(),
        "char_ans": generate_char(),
        "short": generate_name(),
        "short_ans": generate_short(),
        "int": generate_name(),
        "int_ans": generate_int(),
        "ll": generate_name(),
        "ll_ans": generate_long_long(),
        "u_int": generate_name(),
        "u_int_ans": generate_unsigned_int(),
        "double_1": generate_name(),
        "double_1_ans": generate_double(),
        "double_2": generate_name(),
        "double_2_ans": generate_double(),
    }

    return params


def substitute_template(template: str, params) -> str:
    """
    Подставляет в шаблон template параметры param,
    сгенерированные функцией generate_param()
    """
    pattern = re.compile(r'\$\$(\w+)\$\$')

    def replacer(match):
        key = match.group(1)
        value = params.get(key, match.group(0))
        # Проверяем, можно ли привести значение к int,
        # и оборачиваем его в скобки, если оно меньше 0
        try:
            int_value = float(value)
            if int_value < 0:
                return f'({int_value})'
        except (ValueError, TypeError):
            pass

        return str(value)

    return pattern.sub(replacer, template)


def get_final_code(file_name, generate_func, seed=1337):
    """
    Получаем код из файла {file_name}.txt
    с подставленными значениями, сгенерированными функцией generate_func
    """
    with open(f"./tasks/{file_name}.txt", "r") as file:
        template = file.read()

    params = generate_func(seed)

    return substitute_template(template, params)


def main():
    print(get_final_code('basics', generate_param))


if __name__ == '__main__':
    main()
