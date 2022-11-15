import unittest
from csv_combiner import merge_csv_files
'''
@author Enliang Wu
'''


class TestCombiner(unittest.TestCase):
    # testing if the input does not have enough files
    def test_not_enough_input(self):
        self.assertFalse(merge_csv_files([]))
        self.assertFalse(merge_csv_files(['fixtures/clothing.csv']))

    # testing if the input contains files that are not existed
    def test_file_no_found(self):
        self.assertFalse(merge_csv_files(['fixtures/clothing2.csv', 'fixtures/household_cleaners.csv']))

    # testing if the files combined successfully
    def test_combiner(self):
        self.assertTrue(merge_csv_files(['fixtures/clothing.csv', 'fixtures/household_cleaners.csv']))
        self.assertTrue(merge_csv_files(['fixtures/clothing.csv', 'fixtures/household_cleaners.csv',
                                         'fixtures/accessories.csv']))


if __name__ == '__main__':
    unittest.main()
