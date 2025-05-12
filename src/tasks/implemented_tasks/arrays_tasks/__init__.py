from tasks import StoreTask
from .about_array_task import AboutArrayTask

group = 'Array'
StoreTask.register_task(AboutArrayTask, group=group)

__all__ = [
    'AboutArrayTask',
]
