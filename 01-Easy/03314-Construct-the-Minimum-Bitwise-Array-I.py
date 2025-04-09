"""3314. Construct the Minimum Bitwise Array I
Link: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
Difficulty: Easy
Description: You are given an array nums consisting of n prime integers.
You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
Additionally, you must minimize each value of ans[i] in the resulting array.
If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1."""

from typing import List


class Solution:
    @staticmethod
    def minBitwiseArray(nums: List[int]) -> List[int]:
        """Optimal Solution: Bitwise Manipulation. 
           Time Complexity: O(n * m), where m is the max num, Space Complexity: O(n).
           Bitwise XOR operator ^ : 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0.
           Bitwise OR operator | : 1 | 1 = 1, 1 | 0 = 1, 0 | 0 = 0."""
        # Initialize the result array
        ans = []

        # For each number in the input array, find the min bitwise value
        for num in nums:
            # Initialize the minimum value to -1
            min_val = -1

            # Bitwise OR (|) only turns bits on, i | (i + 1) >= i
            for i in range(num + 1):
                # Check if the bitwise OR condition is satisfied
                if (i | (i + 1)) == num:
                    # Update the minimum value
                    min_val = i
                    break

            # Append the minimum value to the result array
            ans.append(min_val)
        return ans


def unit_tests():
    # Input: nums = [2,3,5,7], Output: [-1,1,4,3]
    assert Solution.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3]

    # Input: nums = [11,13,31], Output: [9,12,15]
    assert Solution.minBitwiseArray([11, 13, 31]) == [9, 12, 15]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
