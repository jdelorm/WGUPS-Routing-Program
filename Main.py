# John DeLorme
# Student ID 000893378
# C950 Task 2 Attempt 1

import csv
import datetime
import Truck
import sys
from builtins import ValueError
from HashTable import HashTable
from Package import Package


# Method used to read package data to create/initialize package objects and insert them into a hash table
def read_package(cvs_file, hash_table):
    with (open(cvs_file) as package_info):
        package_data = csv.reader(package_info)
        for package in package_data:
            package_address, package_city, package_state, package_zipcode, package_delivery_time, package_weight = package[
                                                                                                                   1:7]
            package_id = int(package[0])
            package_status = "At local Hub - Preparing for Delivery"

            p = Package(package_id, package_address, package_city, package_state, package_zipcode,
                        package_delivery_time, package_weight, package_status)

            hash_table.insert(package_id, p)


# Reads the distances csv file and creates a list of data
with open("wgups_csv/distances_csv") as csvfile:
    CSV_Distance = list(csv.reader(csvfile))


# Method used for reading travel distance between two addresses using the CSV_distance list
def travel_distance(x_value, y_value):
    distance = CSV_Distance[x_value][y_value] or CSV_Distance[y_value][x_value]
    return float(distance) if distance else 0.0


# Reads the addresses csv file and creates a list of data
with open("wgups_csv/addresses_csv") as csvfile1:
    CSV_Address = list(csv.reader(csvfile1))


# Method used to read the packages address from the CSV_Address list
def read_address(address):
    return next((int(row[0]) for row in CSV_Address if address in row[2]), None)


# Creates the first truck object with assigned initial data
first_truck = Truck.Truck(
    truck_capacity=16,
    truck_speed=18,
    truck_load=None,
    truck_packages=[1, 2, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
    truck_current_miles=0.0,
    package_address="4001 South 700 East",
    truck_departure_time=datetime.timedelta(hours=8, minutes=0, seconds=0)
)

# Creates the second truck object with assigned initial data
second_truck = Truck.Truck(
    truck_capacity=16,
    truck_speed=18,
    truck_load=None,
    truck_packages=[3, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],
    truck_current_miles=0.0,
    package_address="4001 South 700 East",
    truck_departure_time=datetime.timedelta(hours=10, minutes=20, seconds=0)
)

# Creates the third truck object with assigned initial data
third_truck = Truck.Truck(
    truck_capacity=16,
    truck_speed=18,
    truck_load=None,
    truck_packages=[4, 5, 6, 7, 8, 10, 11, 25, 28, 32, 33],
    truck_current_miles=0.0,
    package_address="4001 South 700 East",
    truck_departure_time=datetime.timedelta(hours=9, minutes=5, seconds=0)
)

# Creates a hash table
package_hash_table = HashTable()

# Inserts data into the hash table with information read from the packages_csv file
read_package("wgups_csv/packages_csv", package_hash_table)


# Method used to calculate the minimal travel distance using a greedy algorithm
# The method also calculates delivery times and distance traveled for each truck object
# Searching runtime in the method would be O(n)
# Removing runtime in the method would be O(n)
# Iterating runtime of the loop would be O(n)
# The worst case complexity of the algorithm would be O(n^2) or Quadratic
def delivery(truck):
    truck_route = [package_hash_table.search(packageID) for packageID in truck.packages]
    truck.packages.clear()

    while truck_route:
        next_package = min(truck_route, key=lambda package: travel_distance(read_address(truck.address),
                                                                            read_address(package.address)))

        next_address = travel_distance(read_address(truck.address), read_address(next_package.address))
        truck.packages.append(next_package.id)
        truck_route.pop(truck_route.index(next_package))
        truck.current_miles += next_address
        truck.address = next_package.address
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.departure_time


# Calls the delivery method on the first truck object
delivery(first_truck)
# Calls the delivery method on the second truck object
delivery(second_truck)
# Reassigns the third_truck.time with the highest truck.time value of the other two trucks, preventing
# the third truck from departing the hub until either of the other two trucks is finished delivering packages
third_truck.time = min(first_truck.time, second_truck.time)
# Calls the delivery method on the third truck object
delivery(third_truck)


# Main Class
class Main:

    # Method used to execute the program using the console as an interface
    # Displays a welcome message and the total mileage of all the trucks
    # Then asks a series of questions to display information the user is seeking
    # Uses a series of loops and if statements to verify user input and output data requested
    @staticmethod
    def execute_wgups():
        print("\nWelcome to the WGUPS Routing Program\n")
        total_mileage = sum(truck.current_miles for truck in [first_truck, second_truck, third_truck])
        print(f"The total mileage traveled by all trucks is: {total_mileage}\n")

        while True:
            user_input = input(
                "To search for a package(s) current status, type 'start', else type 'end' to close the program: \n"
            )
            print()

            if user_input.lower() == "start":
                while True:
                    user_input_format = "%H:%M:%S"
                    user_time = input(
                        "Enter the time of the package's status using the HH:MM:SS format: \n"
                    )
                    print()

                    try:
                        valid_time = datetime.datetime.strptime(user_time, user_input_format)
                    except ValueError:
                        print("Unexpected time input, please try again\n")
                        continue

                    hours, minutes, seconds = map(int, user_time.split(":"))
                    user_input_time = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

                    while True:
                        package_input = input(
                            "Enter the package ID you wish to find, or enter 'all' to return the status of all packages: \n"
                        )
                        print()

                        if package_input.isdigit() and 1 <= int(package_input) <= 40:
                            try:
                                package = package_hash_table.search(int(package_input))
                                package.update_status(user_input_time)
                                print(str(package))
                                print()
                                sys.exit()
                            except ValueError:
                                continue
                        elif package_input.lower() == "all":
                            try:
                                for packageID in range(1, 41):
                                    package = package_hash_table.search(packageID)
                                    package.update_status(user_input_time)
                                    print(str(package))
                                print()
                                sys.exit()
                            except ValueError:
                                continue
                        else:
                            print("Unexpected package ID, please try again\n")
                            continue
            elif user_input.lower() == "end":
                sys.exit("Goodbye")
            else:
                print("Unexpected input, please try again\n")
                continue


# Calls execute_wgups method
Main.execute_wgups()
