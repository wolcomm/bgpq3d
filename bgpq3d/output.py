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


class DumpOutput(OutputBase):
    def output(self):
        print json.dumps(self.data)
        return None


class TestOutput(OutputBase):
    def output(self):
        return self.data
