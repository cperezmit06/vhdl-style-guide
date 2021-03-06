import os

import unittest

from vsg import vhdlFile
from vsg.tests import utils

from vsg.token import concurrent_procedure_call_statement as token
from vsg.token import procedure_call


sTestDir = os.path.join(os.path.dirname(__file__),   'concurrent_statement')
lFile = utils.read_vhdlfile(os.path.join(sTestDir, 'classification_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class test_token(unittest.TestCase):


    def test_classification(self):

        lExpected = []
        utils.read_file(os.path.join(sTestDir, 'classification_results.txt'), lExpected, False)

        lActual = []

        for oObject in utils.extract_objects(oFile, True):
            lActual.append(str(oObject))
        
        self.assertEqual(lExpected, lActual)

