
import unittest
from unittest import mock

from vsg import rule


class testRuleMethods(unittest.TestCase):

    def test_rule_exists(self):
        oRule = rule.rule()
        self.assertTrue(oRule)

    def test_rule_name(self):
        oRule = rule.rule()
        self.assertFalse(oRule.name)
        oRule.name = 'sName'
        self.assertEqual(oRule.name, 'sName')

    def test_rule_id(self):
        oRule = rule.rule()
        self.assertFalse(oRule.identifier)
        oRule.id = 'rule id 001'
        self.assertEqual(oRule.id, 'rule id 001')

    def test_rule_solution(self):
        oRule = rule.rule()
        self.assertFalse(oRule.solution)
        oRule.solution = 'rule solution'
        self.assertEqual(oRule.solution, 'rule solution')

    def test_add_violations_method(self):
        oRule = rule.rule()
        self.assertEqual(oRule.violations, [])
        oRule.add_violation(1)
        self.assertEqual(oRule.violations, [1])
        oRule.add_violation(10)
        oRule.add_violation(33)
        self.assertEqual(oRule.violations, [1,10,33])

    def test_rule_configure(self):
        oRule = rule.rule()
        oRule.name = 'xyz'
        oRule.identifier = '001'
        oRule.solution = 'This is my solution'
        self.assertEqual(oRule.name,'xyz')
        self.assertEqual(oRule.identifier,'001')
        self.assertEqual(oRule.solution,'This is my solution')
        self.assertEqual(oRule.disable,False)
        self.assertEqual(oRule.indentSize,2)

        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['xyz_001'] = {}
        dConfiguration['rule']['xyz_001']['disable'] = True

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.disable,True)


        dConfiguration['rule']['xyz_002'] = {}
        dConfiguration['rule']['xyz_002']['disable'] = False

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.disable,True)

        dConfiguration['rule']['xyz_001']['solution'] = 'This is the new solution'

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.solution,'This is the new solution')

        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['indentSize'] = 4

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.indentSize,4)

        # Check for attributes that do not exist
        dConfiguration['rule']['xyz_001']['invalidAttribute'] = False
        oRule.configure(dConfiguration)
        self.assertEqual(oRule.disable,True)
        self.assertEqual(oRule.solution,'This is the new solution')
        self.assertEqual(oRule.indentSize,4)

    def test_get_configuration(self):
        oRule = rule.rule()
        oRule.name = 'xyz'
        oRule.identifier = '010'
        oRule.phase = 3
        dExpected = {}
        dExpected['disable'] = False
        dExpected['fixable'] = True
        dExpected['indentSize'] = 2
        dExpected['phase'] = 3
        dExpected['severity'] = 'Error'
        dActual = oRule.get_configuration()
        for sKey in dExpected.keys():
            self.assertEqual(dActual[sKey], dExpected[sKey])
        for sKey in dActual.keys():
            self.assertEqual(dActual[sKey], dExpected[sKey])

    def test_get_solution(self):
        oRule = rule.rule()
        self.assertEqual(oRule._get_solution(100), None)
        oRule.solution = 'Solution'
        self.assertEqual(oRule._get_solution(100), 'Solution')

    def test_configure_rule_attributes_method(self):
        oRule = rule.rule()
        oRule.name = 'xyz'
        oRule.identifier = '001'
        dConfiguration = {}

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.indentSize, 2)
        self.assertEqual(oRule.phase, None)
        self.assertEqual(oRule.disable, False)
        self.assertEqual(oRule.fixable, True)
        self.assertEqual(oRule.configuration, ['indentSize', 'phase', 'disable', 'fixable', 'severity'])

        dConfiguration['rule'] = {}
        dConfiguration['rule']['xyz_001'] = {}
        dConfiguration['rule']['xyz_001']['indentSize'] = 4
        dConfiguration['rule']['xyz_001']['phase'] = 10
        dConfiguration['rule']['xyz_001']['disable'] = True
        dConfiguration['rule']['xyz_001']['fixable'] = False
        dConfiguration['rule']['xyz_001']['unknown'] = 'New'

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.indentSize, 4)
        self.assertEqual(oRule.phase, 10)
        self.assertEqual(oRule.disable, True)
        self.assertEqual(oRule.fixable, False)
        self.assertEqual(oRule.configuration, ['indentSize', 'phase', 'disable', 'fixable', 'severity'])

        oRule.configuration.append('unknown')
        oRule.unknown = None
        oRule.configure(dConfiguration)

        self.assertEqual(oRule.indentSize, 4)
        self.assertEqual(oRule.phase, 10)
        self.assertEqual(oRule.disable, True)
        self.assertEqual(oRule.fixable, False)
        self.assertEqual(oRule.unknown, 'New')
        self.assertEqual(oRule.configuration, ['indentSize', 'phase', 'disable', 'fixable', 'severity', 'unknown'])

    def test_get_violations_w_vsg_output_method(self):
        oRule = rule.rule()
        oRule.name = 'xyz'
        oRule.identifier = '001'
        oRule.solution = 'Solution'
        dViolation = {}
        dViolation['lineNumber'] = 1
        oRule.add_violation(dViolation)
        dViolation = {}
        dViolation['lineNumber'] = 2
        oRule.add_violation(dViolation)
        dViolation = {}
        dViolation['lines']= []
        dLineViolation = {}
        dLineViolation['number'] = 2
        dViolation['lines'].append(dLineViolation)
        dLineViolation = {}
        dLineViolation['number'] = 3
        dViolation['lines'].append(dLineViolation)
        oRule.add_violation(dViolation)

        lExpected = []
        dExpected = {}
        dExpected['rule'] = 'xyz_001'
        dExpected['lineNumber'] = '1'
        dExpected['solution'] = 'Solution'
        dExpected['severity'] = {}
        dExpected['severity']['name'] = 'Error'
        dExpected['severity']['type'] = 'error'
        lExpected.append(dExpected)

        lActual = oRule.get_violations_at_linenumber(1)
        self.assertEqual(lActual, lExpected)

        lExpected = []
        dExpected = {}
        dExpected['rule'] = 'xyz_001'
        dExpected['lineNumber'] = '2'
        dExpected['solution'] = 'Solution'
        dExpected['severity'] = {}
        dExpected['severity']['name'] = 'Error'
        dExpected['severity']['type'] = 'error'
        lExpected.append(dExpected)
        dExpected = {}
        dExpected['rule'] = 'xyz_001'
        dExpected['lineNumber'] = '2'
        dExpected['solution'] = 'Solution'
        dExpected['severity'] = {}
        dExpected['severity']['name'] = 'Error'
        dExpected['severity']['type'] = 'error'
        lExpected.append(dExpected)

        lActual = oRule.get_violations_at_linenumber(2)
        self.assertEqual(lActual, lExpected)

    def test_has_violations_method(self):
        oRule = rule.rule()

        self.assertFalse(oRule.has_violations())

        oRule.add_violation(1)
        self.assertTrue(oRule.has_violations())
