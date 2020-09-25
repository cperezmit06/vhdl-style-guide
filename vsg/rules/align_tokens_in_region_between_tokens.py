

from vsg import parser
from vsg import rule_item
from vsg import violation


class align_tokens_in_region_between_tokens(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object list
       List of tokens to align

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region
    '''

    def __init__(self, name, identifier, lTokens, left_token, right_token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 5
        self.lTokens = lTokens
        self.left_token = left_token
        self.right_token = right_token
        ## Stuff below is from original keyword_alignment_rule
        self.configuration_triggers = []

        self.compact_alignment = True
        self.configuration.append('compact_alignment')

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')

        self.configuration_triggers = [{'name': 'blank_line_ends_group', 'triggers': ['isBlank']},
                                       {'name': 'comment_line_ends_group', 'triggers': ['isComment']}]


    def analyze(self, oFile):

        lIncludeLines = []
        if not self.blank_line_ends_group:
            lIncludeLines.append(parser.blank_line)
        if not self.comment_line_ends_group:
            lIncludeLines.append(parser.comment)

        dAnalysis = {}

#        lToi = oFile.get_groups_of_lines_between_tokens_inclusive_that_contain_tokens_and_lines_starting_with_tokens(self.left_token, self.right_token, self.lTokens, lIncludeLines)
        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1

            for iIndex in range(0, len(lTokens)):
               iToken += 1
               oToken = lTokens[iIndex]

               if not bTokenFound:
                   for oSearch in self.lTokens:
                       if isinstance(oToken, oSearch):
                           bTokenFound = True
                           dAnalysis[iLine] = {}
                           dAnalysis[iLine]['token_column'] = iColumn
                           dAnalysis[iLine]['token_index'] = iToken
                           dAnalysis[iLine]['line_number'] = iLine
                           if isinstance(lTokens[iIndex -1], parser.whitespace):
                               dAnalysis[iLine]['left_column'] = iColumn - len(lTokens[iIndex - 1].get_value())
                           else:
                               dAnalysis[iLine]['left_column'] = iColumn
                           break

                   iColumn += len(oToken.get_value())
               
               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   iColumn = 0
                   bTokenFound = False
                   iToken = -1

            add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)


            for iKey in list(dAnalysis.keys()):
                if dAnalysis[iKey]['adjust'] != 0:
                    oLineTokens = oFile.get_tokens_from_line(iKey)
                    oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, self.solution)
                    oViolation.set_action(dAnalysis[iKey])
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
            iTokenIndex = dAction['token_index']

            if isinstance(lTokens[iTokenIndex - 1], parser.whitespace):
                iLen = len(lTokens[iTokenIndex - 1].get_value())
                lTokens[iTokenIndex - 1].set_value(' '*(iLen + dAction['adjust']))
            else:
                lTokens.insert(iTokenIndex, parser.whitespace(' '*dAction['adjust']))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment):
    iMaxLeftColumn = 0
    iMinLeftColumn = 9999999999999999
    iMaxTokenColumn = 0
    iMinTokenColumn = 9999999999999999

    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]['left_column'])
        iMinLeftColumn = min(iMinLeftColumn, dAnalysis[iKey]['left_column'])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]['token_column'])
        iMinTokenColumn = min(iMinTokenColumn, dAnalysis[iKey]['token_column'])

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxLeftColumn - dAnalysis[iKey]['token_column'] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxTokenColumn - dAnalysis[iKey]['token_column']
