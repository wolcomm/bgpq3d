import json
import subprocess
from whichcraft import which


class Bgpq3(object):
    def __init__(self, host=None, port=None, path=None):
        self._host = host or "whois.radb.net"
        self._port = port or 43
        self._path = path or which("bgpq3")

    @property
    def host(self):
        return "%s:%s" % (self._host, self._port)

    @property
    def path(self):
        return self._path

    def pl(self, obj=None):
        if not obj or not isinstance(obj, str):
            return None
        output = dict()
        cmds = {
            'ipv4': [self.path, "-h", self.host, "-l", "ipv4", "-4Aj", obj],
            'ipv6': [self.path, "-h", self.host, "-l", "ipv6", "-6Aj", obj]
        }
        for key in cmds:
            output.update(json.loads(subprocess.check_output(cmds[key])))
        return output


class Dummy(Bgpq3):
    def pl(self, obj=None):
        if not obj or not isinstance(obj, str):
            return None
        output = {
            'ipv4': [self.path, "-h", self.host, "-l", "ipv4", "-4Aj", obj],
            'ipv6': [self.path, "-h", self.host, "-l", "ipv6", "-6Aj", obj]
        }
        return output
