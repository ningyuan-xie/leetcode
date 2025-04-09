"""2739. Total Distance Traveled
Link: https://leetcode.com/problems/total-distance-traveled/
Difficulty: Easy
Description: A truck has two fuel tanks. You are given two integers, mainTank representing the fuel
present in the main tank in liters and additionalTank representing the fuel present in the additional
tank in liters.
The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank,
if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the
additional tank to the main tank.
Return the maximum distance which can be traveled.
Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for
every 5 liters consumed."""


class Solution:
    @staticmethod
    def distanceTraveled(mainTank: int, additionalTank: int) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the distance and the fuel in the main tank
        distance = 0

        while mainTank >= 5:
            # Consume 5 liters, moving 50 km
            mainTank -= 5
            distance += 50

            # Transfer 1 liter if available
            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        # Use remaining fuel
        distance += mainTank * 10

        return distance


# Unit Test: mainTank = 5, additionalTank = 10, Output: 60
assert Solution.distanceTraveled(5, 10) == 60

# Unit Test: mainTank = 1, additionalTank = 2, Output: 10
assert Solution.distanceTraveled(1, 2) == 10

# Unit Test: mainTank = 7, additionalTank = 1, Output: 80
assert Solution.distanceTraveled(7, 1) == 80

print("All unit tests are passed.")
