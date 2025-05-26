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
            formatter_class=argparse.RawTextHelpFormatter
        )
        self.__generate_arguments()
        self.args = self.parser.parse_args()
        self.store_task = StoreTask()

    def __generate_arguments(self) -> None:
        self.parser.add_argument(
            '--method',
            help=(
                'methods available: '
                'code_tmp - get_code_template, '
                'cond_task - get_condition_task, '
                'tmp_coderunner - get_template_coderunner'
            ),
            nargs='+',
            type=str,
        )
        self.parser.add_argument(
            '--name', help='name tasks', nargs='+', type=str
        )
        self.parser.add_argument(
            '--seed', help='seed generation number', type=int
        )
        self.parser.add_argument(
            '--no-color', help='disables color printing', action='store_true'
        )
        self.parser.add_argument(
            '--list-tasks', 
            help='list all available tasks', 
            action='store_true'
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
                color_print('Code, name', color=color, end='')
                print(f': {name}:\n{task.get_code_template()}')

            elif method == 'cond_task':
                color_print('Condition, name', color=color, end='')
                print(f': {name}:\n{task.get_condition_task()}')

            elif method == 'tmp_coderunner':
                color_print('Coderunner, name', color=color, end='')
                print(f': {name}:\n{task.get_template_coderunner()}')

            else:
                color_print(f'!!!Метода {method} не существует!!!',
                            color=('red' if not self.args.no_color else None))

    def run(self):
        if self.args.list_tasks:
            print(StoreTask.list_tasks())
            return

        for name in self.args.name:
            self.__print_generate_data(name, self.args.method)


if __name__ == '__main__':
    app = App()
    app.run()
