
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import generic_map_aspect as token


class rule_017(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Instantiation rule 017 checks for generic map keyword and generic assignment on the same line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'instantiation', '017', token.open_parenthesis)
        self.solution = 'Move generic assignment to it\'s own line.'
