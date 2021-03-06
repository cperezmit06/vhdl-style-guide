
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.generic_map_aspect.generic_keyword)
lTokens.append(token.generic_map_aspect.map_keyword)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_013(token_case_in_range_bounded_by_tokens):
    '''
    Checks the "generic map" keywords have proper case.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'instantiation', '013', lTokens, oStart, oEnd)
