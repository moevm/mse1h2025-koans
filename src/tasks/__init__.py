from pathlib import Path
from .store_task import StoreTask

ROOT_DIR = Path(__file__).parent.parent.parent.resolve()
TEMPLATES_DIR = ROOT_DIR / 'templates'
SETTINGS_DIR = ROOT_DIR / 'settings'

from .implemented_tasks import *

__all__ = [
    'StoreTask'
]
