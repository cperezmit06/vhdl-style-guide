
import os
import unittest

from vsg.rules import variable_assignment
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed.vhd'), lExpected)


class test_variable_assignment_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001(self):
        oRule = variable_assignment.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable_assignment')
        self.assertEqual(oRule.identifier, '001')

        lExpected = []
        lExpected.extend(range(31,35))
        lExpected.extend(range(36,40))
        lExpected.extend(range(41,45))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001(self):
        oRule = variable_assignment.rule_001()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
