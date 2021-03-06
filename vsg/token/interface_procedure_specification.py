from vsg import parser


class procedure_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class parameter_keyword(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class designator(parser.designator):

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
