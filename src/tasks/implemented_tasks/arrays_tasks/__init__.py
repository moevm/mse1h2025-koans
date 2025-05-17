from tasks import StoreTask
from .about_array_task import AboutArrayTask

group = 'Array'
tasks_classes = [
    AboutArrayTask,
]

StoreTask.register_tasks(tasks_classes, group=group)

__all__ = [task_class.name for task_class in tasks_classes]
