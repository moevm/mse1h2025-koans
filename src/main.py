from tasks.store_task import StoreTask
import argparse


def color_print(data, color=None, **kwargs):
    color_code = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    code = color_code.get(color, '')
    print(f'{code}{data}{color_code["reset"] if color else ""}', **kwargs)


class App:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            add_help=False
        )
        self.__generate_arguments()
        self.args = self.parser.parse_args()
        self.store_task = StoreTask()

    def __generate_arguments(self) -> None:
        self.parser.add_argument(
            '-h', '--help',
            action='store_true',
            help='Показать help-сообщение с описанием доступных команд и параметров.'
        )
        self.parser.add_argument(
            '--method',
            help=(
                'доступные методы: '
                'code_tmp - получить шаблон кода, '
                'cond_task - получить условие задачи, '
                'tmp_coderunner - получить шаблон для coderunner'
            ),
            nargs='+',
            type=str,
        )
        self.parser.add_argument(
            '--name', help='название задачи(задач)', nargs='+', type=str
        )
        self.parser.add_argument(
            '--list-tasks',
            help='показать список всех доступных задач',
            action='store_true'
        )
        self.parser.add_argument(
            '--seed', help='число для генерации (seed)', type=int
        )
        self.parser.add_argument(
            '--no-color', help='отключает цветной вывод', action='store_true'
        )

    def __print_generate_data(self, name, methods):
        task = self.store_task.get_task(name, self.args.seed)

        if task is None:
            color = 'red' if not self.args.no_color else None
            color_print(f'!!!Задачи {name} не существует!!!', color=color)
            return

        color = 'cyan' if not self.args.no_color else None

        for method in methods:
            if method == 'code_tmp':
                code_temp = task.get_code_template()
                color_print('Код', color=color, end='')
                print(f': {name}:\n{code_temp}')

            elif method == 'cond_task':
                cond_task = task.get_condition_task()
                color_print('Условие', color=color, end='')
                print(f': {name}:\n{cond_task}')

            elif method == 'tmp_coderunner':
                temp_coderunner = task.get_template_coderunner()
                color_print('Coderunner', color=color, end='')
                print(f': {name}:\n{temp_coderunner}')

            else:
                color_print(f'!!!Метода {method} не существует!!!',
                            color=('red' if not self.args.no_color else None))

    def run(self):
        if self.args.help:
            self.parser.print_help()
            return

        if self.args.list_tasks:
            print(StoreTask.list_tasks())
            return

        for name in self.args.name:
            self.__print_generate_data(name, self.args.method)


if __name__ == '__main__':
    app = App()
    app.run()
