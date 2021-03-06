
from vsg import parser
from vsg import rule
from vsg import violation


class remove_spaces_before_token_rule(rule.rule):
    '''
    This class removes whitespace before a given token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oToken : token object
       The token where spaces will be removed before.
    '''

    def __init__(self, name, identifier, oToken, bIgnoreIfLineStart=False):

        rule.rule.__init__(self, name, identifier)
        self.phase = 2
        self.oToken = oToken
        self.solution = None
        self.bIgnoreIfLineStart = bIgnoreIfLineStart

    def analyze(self, oFile):
        lTokens = oFile.get_sequence_of_tokens_matching([parser.whitespace, self.oToken], self.bIgnoreIfLineStart)
        for oToken in lTokens:
            self.add_violation(violation.New(oToken.get_line_number(), oToken))

    def _fix_violations(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            oViolation.set_tokens(lTokens[1:])
        oFile.update(self.violations)
