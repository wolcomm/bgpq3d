import os
import json
from unittest import TestCase
from whichcraft import which
from bgpq3d import parser, bgpq3


class TestOutput(TestCase):
    def test_dependency(self):
        path = which('bgpq3')
        self.assertTrue(isinstance(path, str))

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bgpq3d-test.ini')

    def test_autnum(self):
        cli = ['-f', self.path, '--object', 'AS37271']
        args = parser.Parser(args=cli).args
        output = bgpq3.Bgpq3(args=args).pl()
        self.assertTrue(isinstance(json.loads(output), dict))

