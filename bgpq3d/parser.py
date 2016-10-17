import argparse


class Parser(object):
    def __init__(self, args=None):
        program_name = "bgpq3d"
        description = "A python daemon for prefix filter list management operations based on bgpq3"
        parser = argparse.ArgumentParser(prog=program_name, description=description)
        parser.add_argument('-f', action='store', dest='config_path', type=str, help="path to configuration file")
        parser.add_argument('--object', action='store', type=str, help="print prefix list for OBJECT")
        self._parser = parser
        self._args = args

    @property
    def args(self):
        if self._args:
            return self._parser.parse_args(self._args)
        else:
            return self._parser.parse_args()
