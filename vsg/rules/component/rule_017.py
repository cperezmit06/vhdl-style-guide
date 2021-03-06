
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.interface_unknown_declaration.colon)


class rule_017(align_tokens_in_region_between_tokens):
    '''
    Component rule 017 ensures the alignment of the colon for each generic and port in the component declaration.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'component', '017', lAlign, token.component_declaration.component_keyword, token.component_declaration.end_keyword)
        self.solution = 'Align :.'
