from unittest import TestCase
import pytest
from models.file_handler import FileHandler


class FileHandlerTest(TestCase):

    def test_constructor(self):
        """ Test both cases when the target file can be opened and when the file couldn't be found """

        # valid file name
        f_valid = FileHandler('inputs/input1.txt')
        self.assertEqual(f_valid.file_name, 'inputs/input1.txt')
        self.assertListEqual(f_valid.output, [])

        # invalid file name
        with self.assertRaises((FileNotFoundError, SystemExit)):
            f_invalid = FileHandler('inputs/nonexistent.txt')

    def test_process_command(self):
        """ Tests whether "Driver", "Trip", and unknown commands are processed correctly """

        f_valid = FileHandler('inputs/input1.txt')

        # 'Driver' command
        old_output_len = len(f_valid.output)
        old_dict_len = len(f_valid.driver_to_idx)
        f_valid.process_command(['Driver', 'Chuck'])
        self.assertEqual(len(f_valid.output), old_output_len+1)
        self.assertEqual(len(f_valid.driver_to_idx), old_dict_len+1)

        # 'Trip' command - make sure reasonable trip mph is accounted correctly
        old_total_miles = f_valid.output[0].get_miles()
        old_total_hours = f_valid.output[0].get_hours()
        f_valid.process_command(
            ['Trip', 'Chuck', '18:00', '18:30', '25.8']   # 51.6 mph
        )
        self.assertEqual(f_valid.output[0].get_miles(), old_total_miles+25.8)
        self.assertEqual(f_valid.output[0].get_hours(), old_total_hours+0.5)

        # 'Trip' command - make sure ignores < 5mph and >100mph (hours and miles do not change).
        old_total_miles = f_valid.output[0].get_miles()
        old_total_hours = f_valid.output[0].get_hours()
        f_valid.process_command(
            ['Trip', 'Chuck', '00:00', '23:00', '100.0']   # 4.3 mph
        )
        self.assertEqual(f_valid.output[0].get_miles(), old_total_miles)
        self.assertEqual(f_valid.output[0].get_hours(), old_total_hours)

        old_total_miles = f_valid.output[0].get_miles()
        old_total_hours = f_valid.output[0].get_hours()
        f_valid.process_command(
            ['Trip', 'Chuck', '06:00', '06:30', '100.0']   # 200 mph
        )
        self.assertEqual(f_valid.output[0].get_miles(), old_total_miles)
        self.assertEqual(f_valid.output[0].get_hours(), old_total_hours)

        # unknown command
        with self.assertRaises(SystemExit):
            f_valid.process_command(['abc', 'Luffy'])  # unknown command 'abc'
        out, err = self.capfd.readouterr()
        assert "Error: Unknown input line format found." in out

    def test_print(self):
        """ Test to ensure there is output from print function """
        f_valid = FileHandler('inputs/input1.txt')
        f_valid.print()
        out, err = self.capfd.readouterr()
        assert out != ""

    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd

    def test_find_time_delta(self):
        """ Tests whether find_time_delta() returns the correct time difference, in hour unit """

        f_valid = FileHandler('inputs/input1.txt')
        res1 = f_valid.find_time_delta("00:01", "01:30")
        res2 = f_valid.find_time_delta("07:15", "13:00")

        self.assertEqual(res1, 1.483)   # 1 hours 29 mins = 1.4833 hours
        self.assertEqual(res2, 5.750)   # 5 hours 45 mins = 5.750 hours
