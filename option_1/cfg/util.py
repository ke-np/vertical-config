from importlib import import_module
import os


def get_vertical_config_module(vertical):
    env = os.getenv('ENVIRONMENT', 'local')
    config_name = f'main.cfg.{env}.{vertical}'
    try:
        module = import_module(config_name)
    except ImportError:
        return None
    return module


class KeyValueSetting:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __call__(self, vertical=None):
        if vertical is None:
            return self.val
        module = get_vertical_config_module(vertical)
        if module is None:
            return self.val
        return getattr(module.config, self.key, self.val)
