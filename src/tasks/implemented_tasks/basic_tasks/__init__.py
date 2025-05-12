from tasks import StoreTask
from .basic_task import BasicTask

group = 'Base'
StoreTask.register_task(BasicTask, group=group)

__all__ = [
    'BasicTask',
]
