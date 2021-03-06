
import os
import unittest

from vsg.rules import for_loop
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_004_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_004_test_input.fixed.vhd'), lExpected)


class test_for_loop_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_004(self):
        oRule = for_loop.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '004')

        lExpected = [13, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_004(self):
        oRule = for_loop.rule_004()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
