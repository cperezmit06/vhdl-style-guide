
from vsg import rule_item
from vsg import token
from vsg import violation


class rule_001(rule_item.Rule):
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

    def __init__(self):
        rule_item.Rule.__init__(self, name='with', identifier='001')
        self.solution = "Rewrite with as a process"
        self.phase = 1
        self.fixable = False

    def analyze(self, oFile):
        lToi = oFile.get_tokens_matching([token.concurrent_selected_signal_assignment.with_keyword])
        for oToi in lToi:
            self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        return
