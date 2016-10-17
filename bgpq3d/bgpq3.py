import json
import subprocess
import re
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

    def version(self):
        regexp = re.compile(r'^bgpq3 version: (\w+)$')
        for line in subprocess.check_output(self.bin_path).splitlines():
            m = regexp.match(line)
            if m:
                return m.groups(1)
        return None

    def pl(self, obj=None):
        if not obj:
            obj = self.args.object
        if not isinstance(obj, str):
            raise TypeError
        cmd = [
            self.bin_path,
            "-h", self.host,
            "-4Aj",
            obj
        ]
        out = subprocess.check_output(cmd)
        return json.loads(out)
