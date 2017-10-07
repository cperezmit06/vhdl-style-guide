import os

import unittest
from vsg import vhdlFile

sFileLibraryName = os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd')
oFileLibrary = vhdlFile.vhdlFile(sFileLibraryName)

oFileSignal = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','signal','signal_test_input.vhd'))

oFileProcess = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','process','process_test_input.vhd'))
oFilePort = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input.vhd'))
oFileGeneric = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','generic','generic_test_input.vhd'))
oFileEntity = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','entity','entity_test_input.vhd'))
oFileConcurrent = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))
oFileArchitecture = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','architecture','architecture_test_input.vhd'))
oFileConstant = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','constant','constant_test_input.vhd'))


class testVhdlFileMethods(unittest.TestCase):

    def test_vhdlFile_class_exists(self):
        self.assertTrue(oFileLibrary)
        self.assertEqual(oFileLibrary.filename, sFileLibraryName)

    def test_loading_of_file(self):

        # Read in test file used for all tests
        lExpected = ['']
        with open(sFileLibraryName) as oExpectedFile:
            for sLine in oExpectedFile:
                lExpected.append(sLine.rstrip())
        oExpectedFile.close()
        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            self.assertEqual(oLine.line, lExpected[iIndex])

    def test_blank_line_assignment(self):

        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            if iIndex == 1 or iIndex == 2 or iIndex == 6 or iIndex == 8 or iIndex == 11 or \
               iIndex == 12 or iIndex == 15 or iIndex == 17 or iIndex == 18 or iIndex == 19 or \
               iIndex == 22 or iIndex == 25 or iIndex == 28 or iIndex == 30:
                self.assertTrue(oLine.isBlank)
            else:
                self.assertFalse(oLine.isBlank)

    def test_comment_assignment(self):
        lExpected = [50,76,83,90]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isComment:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_library_assignment(self):
        lExpected = [3,7,9,13,20,21]
        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibrary)
                self.assertEqual(oLine.indentLevel, 0)
            else:
                self.assertFalse(oLine.isLibrary)

    def test_library_use_assignment(self):
        lExpected = [4,5,10,14,16,23,24,26,27,29]
        # Compare
        for iIndex, oLine in enumerate(oFileLibrary.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibraryUse)
                self.assertEqual(oLine.indentLevel, 1)
            else:
                self.assertFalse(oLine.isLibraryUse)

    def test_insideEntity_assignment(self):
        lExpected = [0,1,2,17,18,48,64,79,92,93,104,105,106,107,108,109,110,111,112,124,125,126,134,135,136,137,145]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileEntity.lines):
            if not oLine.insideEntity:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEntityDeclaration_assignment(self):
        lExpected = [3,19,34,49,65,80,94,113,127,138]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileEntity.lines):
            if oLine.isEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndEntityDeclaration_assignment(self):
        lExpected = [16,33,47,63,78,91,103,123,133,144]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileEntity.lines):
            if oLine.isEndEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insidePortMap_assignment(self):
        lExpected = [8,9,10,11,12,13,14,15,25,26,27,28,29,30,31,39,40,41,42,43,44,45,46,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,86,87,88,89,90,98,99,100,101,102,118,119,120,121,122,128,129,130,131,132,133,140,141,142,143,144]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.insidePortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortKeyword_assignment(self):
        lExpected = [8,25,39,56,70,86,98,118,128,140]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndPortMap_assignment(self):
        lExpected = [15,31,46,62,77,90,102,122,133,144]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isEndPortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortDeclaration_assignment(self):
        lExpected = [9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,99,100,101,119,120,121,129,130,131,141,142]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFilePort.lines):
            if oLine.isPortDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_insideGenericMap_assignment(self):
        lExpected = [4,5,6,7,20,21,22,23,35,36,37,38,51,52,53,54,66,67,68,69,82,83,84,85,95,96,97,114,115,116,117,139,140,141]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.insideGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenericKeyword_assignment(self):
        lExpected = [4,20,35,51,66,82,95,114,139]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isGenericKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndGenericMap_assignment(self):
        lExpected = [7,23,38,54,69,85,97,117,141]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isEndGenericMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenericDeclaration_assignment(self):
        lExpected = [5,6,21,22,36,37,52,53,67,68,83,84,96,97,115,116,139,140]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileGeneric.lines):
            if oLine.isGenericDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideArchitecture_assignment(self):
        lExpected = [3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.insideArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureBegin_assignment(self):
        lExpected = [5,11,16,22,29,34,39,49]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isArchitectureKeyword_assignment(self):
        lExpected = [3,9,14,20,26,33,37,47]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isArchitectureKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture_assignment(self):
        lExpected = [7,13,18,24,31,35,45,55]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileArchitecture.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSignal_assignment(self):
        lExpected = [5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileSignal.lines):
            if oLine.isSignal:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConstant_assignment(self):
        lExpected = [5,6,7,8,9,10]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConstant.lines):
            if oLine.isConstant:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideProcess_assignment(self):
        lExpected = [6,7,8,9,11,12,13,14,15,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,38,39,40,41,42,46,47,48,51,52,53,55,56,57,58,59,60,63,64,65,68,69,70,71,72,75,76,77,78,79,81,82,83,84,85,86,88,89,90,91,92,93,94,97,98,99,100,101,102,103]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.insideProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessBegin_assignment(self):
        lExpected = [6,13,20,28,34,40,47,52,59,64,70,77,84,92,101]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isProcessKeyword_assignment(self):
        lExpected = [6,11,17,24,32,38,46,51,55,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isProcessKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndProcess_assignment(self):
        lExpected = [9,15,22,30,36,42,48,53,60,65,72,79,86,94,103]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isEndProcess:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideSensitivityList_assignment(self):
        lExpected = [6,11,12,17,18,19,24,25,26,27,32,33,38,39,46,51,55,56,57,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.insideSensitivityList:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSensitivityListBegin_assignment(self):
        lExpected = [6,11,17,24,32,38,46,51,55,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isSensitivityListBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isSensitivityListEnd_assignment(self):
        lExpected = [6,12,19,27,33,39,46,51,57,63,68,75,81,88,97]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileProcess.lines):
            if oLine.isSensitivityListEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideConcurrent_assignment(self):
        lExpected = [6,7,8,9,10,11,23,24,26,27,28,29,30,32,33,34,35,36,38,39,40,41,42]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.insideConcurrent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isConcurrentBegin_assignment(self):
        lExpected = [6,7,8,9,11,23,24,26,32,33,34,35,38,39,42]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.isConcurrentBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndConcurrent_assignment(self):
        lExpected = [6,7,8,10,11,23,24,30,32,33,34,36,38,41,42]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFileConcurrent.lines):
            if oLine.isEndConcurrent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


if __name__ == '__main__':
    unittest.main()