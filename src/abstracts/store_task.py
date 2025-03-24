class StoreTask:

    __tasks = {}

    @classmethod
    def get_task(cls, task_name: str, seed: int | None = None):
        task_class = cls.__tasks.get(task_name, None)
        if task_class:
            return task_class(seed)
        return None

    @classmethod
    def register_task(cls, task_class):
        cls.__tasks[task_class.name] = task_class

    @classmethod
    def get_register_task(cls):
        return cls.__tasks.copy()