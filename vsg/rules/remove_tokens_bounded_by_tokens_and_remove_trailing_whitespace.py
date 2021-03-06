

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region
    '''

    def __init__(self, name, identifier, left_token, right_token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.left_token = left_token
        self.right_token = right_token


    def analyze(self, oFile):

        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token, include_trailing_whitespace=True)
        for oToi in lToi:
           self.violations.append(violation.New(oToi.get_line_number(), oToi, self.solution))


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
            oViolation.set_tokens([])
        oFile.update(self.violations)
