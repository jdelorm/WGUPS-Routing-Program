WGUPS Routing Program

The WGUPS Routing Program is a Python-based simulation that calculates optimal delivery routes for a fleet of trucks in a package delivery system. 
The program addresses the Traveling Salesman Problem (TSP) by employing a greedy algorithm to determine the most efficient route for each truck, minimizing the total distance traveled during deliveries.

The program reads data from CSV files containing package details, distances between addresses, and addresses themselves. It then computes delivery routes for each truck, ensuring packages are delivered on time and tracking the total distance traveled by each truck.

Greedy Routing Algorithm: Optimizes truck routes based on a minimal travel distance approach.

Package Tracking: Tracks the status of packages and provides delivery status at any given time.

Multiple Trucks: Simulates the use of three trucks, each handling different sets of packages.

Interactive User Interface: Allows users to input a time and query the status of a specific package or all packages.


Python 3.x

Custom Classes:

Truck – Handles truck attributes and methods.

Package – Represents a package and its delivery status.

HashTable – Provides efficient storage and retrieval of packages.

CSV Files: Used for storing package and address data.

Datetime: For managing delivery times and statuses.
