
from vsg.vhdlFile.classify_new import context_reference
from vsg.vhdlFile.classify_new import library_clause
from vsg.vhdlFile.classify_new import use_clause


def detect(iToken, lObjects):
    '''
    context_item ::=
        library_clause
      | use_clause
      | context_reference
    '''

    iCurrent = library_clause.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = use_clause.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = context_reference.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
