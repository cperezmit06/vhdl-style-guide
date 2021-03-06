

from vsg import parser
from vsg import rule_item
from vsg import token
from vsg.vhdlFile import utils
from vsg import violation


class remove_comments_from_end_of_lines_bounded_by_tokens(rule_item.Rule):
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

    def __init__(self, name, identifier, oStart, oEnd):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.oStart = oStart
        self.oEnd = oEnd

    def analyze(self, oFile):

        lToi = oFile.get_tokens_bounded_by(self.oStart, self.oEnd)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.carriage_return):
                    iLine += 1
                if isinstance(oToken, parser.comment):
                    if isinstance(lTokens[iToken + 1], parser.carriage_return):
                        if isinstance(lTokens[iToken - 1], parser.carriage_return) or \
                           isinstance(lTokens[iToken - 2], parser.carriage_return):
                            continue
                        else:
                            if isinstance(lTokens[iToken - 1], parser.whitespace):
                                oNewToi = oToi.extract_tokens(iToken - 1, iToken)
                            else:
                                oNewToi = oToi.extract_tokens(iToken, iToken)
                            oViolation = violation.New(oNewToi.get_line_number(), oNewToi, self.solution)
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
            oViolation.set_tokens([])
               
        oFile.update(self.violations)
