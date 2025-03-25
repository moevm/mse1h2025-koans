from tasks import StoreTask
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
            nargs="+",
            type=str,
        )
        self.parser.add_argument(
            "--name", help="name tasks", nargs="+", type=str
        )
        self.parser.add_argument(
            "--seed", help="seed generation number", type=int
        )

    def __print_generate_data(self, name, method):
        task = self.store_task.get_task(name, self.args.seed)
        match method:
            case "code_tmp":
                print((
                    f"Coderunner, name: {name}:\n"
                    f"{task.get_code_template()}"
                ))
            case "cond_task":
                print((
                    f"Condition, name: {name}:\n"
                    f"{task.get_condition_task()}"
                ))
            case "tmp_coderunner":
                print((
                    f"Code, name: {name}:\n"
                    f"{task.get_template_coderunner()}"
                ))
            case _:
                print("Такого метода не существует!")

    def run(self):
        for method in self.args.method:
            for name in self.args.name:
                self.__print_generate_data(name, method)      


if __name__ == "__main__":
    app = App()
    app.run()
