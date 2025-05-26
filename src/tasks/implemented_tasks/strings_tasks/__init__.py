from tasks import StoreTask
from .strings_assignment import StringsAssignment
from .strings_copy import StringsCopy
from .strings_declaration import StringsDeclaration
from .strings_formating import StringsFormating
from .strings_function_paramater import StringsFunctionParameter
from .strings_reference_characters import StringsReferenceCharacters
from .strings_sizeof_strlen import StringsSizeofStrlen
from .strings_what_is_string import StringsWhatIsString


group = 'String'
tasks_classes = [
    StringsAssignment,
    StringsCopy,
    StringsDeclaration,
    StringsFormating,
    StringsFunctionParameter,
    StringsReferenceCharacters,
    StringsSizeofStrlen,
    StringsWhatIsString,
]

StoreTask.register_tasks(tasks_classes, group=group)

__all__ = [task_class.name for task_class in tasks_classes]
