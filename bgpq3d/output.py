import json


class OutputBase(object):
    def __init__(self, data=None):
        if not isinstance(data, dict):
            raise TypeError("%s is not of type %s" % (data, dict))
        self._data = data

    @property
    def data(self):
        return self._data

    def output(self):
        return None


class TestOutput(OutputBase):
    def output(self):
        return self.data


class JsonOutput(OutputBase):
    def output(self):
        return json.dumps(self.data, indent=4)


class IosOutput(OutputBase):
    def output(self):
        data = self.data
        for af in data:
            i = 0
            for p in data[af]:
                i += 10
                print self.line(af=af, entry=p, i=i)
        return None

    def line(self, name='Prefix-List', af=None, entry=None, i=None):
        if not isinstance(entry, dict):
            raise ValueError("%s not of type %s" % (entry, dict))
        if not isinstance(i, int):
            raise ValueError("%s not of type %s" % (i, int))
        return "%s %s seq %s permit %s" % (self.af(af=af), name, i, entry['prefix'])

    def af(self, af=None):
        if af == 'ipv4':
            return 'ip prefix-list'
        elif af == 'ipv6':
            return 'ipv6 prefix-list'
        else:
            raise ValueError("%s is not a valid address-family name" % af)
