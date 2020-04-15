from main.cfg.util import KeyValueSetting


class _Config:
    FOO = 'foo'
    PUSHER_CHANNEL_NAMESPACE = ''
    BAR = KeyValueSetting('BAR', 'bar from base')


config = _Config()
