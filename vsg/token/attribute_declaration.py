
from vsg import parser


class attribute_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
