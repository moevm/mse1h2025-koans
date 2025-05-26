from tasks import StoreTask
from .pointers_and_addresses_task import PointersAndAddressesTask
from .pointers_arrays_and_arithmetic_task import (
    PointersArraysAndArithmeticTask
)
from .pointers_as_function_arguments_task import (
    PointersAsFunctionArgumentsTask
)
from .pointers_function_task import PointersFunctionTask

group = 'Pointer'
tasks_classes = [
    PointersAndAddressesTask,
    PointersArraysAndArithmeticTask,
    PointersAsFunctionArgumentsTask,
    PointersFunctionTask,
]

StoreTask.register_tasks(tasks_classes, group=group)

__all__ = [task_class.name for task_class in tasks_classes]
