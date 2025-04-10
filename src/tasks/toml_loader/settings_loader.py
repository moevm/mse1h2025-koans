from tasks import SETTINGS_DIR
from .toml_loader import TomlLoader


SETTINGS_PATH = SETTINGS_DIR / 'settings_const.toml'


class SettingsLoader(TomlLoader):

    def __init__(self):
        super().__init__(SETTINGS_PATH)
