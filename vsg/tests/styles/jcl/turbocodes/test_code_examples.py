import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg import severity
from vsg.tests import utils

lIteration = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','..','code_examples', 'turbocodes', 'iteration_synth.vhd'))
oIteration = vhdlFile.vhdlFile(lIteration)

dConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','..','styles', 'jcl.yaml'))
dConfig['debug'] = False

oSeverityList = severity.create_list({})

class testCodeExample(unittest.TestCase):

    @unittest.skip('Need to wait until all rules have been refactored.')
    def test_iteration_synth(self):
        oRuleList = rule_list.rule_list(oIteration, oSeverityList)
        oRuleList.configure(dConfig)
        oRuleList.fix()
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'iteration_synth.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oIteration.lines[iLineNumber].line, sLine)
