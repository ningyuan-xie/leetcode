"""2974. Minimum Number Game
Link: https://leetcode.com/problems/minimum-number-game/
Difficulty: Easy
Description: You are given a 0-indexed integer array nums of even length and there is also an
empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will
do one move. The rules of the game are as follows:
- Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
- Now, first Bob will append the removed element in the array arr, and then Alice does the same.
- The game continues until nums becomes empty.
Return the resulting array arr."""

from typing import List


class Solution:
    @staticmethod
    def numberGame(nums: List[int]) -> List[int]:
        """Optimal Solution: Simulation. Time Complexity: O(nlog(n)), Space Complexity: O(n)"""
        nums.sort()  # [5,4,2,3] -> [2,3,4,5]
        arr, alice, bob = [], [], []

        while nums:
            alice.append(nums.pop(0))
            bob.append(nums.pop(0))
            arr.append(bob.pop())
            arr.append(alice.pop())
        return arr


# Unit Test: nums = [5,4,2,3], Output: [3,2,5,4]
assert Solution.numberGame([5, 4, 2, 3]) == [3, 2, 5, 4]

# Unit Test: nums = [2,5], Output: [5,2]
assert Solution.numberGame([2, 5]) == [5, 2]

print("All unit tests are passed")
