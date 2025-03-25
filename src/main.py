from abstracts.store_task import StoreTask
from some_task import SomeTask
import argparse


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
            "--method",
            help=(
                "methods available: "
                "code_tmp - get_code_template, "
                "cond_task - get_condition_task, "
                "tmp_coderunner - get_template_coderunner"
            ),
            type=str,
        )
        self.parser.add_argument("--name", help="name tasks", type=str)
        self.parser.add_argument(
            "--seed", help="seed generation number", type=int
        )

    def run(self):
        task = self.store_task.get_task(self.args.name, self.args.seed)
        match self.args.method:
            case "code_tmp":
                print(task.get_code_template())
            case "cond_task":
                print(task.get_condition_task())
            case "tmp_coderunner":
                print(task.get_template_coderunner())
            case _:
                print("Такого метода не существует!")


if __name__ == "__main__":
    app = App()
    app.run()