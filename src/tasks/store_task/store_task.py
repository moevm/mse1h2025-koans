from typing import Type, Iterable

from tasks.interfaces import ABCTask


class StoreTask:

    __tasks: dict[str, Type[ABCTask]] = {}
    __group: dict[str, str] = {}

    @classmethod
    def get_task(cls, task_name: str,
                 seed: int | None = None) -> ABCTask | None:
        task_class = cls.__tasks.get(task_name, None)
        if task_class:
            return task_class(seed)
        return None

    @classmethod
    def register_task(cls, task_class: Type[ABCTask],
                      group: str = 'unspecified'):
        if not getattr(task_class, 'name', None):
            raise AttributeError(
                f"Для регистрации класса '{task_class.__name__}'"
                " нужен атрибут 'name'."
            )

        if not getattr(task_class, 'description', None):
            raise AttributeError(
                f"Для регистрации класса '{task_class.__name__}'"
                " нужен атрибут 'description'."
            )

        name = task_class.name

        cls.__tasks[name] = task_class
        cls.__group[group] = name

    @classmethod
    def register_tasks(cls, tasks_classes: Iterable[Type[ABCTask]],
                       group: str = 'unspecified'):
        for task_class in tasks_classes:
            cls.register_task(task_class, group)

    @classmethod
    def __str__(cls) -> str:
        if not cls.__group:
            return "=== Хранилище задач ===\n(пусто)"

        sorted_groups = sorted(
            (group for group in cls.__group.keys() if group != 'unspecified'),
            key=lambda x: x.lower()
        )

        if 'unspecified' in cls.__group:
            sorted_groups.append('unspecified')

        result = ["=== Хранилище задач ==="]

        for group in sorted_groups:
            result.append(f"* Группа: {group}")

            group_tasks = [
                (name, cls.__tasks[name].description)
                for name, task_class in cls.__tasks.items()
                if cls.__group.get(task_class.name, ('', ''))[0] == name
                and cls.__group[task_class.name][0] == group
            ]

            for task_name, task_desc in sorted(group_tasks, key=lambda x: x[0]):
                result.append(f"  - {task_name}: {task_desc}")

        return "\n".join(result)
