

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    start_token : token object
       reference token to align comments with

    stop_token : token object
       The token that ends the region to perform the alignment
    '''

    def __init__(self, name, identifier, start_token, stop_token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 4
        self.start_token = start_token
        self.stop_token = stop_token

    def analyze(self, oFile):

        lToi = oFile.get_tokens_where_line_starts_with_token_until_ending_token_is_found(self.start_token, self.stop_token)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()

            for iIndex in range(0, len(lTokens)):
               oToken = lTokens[iIndex]

               if isinstance(oToken, self.start_token):
                   iTargetIndent = oToken.get_indent()
                   iWhitespaceLength = iTargetIndent * self.indentSize + len(oToken.get_value()) + 1

               if isinstance(oToken, self.stop_token):
                   break

               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   if isinstance(lTokens[iIndex + 1], parser.whitespace):
                       if len(lTokens[iIndex + 1].get_value()) != iWhitespaceLength:
                           oLineTokens = oFile.get_tokens_from_line(iLine)
                           oViolation = violation.New(iLine, oLineTokens, self.solution)
                           dAction = {}
                           dAction['type'] = 'adjust'
                           dAction['adjust'] = iWhitespaceLength
                           oViolation.set_action(dAction)
                           self.violations.append(oViolation)
                   else:
                       oLineTokens = oFile.get_tokens_from_line(iLine)
                       oViolation = violation.New(iLine, oLineTokens, self.solution)
                       dAction = {}
                       dAction['type'] = 'insert'
                       dAction['adjust'] = iWhitespaceLength
                       oViolation.set_action(dAction)
                       self.violations.append(oViolation)


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
            if dAction['type'] == 'adjust':
                lTokens[0].set_value(' ' * dAction['adjust'])
            elif dAction['type'] == 'insert':
                lTokens.insert(0, parser.whitespace(' ' * dAction['adjust']))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)

