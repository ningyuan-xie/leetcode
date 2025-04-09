"""2418. Sort the People
Link: http://leetcode.com/problems/sort-the-people/
Difficulty: Easy
Description: You are given an array of strings names, and an array heights that consists of distinct
positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights."""

from typing import List


class Solution:
    @staticmethod
    def sortPeople(names: List[str], heights: List[int]) -> List[str]:
        """Optimal Solution: Sorting. Time Complexity: O(nlog(n)), Space Complexity: O(n)"""
        # Sort the names in descending order by the people's heights
        names = [name for _, name in sorted(zip(heights, names), key=lambda x: x[0], reverse=True)]
        return names


# Unit Test: names = ["Mary","John","Emma"], heights = [180,165,170], Output: ["Mary","Emma","John"]
assert (Solution.sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
        == ["Mary", "Emma", "John"])

# Unit Test: names = ["Alice","Bob","Bob"], heights = [155,185,150], Output: ["Bob","Alice","Bob"]
assert (Solution.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150])
        == ["Bob", "Alice", "Bob"])
