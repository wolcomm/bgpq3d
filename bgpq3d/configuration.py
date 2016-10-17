import os
import ConfigParser


class Config(object):
    def __init__(self, config_path=None):
        config = ConfigParser.SafeConfigParser()
        if not config_path or not os.path.isfile(config_path):
            config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bgpq3d.ini')
        try:
            config.read(config_path)
            self._config = config
        except ConfigParser.Error:
            self._config = None

    def get(self, key=None):
        try:
            value = self._config.get("main", key)
        except:
            value = None
        return value
