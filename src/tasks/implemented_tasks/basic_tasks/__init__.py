from tasks import StoreTask
from .basic_task import BasicTask

group = 'Base'
tasks_classes = [
    BasicTask,
]

StoreTask.register_tasks(tasks_classes, group=group)

__all__ = [task_class.name for task_class in tasks_classes]
