"""2899. Last Visited Integers
Link: https://leetcode.com/problems/last-visited-integers/
Difficulty: Easy
Description: Given an integer array nums where nums[i] is either a positive integer or -1. We
need to find for each -1 the respective positive integer, which we call the last visited integer.
To achieve this goal, let's define two empty arrays: seen and ans.
Start iterating from the beginning of the array nums.
- If a positive integer is encountered, prepend it to the front of seen.
- If -1 is encountered, let k be the number of consecutive -1s seen so far (including the current -1),
-- If k is less than or equal to the length of seen, append the k-th element of seen to ans.
-- If k is strictly greater than the length of seen, append -1 to ans.
Return the array ans."""

from typing import List


class Solution:
    @staticmethod
    def lastVisitedIntegers(nums: List[int]) -> List[int]:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(n)"""
        seen, ans = [], []

        k = 0
        for num in nums:
            if num > 0:
                k = 0
                seen.insert(0, num)
            elif num == -1:
                # Count the number of consecutive -1s seen so far
                k += 1

                if k <= len(seen):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
        return ans


# Unit Test: nums = [1,2,-1,-1,-1], Output: [2,1,-1]
assert Solution.lastVisitedIntegers([1, 2, -1, -1, -1]) == [2, 1, -1]

# Unit Test: nums = [1,-1,2,-1,-1], Output: [1,2,1]
assert Solution.lastVisitedIntegers([1, -1, 2, -1, -1]) == [1, 2, 1]

print("All unit tests are passed")
