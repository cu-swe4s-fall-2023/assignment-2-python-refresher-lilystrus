import sys
import os
import unittest

sys.path.append('../../src')
sys.path.append('../../data')

import analysis_utils  # noqa

cwdir = os.getcwd()
# go back one directory (/test)
pardir = os.path.dirname(cwdir)
# go back another directory (the repo dir)
grpardir = os.path.dirname(pardir)
# go forward one directory into src
srcdir = grpardir+'/src'
os.chdir(srcdir)


class TestAnalysis(unittest.TestCase):

    # check that it correctly reads the file if it exists
    # and the correct number of arguments is given
    def test_handle_read_csv_correct(self):
        self.assertIsNotNone(
            analysis_utils.handle_read_csv('Agro_co2_Afgha.csv', 'Area'))

    # check that it exits if the file does not exist
    def test_handle_read_csv_nofile(self):
        with self.assertRaises(SystemExit):
            analysis_utils.handle_read_csv('Agrofood_emission.csv',
                                           'Afghanistan')

    # check that it exits if the user did not give correct number of arguments
    def test_handle_read_csv_arguments(self):
        with self.assertRaises(TypeError):
            analysis_utils.handle_read_csv('Agrofood_co2_emission.csv')

    # check that it correctly reads the file when it exists
    def test_read_file_contents_correct(self):
        result = analysis_utils.handle_open_txt('Algeria_total_emission.txt')
        self.assertNotEqual(result, [])

    # check that it exits if the file does not exist
    def test_handle_open_txt_nofile(self):
        with self.assertRaises(SystemExit):
            analysis_utils.handle_open_txt('Greece_total_emission.txt')

    # check that it correctly opens the image when it exists
    def test_handle_image_open_correct(self):
        result = analysis_utils.handle_image_open('t1.png')
        self.assertIsNotNone(result)

    # check that it exits if the file does not exist
    def test_handle_image_open_nofile(self):
        with self.assertRaises(SystemExit):
            analysis_utils.handle_image_open('Greece_Forestland.png')

    # check that it finds non-zero dimensions if all goes well
    def test_find_final_dimensions_correct(self):
        image1 = analysis_utils.handle_image_open('t1.png')
        image2 = analysis_utils.handle_image_open('t2.png')
        image3 = analysis_utils.handle_image_open('t3.png')
        image4 = analysis_utils.handle_image_open('t4.png')
        x1, x2 = analysis_utils.find_final_dimensions([image1, image2,
                                                       image3, image4])
        self.assertNotEqual(x1, 0)
        self.assertNotEqual(x2, 0)


if __name__ == '__main__':
    unittest.main()
