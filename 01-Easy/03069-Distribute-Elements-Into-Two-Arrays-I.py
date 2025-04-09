"""3069. Distribute Elements Into Two Arrays I
Link: https://leetcode.com/problems/distribute-elements-into-two-arrays/
Difficulty: Easy
Description: You are given a 1-indexed array of distinct integers nums of length n.
You need to distribute all the elements of nums between two arrays arr1 and arr2 using n
operations. In the first operation, append nums[1] to arr1. In the second operation, append
nums[2] to arr2. Afterwards, in the ith operation:
- If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1.
Otherwise, append nums[i] to arr2.
The array result is formed by concatenating the arrays arr1 and arr2. For example, if
arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].
Return the array result."""

from typing import List


class Solution:
    @staticmethod
    def resultArray(nums: List[int]) -> List[int]:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the two arrays
        array1, array2 = [], []
        array1.append(nums[0])
        array2.append(nums[1])

        # Distribute the elements into two arrays
        for i in range(2, len(nums)):
            if array1[-1] > array2[-1]:
                array1.append(nums[i])
            else:
                array2.append(nums[i])

        # Concatenate the two arrays
        return array1 + array2


# Unit Test: nums = [2,1,3], Output = [2,3,1]
assert Solution.resultArray([2, 1, 3]) == [2, 3, 1]

# Unit Test: nums = [5,4,3,8], Output = [5,3,4,8]
assert Solution.resultArray([5, 4, 3, 8]) == [5, 3, 4, 8]

print("All unit tests are passed")
