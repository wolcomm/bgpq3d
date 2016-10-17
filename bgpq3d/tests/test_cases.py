import os
from unittest import TestCase
from whichcraft import which
from bgpq3d import parser, dispatch


class TestOutput(TestCase):
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bgpq3d-test.ini')

    def test_01_dependency(self):
        path = which('bgpq3')
        self.assertIsInstance(path, str, msg="bgpq3 executable not found in PATH")

    def test_02_autnum(self):
        cli = ['-f', self.config_path, '--object', 'AS37271']
        self.assertIsInstance(self._get_output(cli=cli), dict, msg="didn't get a dict object")

    def test_03_as_set(self):
        cli = ['-f', self.config_path, '--object', 'AS37271:AS-CUSTOMERS']
        self.assertIsInstance(self._get_output(cli=cli), dict, msg="didn't get a dict object")

    def _get_output(self, cli=None):
        args = parser.Parser(args=cli).args
        dispatcher = dispatch.Dispatcher(args=args, test=True)
        output = dispatcher.dispatch()
        return output
