"""1603. Design Parking System
Link: https://leetcode.com/problems/design-parking-system/
Difficulty: Easy
Description: Design a parking system for a parking lot. The parking lot has three kinds of parking
spaces: big, medium, and small, with a fixed number of slots for each size.
Implement the ParkingSystem class:
- ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
The number of slots for each parking space are given as part of the constructor.
- bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants
to get into the parking lot. carType can be of three kinds: big, medium, or small, which are
represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType.
If there is no space available, return false, else park the car in that size space and return true."""


class ParkingSystem:
    """Optimal Solution: Object-Oriented Design. Time Complexity: O(1), Space Complexity: O(1)"""

    def __init__(self, big: int, medium: int, small: int):
        """Constructor: Initialize the parking system with the number of parking spaces
           for each type"""
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        """Add a car of the specified type to the parking lot"""
        # Check if there is an available parking space for the car type
        if self.spaces[carType - 1] > 0:
            self.spaces[carType - 1] -= 1
            return True
        else:
            return False


# Input: ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# Output: [null, true, true, false, false]
parking_system = ParkingSystem(1, 1, 0)
assert parking_system.addCar(1) is True
assert parking_system.addCar(2) is True
assert parking_system.addCar(3) is False
assert parking_system.addCar(1) is False

print("All unit tests are passed.")
