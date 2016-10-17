import daemonize
from argparse import Namespace
from bgpq3d import configuration, bgpq3


class Dispatcher(object):
    def __init__(self, args=None):
        if not isinstance(args, Namespace):
            raise TypeError("%s not of type %s" % (args, Namespace))
        config_path = args.config_path or None
        self._config = configuration.Config(config_path=config_path)
        self._host = args.host or self.config.get("host")
        self._port = args.port or self.config.get("port")
        self._path = self.config.get("bgpq3_path")
        self._bgpq3 = bgpq3.Bgpq3(host=self.host, port=self.port, path=self.path)
        if args.object:
            self.dispatch = self.one_shot

    def one_shot(self, obj):
        return self._bgpq3.pl(obj)

    @property
    def config(self):
        return self._config

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def path(self):
        return self._path
