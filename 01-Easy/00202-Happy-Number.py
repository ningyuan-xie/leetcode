"""202. Happy Number
Link: https://leetcode.com/problems/happy-number/
Difficulty: Easy
Description: Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy."""


class Solution:
    @staticmethod
    def isHappy(n: int) -> bool:
        """Optimal Solution: Hash Set. Time Complexity: O(log(n)), Space Complexity: O(log(n))."""
        # Initialize a set to store UNIQUE sum of squares of digits
        seen = set()
        # Continue the process until the sum of squares of digits is 1
        while n != 1:
            if n in seen:  # If the sum of squares of digits is already in the set,
                return False  # an infinite loop is detected, unable to reach 1
            else:
                seen.add(n)
            # Calculate the sum of squares of digits
            sum_of_squares = 0
            while n > 0:
                # Extract the rightmost digit
                digit = n % 10  # 19 -> 9; 1 -> 1
                sum_of_squares += digit ** 2
                # Remove the rightmost digit
                n //= 10  # 19 -> 1; 1 -> 0
            # Update the given integer with the sum of squares of digits
            n = sum_of_squares  # 19 -> 82 -> 68 -> 100 -> 1
        return True


# Input: n = 19, Output: True
assert Solution.isHappy(19) is True

# Input: n = 2, Output: False
assert Solution.isHappy(2) is False

print("All unit tests are passed.")
