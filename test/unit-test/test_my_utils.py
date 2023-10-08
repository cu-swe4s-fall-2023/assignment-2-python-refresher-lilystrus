import sys
import os
import unittest
import random
import statistics

# sys.path.append('../src') : not working ?
# found alternative :

# get the current directory
cwdir = os.getcwd()
# go back one directory (/test)
pardir = os.path.dirname(cwdir)
# go back another directory (the repo dir)
grpardir = os.path.dirname(pardir)
# go forward one directory into src
srcdir = grpardir+'/src'
# append it to the path
sys.path.append(srcdir)

import my_utils  # nopep8


class TestMyUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.listpos = []
        cls.listneg = []
        for i in range(100):
            randpos = random.randint(1, 300)
            cls.listpos.append(randpos)
            randneg = random.randint(-300, 300)
            cls.listneg.append(randneg)

    @classmethod
    def tearDownClass(cls):
        pass

    # Make sure that a character string is not accept
    def test_convertStrInt_failure(self):
        self.assertIsNone(my_utils.convert_str_to_int('Lily'))

    # Make sure that a numerical string is accepted
    def test_convertStrInt_success(self):
        self.assertIsNotNone(my_utils.convert_str_to_int('1'))

    # Test that it finds the file when correct name is given
    def test_fileFound(self):
        self.assertIsNotNone(my_utils.handle_file_io(
                            'Agrofood_co2_emission.csv'))

    # Test that it catches problems when incorrect name is given
    def test_fileNotFound(self):
        self.assertIsNone(my_utils.handle_file_io('Agrofood_co2.csv'))

    # Make sure it finds the correct length
    def test_correct_length(self):
        self.assertEqual(my_utils.valid_length([1, 2, 3, 4]), 4)

    # Make sure it handles an empty list correctly
    def test_handle_empty(self):
        self.assertIsNone(my_utils.valid_length([]))

    # Make sure it finds the right mean: positive integers
    def test_mean_posint(self):
        direct_mean = statistics.mean(self.listpos)
        self.assertEqual(my_utils.find_mean(self.listpos), direct_mean)

    # Make sure it finds the right mean: negative integers
    def test_mean_negint(self):
        direct_mean = statistics.mean(self.listneg)
        self.assertEqual(my_utils.find_mean(self.listneg), direct_mean)

    # Make sure it finds the right median: positive integers
    def test_median_posint(self):
        direct_median = statistics.median(self.listpos)
        self.assertEqual(my_utils.find_median(self.listpos), direct_median)

    # Make sure it finds the right median : negative integers
    def test_median_negint(self):
        direct_median = statistics.median(self.listneg)
        self.assertEqual(my_utils.find_median(self.listneg), direct_median)

    # Make sure it finds the right median: positive integers
    def test_std_posint(self):
        direct_std = statistics.stdev(self.listpos)
        direct_mean = statistics.mean(self.listpos)
        start = round(my_utils.find_std(self.listpos, direct_mean) - 5.0)
        end = round(my_utils.find_std(self.listpos, direct_mean) + 5.0)
        CompareArray = list(range(start, end))
        self.assertIn(round(direct_std), CompareArray)

    # Make sure it finds the right median : negative integers
    def test_std_negint(self):
        direct_std = statistics.stdev(self.listneg)
        direct_mean = statistics.mean(self.listneg)
        start = round(my_utils.find_std(self.listneg, direct_mean) - 5.0)
        end = round(my_utils.find_std(self.listneg, direct_mean) + 5.0)
        CompareArray = list(range(start, end))
        self.assertIn(round(direct_std), CompareArray)


if __name__ == '__main__':
    unittest.main()
