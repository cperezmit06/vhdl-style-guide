

from vsg import rule_item
from vsg import utils
from vsg import parser

from vsg import violation


class existence_of_tokens_which_should_not_occur(rule_item.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    '''

    def __init__(self, name, identifier, lTokens):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens
        self.fixable = False

    def analyze(self, oFile):
        lToi = oFile.get_tokens_matching(self.lTokens)
        for oToi in lToi:
            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.add_violation(oViolation)


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        return
