import re
import random
from string import ascii_letters
from tasks.toml_loader import SettingsLoader


def substitute_template(template: str, params: dict[str, str]) -> str:
    """
    Подставляет в шаблон template параметры param,
    сгенерированные функцией generate_param()
    """
    pattern = re.compile(r'\$\$(\w+)\$\$')

    def replacer(match):
        key = match.group(1)
        return params.get(key, match.group(0))

    return pattern.sub(replacer, template)


class GeneratorTemplate:

    settings = SettingsLoader()

    @classmethod
    def generate_name(cls, name_list):
        """
        |Возвращает случайную строку из переданного
        списка имён.
        """
        return random.choice(name_list)

    @classmethod
    def generate_char(cls):
        """
        Возвращаем случайное значение переменной char.
        """
        return "'" + random.choice(ascii_letters) + "'"

    @classmethod
    def generate_int(cls):
        return str(random.randint(
            cls.settings.data['range_int']['min'],
            cls.settings.data['range_int']['max']
        ))

    @classmethod
    def generate_short(cls):
        return str(random.randint(
            cls.settings.data['range_short']['min'],
            cls.settings.data['range_short']['max']
        ))

    @classmethod
    def generate_long_long(cls):
        return str(random.randint(
            cls.settings.data['range_long_long']['min'],
            cls.settings.data['range_long_long']['max']
        ))

    @classmethod
    def generate_unsigned_int(cls):
        return str(random.randint(
            cls.settings.data['range_unsigned_int']['min'],
            cls.settings.data['range_unsigned_int']['max']
        ))

    @classmethod
    def generate_double(cls):
        num = round(
            random.uniform(
                cls.settings.data['range_double']['min'],
                cls.settings.data['range_double']['max']
            ), 3
        )
        str_num = str(num)
        if num < 0:
            str_num = '(' + str_num + ')'
        return str_num

    @classmethod
    def generate_int_range(cls, number_min, number_max):
        return str(random.randint(number_min, number_max))

    @classmethod
    def generate_array(cls, array_size):
        return (
            "{"
            + ", ".join(
                [cls.generate_int_range(0, 100) for _ in range(int(array_size))]
            )
            + "}"
        )