
from vsg.token import index_constraint as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import discrete_range
from vsg.vhdlFile.classify_new import subtype_indication


def classify(iToken, lObjects):
    '''
    index_constraint ::=
        ( discrete_range { , discrete_range } )
    '''

    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iToken, lObjects)

    while not utils.is_next_token(')', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)
        iCurrent = discrete_range.classify(iCurrent, lObjects)
    
    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    return iCurrent
