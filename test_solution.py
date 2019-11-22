from unittest import TestCase
import sys
import pytest

from solution import Solution


class SolutionTest(TestCase):
    def test_get_file_name(self):
        """ Tests cases when proper file name is given and when it is not. """
        s = Solution()

        # File name not provided: ensure SystemExit exception raised and proper message printed
        sys.argv = ['solution.py']
        with self.assertRaises(SystemExit):
            s.get_file_name()
        out, err = self.capfd.readouterr()
        assert "Error: File name must be provided from the command line." in out 

        # File name is provided: ensure no error message printed
        sys.argv = ['solution.py', 'inputs/input1.txt']
        s.get_file_name()
        out, err = self.capfd.readouterr()
        assert out == ""

    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd