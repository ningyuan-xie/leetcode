"""1470. Shuffle the Array
Link: https://leetcode.com/problems/shuffle-the-array/
Difficulty: Easy
Description: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn]."""

from typing import List


class Solution:
    @staticmethod
    def shuffle(nums: List[int], n: int) -> List[int]:
        """Optimal Solution: Iteration. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the shuffled array
        shuffled = []

        # Iterate through the first n elements of the nums array
        for i in range(n):
            # Append the ith element of the nums array to the shuffled array
            shuffled.append(nums[i])
            # Append the (n+i)th element of the nums array to the shuffled array
            shuffled.append(nums[n + i])

        # Return the shuffled array
        return shuffled


# Unit Test: nums = [2, 5, 1, 3, 4, 7], n = 3, Output: [2, 3, 5, 4, 1, 7]
assert Solution.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]

# Unit Test: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4, Output: [1, 4, 2, 3, 3, 2, 4, 1]
assert Solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]

# Unit Test: nums = [1, 1, 2, 2], n = 2, Output: [1, 2, 1, 2]
assert Solution.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]

print("All unit tests are passed")
