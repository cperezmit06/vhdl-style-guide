
from vsg.token import case_statement_alternative as token

from vsg.vhdlFile.classify_new import choices
from vsg.vhdlFile.classify_new import sequence_of_statements

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    case_statement_alternative ::=
        when choices =>
            sequence_of_statements
    '''
    if utils.is_next_token('when', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)

    iCurrent = choices.classify_until(['=>'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('=>', token.assignment, iCurrent, lObjects)

    iCurrent = sequence_of_statements.detect(iCurrent, lObjects)

    return iCurrent
