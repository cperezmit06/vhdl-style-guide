
import os
import unittest

from vsg.rules import whitespace
from vsg import vhdlFile
from vsg import line
from vsg.tests import utils

sFileName = os.path.join(os.path.dirname(__file__),'..','whitespace','whitespace_test_input.txt')

class testRuleWhitespaceMethods(unittest.TestCase):

    def setUp(self):
        self.lFile = utils.read_vhdlfile(sFileName)
        self.oFile = vhdlFile.vhdlFile(self.lFile)

    def test_005(self):
        oRule = whitespace.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '005')
        self.assertEqual(oRule.phase, 2)

        dExpected = utils.add_violation_list([1,3,5])
        self.oFile.lines.append(line.line('  This is a test of parenthesis ( failure'))
        self.oFile.lines.append(line.line('  This is a test of parenthesis (pass'))
        self.oFile.lines.append(line.line('  This is a test of parentehsis (  failure'))
        self.oFile.lines.append(line.line('  This is a test of parentehsis (  7 pass'))
        self.oFile.lines.append(line.line('  This is a test of parenthesis ( pass) --  ( pass'))
        self.oFile.lines.append(line.line(' --  This is a test of parenthesis ( pass)'))
        self.oFile.lines[5].hasComment = True
        self.oFile.lines[6].isComment = True
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[1].line, '  This is a test of parenthesis (failure')
        self.assertEqual(self.oFile.lines[2].line, '  This is a test of parenthesis (pass')
        self.assertEqual(self.oFile.lines[3].line, '  This is a test of parentehsis (failure')
        self.assertEqual(self.oFile.lines[4].line, '  This is a test of parentehsis (  7 pass')
        self.assertEqual(self.oFile.lines[5].line, '  This is a test of parenthesis (pass) --  ( pass')
        self.assertEqual(self.oFile.lines[6].line, ' --  This is a test of parenthesis ( pass)')



    def test_011(self):
        oRule = whitespace.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '011')
        self.assertEqual(oRule.phase, 2)

        dExpected = utils.add_violation_list([1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,23,24,26])
        self.oFile.lines.append(line.line('  a <= b+ c'))   #1
        self.oFile.lines.append(line.line('  a <= b +c'))   #2
        self.oFile.lines.append(line.line('  a <= b + c'))  #3
        self.oFile.lines.append(line.line('  a <= b+c'))    #4
        self.oFile.lines.append(line.line('  a <= b- c'))   #5
        self.oFile.lines.append(line.line('  a <= b -c'))   #6
        self.oFile.lines.append(line.line('  a <= b - c'))  #7
        self.oFile.lines.append(line.line('  a <= b-c'))    #8
        self.oFile.lines.append(line.line('  a <= b/ c'))   #9
        self.oFile.lines.append(line.line('  a <= b /c'))   #10
        self.oFile.lines.append(line.line('  a <= b / c'))  #11
        self.oFile.lines.append(line.line('  a <= b/c'))    #12
        self.oFile.lines.append(line.line('  a <= b* c'))   #13
        self.oFile.lines.append(line.line('  a <= b *c'))   #14
        self.oFile.lines.append(line.line('  a <= b * c'))  #15
        self.oFile.lines.append(line.line('  a <= b*c'))    #16
        self.oFile.lines.append(line.line('  a <= b** c'))   #17
        self.oFile.lines.append(line.line('  a <= b **c'))   #18
        self.oFile.lines.append(line.line('  a <= b ** c'))  #19
        self.oFile.lines.append(line.line('  a <= b**c'))    #20
        self.oFile.lines.append(line.line('  a <= b**c -- This**is fine'))    #21
        self.oFile.lines.append(line.line('  a <= b ** c -- This**is fine'))    #22
        self.oFile.lines.append(line.line('  a <= )+ ('))   #23
        self.oFile.lines.append(line.line('  a <= ) +('))   #24
        self.oFile.lines.append(line.line('  a <= ) + ('))  #25
        self.oFile.lines.append(line.line('  a <= )+('))    #26
        self.oFile.lines.append(line.line('  G_FILE => "$DIR/somedir/somefile.txt",')) #27
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_011_with_negative_numbers(self):
        oRule = whitespace.rule_011()

        dExpected = [utils.add_violation(7)]
        self.oFile.lines.append(line.line('  for i in -32768 to 32767 loop')) #1
        self.oFile.lines.append(line.line('  a <= b -32768')) #2
        self.oFile.lines.append(line.line('  a <= c + -32768')) #3
        self.oFile.lines.append(line.line('  a <= to -32768')) #4
        self.oFile.lines.append(line.line('  a <= (-32 downto -568)')) #5
        self.oFile.lines.append(line.line('  a <= c_constant -144')) #6
        self.oFile.lines.append(line.line('  a <= c_constant -144_stuff')) #7

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
