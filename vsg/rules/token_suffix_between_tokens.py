

from vsg import rule_item
from vsg import utils
from vsg import parser

from vsg import violation


class token_suffix_between_tokens(rule_item.Rule):
    '''
    Checks the suffix of a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lSuffixes: string list
       acceptable suffixes
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 7
        self.lTokens = lTokens
        self.suffixes = None
        self.configuration.append('suffixes')
        self.fixable = False
        self.disable = True
        self.oStart = oStart
        self.oEnd = oEnd

    def analyze(self, oFile):
        lToi = oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sToken = lTokens[0].get_value().lower()
            bValid = False
            for sSuffix in self.suffixes:
                if sToken.endswith(sSuffix):
                    bValid = True
            if not bValid:
                sSolution = 'Suffix ' + lTokens[0].get_value() + ' with one of the following: ' + ', '.join(self.suffixes)
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                self.add_violation(oViolation)


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        return
