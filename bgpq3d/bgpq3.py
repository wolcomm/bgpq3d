import json
import subprocess
from whichcraft import which
from bgpq3d import configuration


class Bgpq3(object):
    def __init__(self, args=None):
        self._args = args
        if self._args:
            config_path = self._args.config_path
        else:
            config_path = None
        self._config = configuration.Config(config_path=config_path)

    @property
    def args(self):
        return self._args

    @property
    def config(self):
        return self._config

    @property
    def host(self):
        if self.config:
            return "%s:%s" % (self.config.get("host"), self.config.get("port"))
        else:
            return "whois.radb.net"

    @property
    def bin_path(self):
        return self.config.get("bin_path") or which("bgpq3")

    def pl(self, obj=None):
        if not obj:
            obj = self.args.object
        if not isinstance(obj, str):
            raise TypeError
        output = dict()
        cmds = {
            'ipv4': [self.bin_path, "-h", self.host, "-l", "ipv4", "-4Aj", obj],
            'ipv6': [self.bin_path, "-h", self.host, "-l", "ipv6", "-6Aj", obj]
        }
        for key in cmds:
            output.update(json.loads(subprocess.check_output(cmds[key])))
        return output
