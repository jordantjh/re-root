from unittest import TestCase
import pytest
from models.report import Report
from models.driver import Driver


class ReportTest(TestCase):
    def test_constructor(self):
        """ Test whether constructor sets correctly """
        d1 = Driver('a', 0, 0)
        d2 = Driver('b', 0, 0)
        r = Report([d1, d2])

        self.assertListEqual(r.output, [d1, d2])

    def test_print(self):
        """ Test both cases when output is empty and when it is not """

        # output = []
        r1 = Report([])
        r1.print()
        out, err = self.capfd.readouterr()
        assert "No result." in out

        # output = [d1]
        d1 = Driver('a', 0, 0)
        r2 = Report([d1])
        r2.print()
        out, err = self.capfd.readouterr()
        assert "No result." not in out

    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd
