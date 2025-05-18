"""1518. Water Bottles
Link: https://leetcode.com/problems/water-bottles/
Difficulty: Easy
Description: There are numBottles water bottles that are initially full of water. You can exchange
numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water bottles you
can drink."""


class Solution:
    @staticmethod
    def numWaterBottles(numBottles: int, numExchange: int) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(log(n)), Space Complexity: O(1)."""
        # Initialize the total number of water bottles drunk
        total = numBottles

        # While we can exchange empty bottles for new full ones
        while numBottles >= numExchange:
            # Calculate how many new bottles we can get by exchanging
            new_bottles, remainder = divmod(numBottles, numExchange)
            # Add the new bottles to the total
            total += new_bottles
            # Update the number of bottles to the new full ones plus the remainder
            numBottles = new_bottles + remainder

        return total


# Unit Test: numBottles = 9, numExchange = 3, Output: 13
assert Solution.numWaterBottles(9, 3) == 13

# Unit Test: numBottles = 15, numExchange = 4, Output: 19
assert Solution.numWaterBottles(15, 4) == 19

# Unit Test: numBottles = 5, numExchange = 5, Output: 6
assert Solution.numWaterBottles(5, 5) == 6

# Unit Test: numBottles = 2, numExchange = 3, Output: 2
assert Solution.numWaterBottles(2, 3) == 2

print("All unit tests are passed.")
