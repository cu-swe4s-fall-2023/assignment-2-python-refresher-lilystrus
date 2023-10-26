import sys
import os
import unittest

sys.path.append('../../src')
sys.path.append('../../data')

import analysis_utils  # noqa


class TestAnalysis(unittest.TestCase):

    # check that it correctly reads the file if it exists
    # and the correct number of arguments is given
    def test_handle_read_csv_correct(self):
        self.assertIsNotNone(analysis_utils.handle_read_csv('Agro_co2_USA.csv', 'Area'))

if __name__ == '__main__':
    unittest.main()
