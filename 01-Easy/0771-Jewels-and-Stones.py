"""771. Jewels and Stones
Link: https://leetcode.com/problems/jewels-and-stones/
Difficulty: Easy
Description: You're given strings jewels representing the types of stones that are jewels, and stones
representing the stones you have. Each character in stones is a type of stone you have. You want to
know how many of the stones you have are also jewels.
Letters are case-sensitive, so "a" is considered a different type of stone from "A"."""


class Solution:
    @staticmethod
    def num_jewels_in_stones(jewels: str, stones: str) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0762-Prime-Number-of-Set-Bits-in-Binary-Representation.py"""
        # Initialize the count of jewels in stones
        count = 0

        # Create a set of jewels for faster lookup
        jewels_set = set(jewels)

        # Count the number of jewels in stones
        for stone in stones:
            if stone in jewels_set:
                count += 1

        return count


# Unit Test: Input: jewels = "aA", stones = "aAAbbbb", Output: 3
assert Solution.num_jewels_in_stones("aA", "aAAbbbb") == 3

# Unit Test: Input: jewels = "z", stones = "ZZ", Output: 0
assert Solution.num_jewels_in_stones("z", "ZZ") == 0

print("All unit tests are passed")
