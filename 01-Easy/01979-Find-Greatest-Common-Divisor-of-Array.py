"""1979. Find Greatest Common Divisor of Array
Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
Difficulty: Easy
Description: Given an integer array nums, return the greatest common divisor of the smallest number
and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides
both numbers."""


from typing import List


class Solution:
    @staticmethod
    def findGCD(nums: List[int]) -> int:
        """Optimal Solution: Euclidean Algorithm. Time Complexity: O(log(n)), Space Complexity: O(1).
           Similar to 1071-Greatest-Common-Divisor-of-Strings.py"""

        def gcd(a: int, b: int) -> int:
            """Euclidean Algorithm: Recursively find the GCD of two numbers.
               For any two int a and b, the GCD of a and b is the same as the GCD of b and a % b.
               If a number d divides both a and b, then d also divides a % b."""
            while b:
                a, b = b, a % b
            return a

        # Find the minimum and maximum numbers in the array
        min_num, max_num = min(nums), max(nums)

        # Return the greatest common divisor of the minimum and maximum numbers
        return gcd(min_num, max_num)


# Unit Test: nums = [2, 5, 6, 9, 10], Output: 2
assert Solution.findGCD([2, 5, 6, 9, 10]) == 2

# Unit Test: nums = [7, 5, 6, 8, 3], Output: 1
assert Solution.findGCD([7, 5, 6, 8, 3]) == 1

# Unit Test: nums = [3, 3], Output: 3
assert Solution.findGCD([3, 3]) == 3

print("All unit tests are passed.")
