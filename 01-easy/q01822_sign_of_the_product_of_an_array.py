"""1822. Sign of the Product of an Array
Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/
Difficulty: Easy
Description: Implement a function signFunc(x) that returns:
- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product)."""

from typing import List


class Solution:
    @staticmethod
    def arraySign(nums: List[int]) -> int:
        """Optimal Solution: Count Negatives. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the product of the array
        product = 1

        # Traverse the array and calculate the product
        for num in nums:
            product *= num

        # Return the sign of the product
        return 1 if product > 0 else -1 if product < 0 else 0


# Unit Test: nums = [-1, -2, -3, -4], Output: 1
assert Solution.arraySign([-1, -2, -3, -4]) == 1

# Unit Test: nums = [1, 2, 3, -4], Output: -1
assert Solution.arraySign([1, 2, 3, -4]) == -1

# Unit Test: nums = [-1, 1, -1, 1, -1], Output: -1
assert Solution.arraySign([-1, 1, -1, 1, -1]) == -1

print("All unit tests are passed.")
