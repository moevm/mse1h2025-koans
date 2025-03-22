import random
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
    функция возвращает что-то, что хранит информацию
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


def substitute_template(template: str) -> str:
    """
    Подставляет в шаблон template параметры param,
    сгенерированные функцией generate_param()
    """
    params = generate_param(1337)

    for key, value in params.items():
        template = template.replace(f'$${key}$$', value)

    return template


def main():
    with open("./tasks/basics.txt", "r") as file:
        template = file.read()

    substituted = substitute_template(template)
    print(substituted)


if __name__ == '__main__':
    main()
