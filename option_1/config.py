import os.path
from importlib import import_module

basedir = os.path.abspath(os.path.dirname(__file__))
env = os.getenv('ENVIRONMENT', 'local')
if not env in ['local', 'test']:
    config_file = 'main/cfg/' + env + '.py'
    if not os.path.isfile(config_file):
        env = 'local'

config_name = 'main.cfg.' + env + '.shared'

module = import_module(config_name)

config = module.config
config.MIGRATIONS_PATH = os.path.join(basedir, 'migrations')
if config.PUSHER_CHANNEL_NAMESPACE == '':
    config.PUSHER_CHANNEL_NAMESPACE = os.getenv('PUSHER_CHANNEL_NAMESPACE', '')