from .driver import Driver


class Report:
    """ Take in a list and present result. """

    def __init__(self, output_list):
        self.output = output_list

    def print(self):
        """ Print output. """

        print()
        print("="*20)
        print("Result".center(20))
        print("="*20)

        if self.output:   # if output is not empty
            for driver in self.output:
                if driver.get_miles() > 0:
                    print("{}: {} miles @ {} mph".format(
                        driver.get_name(),
                        round(driver.get_miles()),
                        round(driver.get_miles()/driver.get_hours())
                    ))
                else:
                    print("{}: 0 miles".format(driver.get_name()))
        else:
            print("No result.")
        print()
