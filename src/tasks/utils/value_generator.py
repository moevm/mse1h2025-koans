import random
from string import ascii_letters

from tasks import SETTINGS_DIR
from .load_toml import load_toml


GENERATOR_SETTINGS_PATH = SETTINGS_DIR / 'settings_const.toml'


class ValueGenerator:

    settings = load_toml(GENERATOR_SETTINGS_PATH)

    @classmethod
    def set_seed(cls, seed: int):
        random.seed(seed)

    @classmethod
    def generate_name(cls, name_list):
        return random.choice(name_list)

    @classmethod
    def generate_char(cls):
        return "'" + random.choice(ascii_letters) + "'"

    @classmethod
    def generate_int(cls):
        return str(random.randint(
            cls.settings['range_int']['min'],
            cls.settings['range_int']['max']
        ))

    @classmethod
    def generate_short(cls):
        return str(random.randint(
            cls.settings['range_short']['min'],
            cls.settings['range_short']['max']
        ))

    @classmethod
    def generate_long_long(cls):
        return str(random.randint(
            cls.settings['range_long_long']['min'],
            cls.settings['range_long_long']['max']
        ))

    @classmethod
    def generate_unsigned_int(cls):
        return str(random.randint(
            cls.settings['range_unsigned_int']['min'],
            cls.settings['range_unsigned_int']['max']
        ))

    @classmethod
    def generate_double(cls):
        num = round(
            random.uniform(
                cls.settings['range_double']['min'],
                cls.settings['range_double']['max']
            ), 3
        )
        str_num = str(num)
        if num < 0:
            str_num = '(' + str_num + ')'
        return str_num

    @classmethod
    def generate_string_from_struct(cls, strings_struct):
        string = random.choice(strings_struct['strings'])
        return f'"{string}"'

    @classmethod
    def generate_index_from_struct(cls, strings_struct):
        index = str(random.randint(0, strings_struct['max_index']))
        return index

    @classmethod
    def generate_array_string_from_struct(cls, strings_struct):
        string = random.choice(strings_struct['strings'])
        array_string = list(map(lambda x: "'" + x + "'", string))
        return f"{{ {', '.join(array_string)} }}"

    @classmethod
    def generate_string_and_array_from_struct(cls, strings_struct):
        string = random.choice(strings_struct['strings'])
        array_string = list(map(lambda x: "'" + x + "'", string))
        return f'"{string}"', f"{{ {', '.join(array_string)} }}"

    @classmethod
    def generate_int_range(cls, number_min, number_max):
        return str(random.randint(number_min, number_max))

    @classmethod
    def generate_array(cls, array_size):
        return (
            "{"
            + ", ".join(
                [cls.generate_int_range(0, 100)
                 for _ in range(int(array_size))]
            )
            + "}"
        )

    @classmethod
    def generate_string(cls, string_size):
        body = "".join(
            random.choice(ascii_letters) for _ in range(int(string_size))
        )
        return '"' + body + '"'
