class Driver:
    """
    A model that describes a driver
    """

    def __init__(self, name, miles, hours):
        self.name = name
        self.total_miles = miles   # preserve 1 decimal point
        self.total_hours = hours   # preserve 3 decimal points

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def add_miles(self, miles):
        self.total_miles += miles

    def add_hours(self, hours):
        self.total_hours += hours

    def get_name(self):
        return self.name

    def get_miles(self):
        return self.total_miles

    def get_hours(self):
        return self.total_hours
