
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_029_test_input.vhd'))

lExpected_event = []
lExpected_event.append('')
utils.read_file(os.path.join(sTestDir, 'rule_029_test_input.fixed_event.vhd'), lExpected_event)

lExpected_edge = []
lExpected_edge.append('')
utils.read_file(os.path.join(sTestDir, 'rule_029_test_input.fixed_edge.vhd'), lExpected_edge)

class test_process_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_029_event(self):
        oRule = process.rule_029()
        oRule.clock = 'event'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '029')

        lExpected = [18, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_029_edge(self):
        oRule = process.rule_029()
        oRule.clock = 'edge'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '029')

     
        lExpected = [10, 14]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_029_event(self):
        oRule = process.rule_029()
        oRule.clock = 'event'

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_event, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_029_edge(self):
        oRule = process.rule_029()
        oRule.clock = 'edge'

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected_edge, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

