

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class n_spaces_before_and_after_tokens(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token type pairs
       The tokens to check for a single space between
    '''

    def __init__(self, name, identifier, iSpaces, lTokens, bNIsMinimum=False):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.iSpaces = iSpaces
        self.lTokens = lTokens
        self.bNIsMinimum = bNIsMinimum

    def analyze(self, oFile):
        lToi = []

        lToi = oFile.get_n_tokens_before_and_after_tokens(1, self.lTokens)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            dAction = {}

            oLeft = lTokens[0]
            if not isinstance(oLeft, parser.carriage_return):
                if isinstance(oLeft, parser.whitespace):
                    if self.bNIsMinimum:
                        if self.iSpaces > len(oLeft.get_value()):
                            dAction['left'] = {}
                            dAction['left']['action'] = 'adjust'
                    elif self.iSpaces != len(oLeft.get_value()):
                        dAction['left'] = {}
                        dAction['left']['action'] = 'adjust'
                else:
                    dAction['left'] = {}
                    dAction['left']['action'] = 'insert'

            oRight = lTokens[-1]
            if not isinstance(oRight, parser.carriage_return):
                if isinstance(oRight, parser.whitespace):
                    if self.bNIsMinimum:
                        if self.iSpaces > len(oRight.get_value()):
                            dAction['right'] = {}
                            dAction['right']['action'] = 'adjust'
                    elif self.iSpaces != len(oLeft.get_value()):
                        dAction['right'] = {}
                        dAction['right']['action'] = 'adjust'
                else:
                    dAction['right'] = {}
                    dAction['right']['action'] = 'insert'

            if len(list(dAction.keys())) > 0:
                sSolution = create_solution_text(dAction, self.iSpaces, lTokens)
                oViolation = violation.New(iLine, oToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            dAction = oViolation.get_action()
            lKeys = list(dAction.keys())
            for sKey in lKeys:
                if sKey == 'left':
                    if dAction[sKey]['action'] == 'adjust':
                        lTokens[0].set_value(' '*self.iSpaces)
                    else:
                        lTokens.insert(1, parser.whitespace(' '))
                if sKey == 'right':
                    if dAction[sKey]['action'] == 'adjust':
                        lTokens[-1].set_value(' '*self.iSpaces)
                    else:
                        lTokens.insert(len(lTokens) -1, parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)


def create_solution_text(dAction, iNumSpaces, lTokens):
    sReturn = ''
    for sKey in list(dAction.keys()):
        if sKey == 'left':
            if dAction[sKey]['action'] == 'adjust':
                sReturn += 'Remove all but one space before ' + lTokens[1].get_value()
            else:
                sReturn += 'Add ' + str(iNumSpaces) + ' space(s) before ' + lTokens[1].get_value()
        if sKey == 'right':
            if dAction[sKey]['action'] == 'adjust':
                sReturn += 'Remove all but one space after ' + lTokens[1].get_value()
            else:
                sReturn += 'Add ' + str(iNumSpaces) + ' space(s) after ' + lTokens[1].get_value()
