# Class for trucks

class Truck:

    # Method that initializes truck objects
    def __init__(self, truck_capacity, truck_speed, truck_load, truck_packages, truck_current_miles, package_address,
                 truck_departure_time):
        self.capacity, self.speed, self.load, self.packages, self.current_miles, self.address, self.departure_time = (
            truck_capacity, truck_speed, truck_load, truck_packages, truck_current_miles, package_address,
            truck_departure_time
        )
        self.time = truck_departure_time

    # Method that returns string values of a truck object
    def __str__(self):
        return (f"{self.capacity}, {self.speed}, {self.load}, {self.packages}, {self.current_miles}, {self.address}, "
                f"{self.departure_time}")
