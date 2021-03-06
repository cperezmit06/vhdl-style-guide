

from vsg import rule_item
from vsg import utils
from vsg import parser

from vsg import violation


lKeywords = []
lKeywords.append('std_logic')
lKeywords.append('std_logic_vector')
lKeywords.append('integer')
lKeywords.append('signed')
lKeywords.append('unsigned')
lKeywords.append('natural')
lKeywords.append('std_ulogic')


class token_case_n_token_after_tokens(rule_item.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self, name, identifier, iToken, lTokens, bLimitToVhdlKeywords=False):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.iToken = iToken
        self.lTokens = lTokens
        self.disabled = False
        self.bLimitToVhdlKeywords = bLimitToVhdlKeywords

    def analyze(self, oFile):
        lToi = oFile.get_n_token_after_tokens(self.iToken, self.lTokens)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sObjectValue = lTokens[0].get_value()
            if self.bLimitToVhdlKeywords:
                if sObjectValue.lower() not in lKeywords:
                    continue
            if self.case == 'lower':
                if not sObjectValue.islower():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.lower() + '"'
                    self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))
            if self.case == 'upper':
                if not sObjectValue.isupper():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.upper() + '"'
                    self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))


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
            if self.case == 'lower':
                lTokens[0].set_value(lTokens[0].get_value().lower())
            if self.case == 'upper':
                lTokens[0].set_value(lTokens[0].get_value().upper())
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)

