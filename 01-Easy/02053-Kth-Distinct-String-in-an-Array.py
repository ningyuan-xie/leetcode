"""2053. Kth Distinct String in an Array
Link: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
Difficulty: Easy
Description: A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array."""

from typing import List


class Solution:
    @staticmethod
    def kthDistinct(arr: List[str], k: int) -> str:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a dictionary to store the frequency of each string
        freq = {}
        for s in arr:
            freq[s] = freq.get(s, 0) + 1  # {"d": 1, "b": 2, "c": 2, "a": 1}

        # Filter distinct strings in order
        distinct = [s for s in arr if freq[s] == 1]  # ["d", "a"]

        # Return the kth distinct string or an empty string if not enough
        return distinct[k - 1] if k <= len(distinct) else ""


# Input: arr = ["d","b","c","b","c","a"], k = 2, Output: "a"
assert Solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"

# Input: arr = ["aaa","aa","a"], k = 1, Output: "aaa"
assert Solution.kthDistinct(["aaa", "aa", "a"], 1) == "aaa"

# Input: arr = ["a","b","a"], k = 3, Output: ""
assert Solution.kthDistinct(["a", "b", "a"], 3) == ""

print("All unit tests are passed.")
