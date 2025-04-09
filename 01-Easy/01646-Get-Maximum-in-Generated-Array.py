"""1646. Get Maximum in Generated Array
Link: https://leetcode.com/problems/get-maximum-in-generated-array/
Difficulty: Easy
Description: You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated
in the following way:
- nums[0] = 0
- nums[1] = 1
- nums[2 * i] = nums[i] when 2 <= 2 * i <= n
- nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums."""


class Solution:
    @staticmethod
    def getMaximumGenerated(n: int) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(n)"""
        # Base case: n = 0
        if n == 0:
            return 0

        # Initialize the array
        nums = [0] * (n + 1)
        nums[1] = 1

        # Generate the array
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

        return max(nums)


# Unit Test: Input: n = 7, Output: 3
assert Solution.getMaximumGenerated(7) == 3

# Unit Test: Input: n = 2, Output: 1
assert Solution.getMaximumGenerated(2) == 1

# Unit Test: Input: n = 3, Output: 2
assert Solution.getMaximumGenerated(3) == 2

print("All unit tests are passed")
