import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','comment','comment_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileCommentAssignments(unittest.TestCase):


    def test_isComment_assignment(self):
        lExpected = [2,3,7,8,12,13,14,17,19,20,21,22,23,27,30,41,45,49,55,67,71,75,81,86]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isComment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_hasComment_assignment(self):
        lExpected = [2,3,7,8,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,60,61,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasComment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_hasInlineComment_assignment(self):
        lExpected = [15,16,18,25,26,28,29,39,40,43,44,46,47,48,50,51,52,53,54,57,58,60,61,62,65,66,68,69,70,72,73,74,76,77,78,79,80]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasInlineComment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_commentColumn_assignment(self):
        lExpected = [0,1,0,2,0,2,4,18,18,18,19,18,4,5,4,3,23,22,23,23,23,19,35,38,4,36,37,5,37,37,37,35,37,38,37,37,38,4,52,43,49,50,49,32,33,4,32,31,32,6,32,32,32,30,32,33,32,32,32,4,0]
        # Generic actual list
        lActual = []
        for oLine in oFile.lines:
            if oLine.hasComment:
                lActual.append(oLine.commentColumn)
        # Compare
        self.assertEqual(lActual, lExpected)
