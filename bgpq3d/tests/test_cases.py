import os
from unittest import TestCase
from whichcraft import which
from bgpq3d import parser, bgpq3


class TestOutput(TestCase):
    def test_dependency(self):
        path = which('bgpq3')
        self.assertTrue(isinstance(path, str))

    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bgpq3d-test.ini')

    def test_autnum(self):
        cli = ['-f', self.config_path, '--object', 'AS37271']
        self.assertTrue(self._get_output(cli=cli), dict)

    def test_as_set(self):
        cli = ['-f', self.config_path, '--object', 'AS37271:AS-CUSTOMERS']
        self.assertTrue(self._get_output(cli=cli), dict)

    def _get_output(self, cli=None):
        args = parser.Parser(args=cli).args
        output = bgpq3.Bgpq3(args=args).pl()
        return output
