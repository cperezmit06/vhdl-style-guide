import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg import severity
from vsg.tests import utils

sSourceDir = os.path.join(os.path.dirname(__file__),'..','..','code_examples','c16')

lBaudGen = utils.read_vhdlfile(os.path.join(sSourceDir,'BaudGen.vhd'))
oBaudGen = vhdlFile.vhdlFile(lBaudGen)
lBoardCpu = utils.read_vhdlfile(os.path.join(sSourceDir,'Board_cpu.vhd'))
oBoardCpu = vhdlFile.vhdlFile(lBoardCpu)
lDataCore = utils.read_vhdlfile(os.path.join(sSourceDir,'data_core.vhd'))
oDataCore = vhdlFile.vhdlFile(lDataCore)

dLegacyConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','..','styles', 'indent_only.yaml'))
dLegacyConfig['debug'] = False

oSeverityList = severity.create_list({})

class testCodeExample(unittest.TestCase):

    @unittest.skip('Waiting until all rules have been refactored for new parser')
    def test_baudgen(self):
        oRuleList = rule_list.rule_list(oBaudGen, oSeverityList)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'BaudGen.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oBaudGen.lines[iLineNumber].line, sLine)

    @unittest.skip('Waiting until all rules have been refactored for new parser')
    def test_board_cpu(self):
        oRuleList = rule_list.rule_list(oBoardCpu, oSeverityList)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Board_cpu.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oBoardCpu.lines[iLineNumber].line, sLine)

    @unittest.skip('Waiting until all rules have been refactored to new parser.')
    def test_data_core(self):
        oRuleList = rule_list.rule_list(oDataCore, oSeverityList)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7, dLegacyConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'data_core.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oDataCore.lines[iLineNumber].line, sLine)
