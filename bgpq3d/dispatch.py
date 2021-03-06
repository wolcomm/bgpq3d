from argparse import Namespace
from bgpq3d import configuration, bgpq3, output

try:
    import daemonize
    can_daemonize = True
except ImportError:
    can_daemonize = False

class Dispatcher(object):
    def __init__(self, args=None, test=False, config_path=None,
                 host=None, port=None, bgpq3_path=None, output_class=None, object=None):
        if args and not isinstance(args, Namespace):
            raise TypeError("%s not of type %s" % (args, Namespace))
        config_path = config_path or args.config_path or None
        self._config = configuration.Config(config_path=config_path)
        self._host = host or args.host or self.config.get("host")
        self._port = port or args.port or self.config.get("port")
        self._path = bgpq3_path or self.config.get("bgpq3_path")
        if not args.dummy:
            self._bgpq3 = bgpq3.Bgpq3(host=self.host, port=self.port, path=self.path)
        else:
            self._bgpq3 = bgpq3.Dummy(host=self.host, port=self.port, path=self.path)
        self._output_class_name = args.output or self.config.get("output_class_name") or "JsonOutput"
        self._output_class = output.TestOutput if test else getattr(output, self.output_class_name)
        self._object = args.object

    def dispatch(self):
        data = self.bgpq3.pl(self.object)
        return self._output_class(data=data).output()

    @property
    def object(self):
        return self._object or None

    @object.setter
    def object(self, name=None):
        self._object = name

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
    def output_class_name(self):
        return self._output_class_name
