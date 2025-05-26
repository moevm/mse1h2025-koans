from tasks import StoreTask
from .function_basics_task import FunctionBasicsTask
from .function_prototypes_task import FunctionPrototypesTask
from .function_scope_and_vars_task import FunctionScopeAndVarsTask

group = 'Function'
tasks_classes = [
    FunctionBasicsTask,
    FunctionPrototypesTask,
    FunctionScopeAndVarsTask,
]

StoreTask.register_tasks(tasks_classes, group=group)

__all__ = [task_class.name for task_class in tasks_classes]
