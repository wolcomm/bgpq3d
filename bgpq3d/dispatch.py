import daemonize
from argparse import Namespace
from bgpq3d import configuration, bgpq3, output


class Dispatcher(object):
    def __init__(self, args=None, test=False):
        if not isinstance(args, Namespace):
            raise TypeError("%s not of type %s" % (args, Namespace))
        config_path = args.config_path or None
        self._config = configuration.Config(config_path=config_path)
        self._host = args.host or self.config.get("host")
        self._port = args.port or self.config.get("port")
        self._path = self.config.get("bgpq3_path")
        self._bgpq3 = bgpq3.Bgpq3(host=self.host, port=self.port, path=self.path)
        self._output_class = output.TestOutput if test else output.DumpOutput
        if args.object:
            self._object = args.object
            self.dispatch = self.one_shot

    def one_shot(self):
        data = self.bgpq3.pl(self.object)
        return self._output_class(data=data).output()

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

    @property
    def bgpq3(self):
        return self._bgpq3

    @property
    def object(self):
        return self._object or None
