
from vsg.vhdlFile.classify_new import assertion_statement
#from vsg.vhdlFile.classify_new import case_statement
from vsg.vhdlFile.classify_new import exit_statement
from vsg.vhdlFile.classify_new import loop_statement
from vsg.vhdlFile.classify_new import next_statement
from vsg.vhdlFile.classify_new import null_statement
from vsg.vhdlFile.classify_new import procedure_call_statement
from vsg.vhdlFile.classify_new import report_statement
from vsg.vhdlFile.classify_new import return_statement
from vsg.vhdlFile.classify_new import signal_assignment_statement
from vsg.vhdlFile.classify_new import wait_statement

'''
    sequential_statement ::=
        wait_statement
      | assertion_statement
      | report_statement
      | signal_assignment_statement
      | variable_assignment_statement
      | procedure_call_statement
      | if_statement
      | case_statement
      | loop_statement
      | next_statement
      | exit_statement
      | return_statement
      | null_statement
'''


def detect(iToken, lObjects):

    iReturn = wait_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = assertion_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = report_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = signal_assignment_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    iReturn = variable_assignment_statement.detect(iToken, lObjects)
#    if iReturn != iToken:
#        return iReturn

    iReturn = procedure_call_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    iReturn = if_statement.detect(iToken, lObjects)
#    if iReturn != iToken:
#        return iReturn

#    iReturn = case_statement.detect(iToken, lObjects)
#    if iReturn != iToken:
#        return iReturn

    iReturn = loop_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = next_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = exit_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = return_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = null_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken