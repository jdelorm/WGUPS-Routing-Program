# Class for truck_packages

class Package:

    # Method that initializes package objects
    def __init__(self, package_id, package_address, package_city, package_state, package_zipcode,
                 package_deliver_by_time, package_weight, package_status):
        self.id, self.address, self.city, self.state, self.zipcode, self.deliver_by_time, self.weight, self.status = (
            package_id, package_address, package_city, package_state, package_zipcode, package_deliver_by_time,
            package_weight, package_status
        )
        self.departure_time = None
        self.delivery_time = None

    # Method that returns string values of package objects
    def __str__(self):
        return (f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zipcode}, {self.deliver_by_time}, "
                f"{self.weight}, {self.delivery_time}, {self.status}")

    # Method that checks and returns the current delivery status of a package object based on a user input time
    def update_status(self, user_input_time):
        if self.delivery_time <= user_input_time:
            # print(self.departure_time) - used for testing
            self.status = "Package Delivered - Current Time: " + str(user_input_time)
            self.delivery_time = "Delivered at " + str(self.delivery_time)
        elif self.departure_time < user_input_time:
            # print(self.departure_time) - used for testing
            self.status = "Package is Out for Delivery - Current Time: " + str(user_input_time)
            self.delivery_time = "Package will be delivered at " + str(self.delivery_time)
        else:
            # print(self.departure_time) - used for testing
            self.status = "At Local Hub - Preparing for Delivery - Current Time: " + str(user_input_time)
            self.delivery_time = "Package will be delivered at " + str(self.delivery_time)
