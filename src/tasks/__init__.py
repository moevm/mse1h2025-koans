from pathlib import Path
from .store_task import StoreTask

ROOT_DIR = Path(__file__).parent.parent.parent.resolve()
TEMPLATES_DIR = ROOT_DIR / 'templates'
SETTINGS_DIR = ROOT_DIR / 'settings'

'''
Тут обязательно импортировать implemented_tasks после инициализации папок,
так как эти пути используются в task для создания кода
'''
from . import implemented_tasks


__all__ = [
    'StoreTask',
    'implemented_tasks'
]
