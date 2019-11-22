from unittest import TestCase
from models.driver import Driver


class DriverTest(TestCase):
    """
    Encapsulates all the tests for Driver class
    """

    def test_contructor(self):
        """ Tests whether the constructor sets values to an instance correctly """
        self.d1 = Driver('Einstein', 0.0, 0.000)

        self.assertEqual('Einstein', self.d1.name)
        self.assertEqual(0.0, self.d1.total_hours)
        self.assertEqual(0.0, self.d1.total_miles)

    def test_get_name(self):
        """ Test whether the function returns the object's name """

        d1 = Driver('Einstein', 100.2, 0.000)
        self.assertEqual('Einstein', d1.get_name())

    def test_get_miles(self):
        """ Test whether the function returns the object's total miles """

        d1 = Driver('Einstein', 100.2, 0.000)
        self.assertEqual(100.2, d1.get_miles())

    def test_add_miles(self):
        """ Test whether the function add miles to exiting total miles """

        d1 = Driver('Edison', 1.0, 1.000)
        d1.add_miles(35)

        self.assertEqual(36, d1.get_miles())

    def test_get_hours(self):
        """ Test whether the function returns the object's total hours """

        d1 = Driver('Einstein', 0.0, 5.250)
        self.assertEqual(5.25, d1.get_hours())

    def test_add_hours(self):
        """ Test whether the function add hours to exiting total hours """

        d1 = Driver('Edison', 1.0, 1.000)
        d1.add_hours(3.2)

        self.assertEqual(4.2, d1.get_hours())
