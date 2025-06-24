"""2293. Min-Max Game
Link: https://www.leetcode.com/problems/min-max-game/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums whose length is a power of 2.
Apply the following algorithm on nums:
1. Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer
array newNums of length n / 2.
2. For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i],
nums[2 * i + 1]).
3. For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i],
nums[2 * i + 1]).
4. Replace the array nums with newNums.
5. Repeat the entire process starting from step 1.
Return the last number that remains in nums after applying the algorithm."""

from typing import List


class Solution:
    @staticmethod
    def minMaxGame(nums: List[int]) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(n)."""
        # Iterate through the array
        while len(nums) > 1:
            new_nums = []
            for i in range(0, len(nums), 2):
                # Determine the pair index by dividing i by 2
                pair_index = i // 2
                if pair_index % 2 == 0:
                    # Take the minimum for even pair indices
                    new_nums.append(min(nums[i], nums[i + 1]))
                else:
                    # Take the maximum for odd pair indices
                    new_nums.append(max(nums[i], nums[i + 1]))
            nums = new_nums
        return nums[0]


# Input: nums = [1,3,5,2,4,8,2,2], Output: 1
assert Solution.minMaxGame([1, 3, 5, 2, 4, 8, 2, 2]) == 1

# Input: nums = [3], Output: 3
assert Solution.minMaxGame([3]) == 3

print("All unit tests are passed.")
