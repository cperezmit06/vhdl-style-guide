
import os
import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_018_test_input.vhd'))


class test_entity_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_018_with_combined_generic(self):
        oRule = entity.rule_018()
        oRule.separate_generic_port_alignment = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '018')

        lExpected = [10, 11, 12, 19, 21, 24, 25, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_018_with_combined_generic(self):
        oRule = entity.rule_018()
        oRule.separate_generic_port_alignment = False

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_018_test_input.fixed_combined_generic.vhd'), lExpected)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_018_with_seperate_generic(self):
        oRule = entity.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '018')

        lExpected = [11, 12, 19, 21, 24, 25, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_018_with_seperate_generic(self):
        oRule = entity.rule_018()

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_018_test_input.fixed_seperate_generic.vhd'), lExpected)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

