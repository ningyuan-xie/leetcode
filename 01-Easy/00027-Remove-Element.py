"""27. Remove Element
Link: https://leetcode.com/problems/remove-element/
Difficulty: Easy
Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
• Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
• Return k."""

from typing import List


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 26. Remove Duplicates from Sorted Array."""
        # Initialize the new length index to 0
        length_new = 0
        # Loop through the list
        for i in range(len(nums)):
            # If the current number != val, keep it at the new length index
            if nums[i] != val:
                # Replace the new length number in-place with the current number
                nums[length_new] = nums[i]
                # Increase the new length index
                length_new += 1
        # Return the length of the list, minimal length is 0
        return length_new


def unit_tests():
    # Input: nums = [3,2,2,3], val = 3, Output: 2; nums = [2,2,_,_]
    assert Solution.removeElement([3, 2, 2, 3], 3) == 2

    # Input: nums = [0,1,2,2,3,0,4,2], val = 2, Output: 5; nums = [0,1,3,0,4,_]
    assert Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5

    # Input: nums = [1], val = 1, Output: 0; nums = []
    assert Solution.removeElement([1], 1) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
