import sys

from models.driver import Driver
from models.report import Report


class FileHandler:
    """
    Handles processing of the input file.
    """

    def __init__(self, file_name):
        """ set instance's file_name and file_handler properties. """

        self.file_name = file_name
        self.output = []
        self.driver_to_idx = {}  # key: driver name; value: index to the driver in 'output'

        # open file
        try:
            self.file_handler = open(
                self.file_name, mode="r", encoding="utf-8")
        except FileNotFoundError:
            print("Error: \"{}\" cannot be found.\n".format(file_name))
            sys.exit()
        except:
            print("Error: an error occurred when opening the input file.")
            sys.exit()

    def process(self):
        """ Process file line by line. """

        driver_to_idx = {}   # for O(1) access

        # read the input file line by line
        for line in self.file_handler.read().splitlines():
            if line == "":
                continue   # skip to next line

            parsed_line_list = line.split()

            # "Driver" command
            # process_driver_command(parsed_line_list)
            if parsed_line_list[0] == 'Driver':
                command, driver_name = tuple(parsed_line_list)

                # record new driver
                self.output.append(Driver(driver_name, 0.0, 0.000))
                self.driver_to_idx[driver_name] = len(
                    self.output) - 1   # record index

            # "Trip" command
            elif parsed_line_list[0] == 'Trip':
                command, driver_name, start_time, \
                    end_time, miles_driven = tuple(parsed_line_list)
                hours_driven = self.find_time_delta(start_time, end_time)

                # ignore trips with 0 travel time
                if hours_driven > 0:
                    cur_mph = float(miles_driven)/hours_driven
                    # ignore trips that are < 5 mph or > 100 mph
                    if 5 <= cur_mph <= 100:
                        # update the driver's info
                        cur_driver = self.output[self.driver_to_idx[driver_name]]
                        cur_driver.add_miles(float(miles_driven))
                        cur_driver.add_hours(hours_driven)

            else:
                print("Error: Unknown input line format found.\n")
                sys.exit()

        # sort output list by total miles
        self.output.sort(
            key=lambda driver: driver.get_miles(), reverse=True)

    def find_time_delta(self, start_time, end_time):
        """ A helper function to process() """
        """ Finds the difference between end time and start time, in hour unit """

        start_time_hour, start_time_min = tuple(start_time.split(":"))
        end_time_hour, end_time_min = tuple(end_time.split(":"))

        if int(end_time_min) < int(start_time_min):
            delta_hour = int(end_time_hour) - 1 - int(start_time_hour)
            delta_min = int(end_time_min) + 60 - int(start_time_min)
        else:
            delta_hour = int(end_time_hour) - int(start_time_hour)
            delta_min = int(end_time_min) - int(start_time_min)

        # round result to 3 decimal points
        return round(delta_hour + (delta_min/60), 3)

    def print(self):
        """ Output result. """

        r = Report(self.output)
        r.print()

    def __del__(self):
        """ close file handler """

        try:
            self.file_handler.close()
        except AttributeError:   # triggered when file not found
            pass
        except:
            print("Error: an error occurred in FileHandler's destructor.")
