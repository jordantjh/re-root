from unittest import TestCase
from models.file_handler import FileHandler


class FileHandlerTest(TestCase):

    def test_constructor(self):
        """ Test both cases when the target file can be opened and when the file couldn't be found """

        # valid file name
        f_valid = FileHandler('test_inputs/input1.txt')
        self.assertEqual(f_valid.file_name, 'test_inputs/input1.txt')
        self.assertListEqual(f_valid.output, [])

        # invalid file name
        with self.assertRaises((FileNotFoundError, SystemExit)):
            f_invalid = FileHandler('test_inputs/nonexistent.txt')

    def test_find_time_delta(self):
        """ Tests whether find_time_delta() returns the correct time difference, in hour unit """

        f_valid = FileHandler('test_inputs/input1.txt')
        res1 = f_valid.find_time_delta("00:01", "01:30")
        res2 = f_valid.find_time_delta("07:15", "13:00")

        self.assertEqual(res1, 1.483)   # 1 hours 29 mins = 1.4833 hours
        self.assertEqual(res2, 5.750)   # 5 hours 45 mins = 5.750 hours
