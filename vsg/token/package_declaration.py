
from vsg import parser


class package_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_package_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_package_simple_name(parser.simple_name):

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
