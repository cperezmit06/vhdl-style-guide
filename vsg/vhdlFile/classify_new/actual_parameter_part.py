
from vsg.vhdlFile.classify_new import association_list


def classify(iTokent, lObjects):
    '''
    actual_parameter_part ::=
        *parameter*_association_list
    '''

    return association_list.classify(iTokent, lObjects)
