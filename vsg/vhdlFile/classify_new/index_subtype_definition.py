
from vsg.token import index_subtype_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import type_mark

'''
    index_subtype_definition ::=
        type_mark range <>
'''


def classify(iToken, lObjects):
    iCurrent = type_mark.classify(iToken, lObjects)
    iCurrent = utils.assign_next_token_required('range', token.range_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<>', token.undefined_range, iCurrent, lObjects)
    return iCurrent
