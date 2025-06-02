"""830. Positions of Large Groups
Link: https://leetcode.com/problems/positions-of-large-groups/
Difficulty: Easy
Description: In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index."""

from typing import List


class Solution:
    @staticmethod
    def largeGroupPositions(s: str) -> List[List[int]]:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)."""
        result = []
        n = len(s)
        start = 0  # Start of current group
        
        while start < n:
            # Initialize the end pointer to the start pointer
            end = start
            # Expand the end pointer to the end of the current group
            while end < n and s[end] == s[start]:
                end += 1
            # Check if group is large
            if end - start >= 3:
                result.append([start, end - 1])
            start = end  # Move to next group
            
        return result


def unit_tests():
    # Input: s = "abbxxxxzyy", Output: [[3, 6]]
    assert Solution.largeGroupPositions("abbxxxxzyy") == [[3, 6]]

    # Input: s = "abc", Output: []
    assert Solution.largeGroupPositions("abc") == []

    # Input: s = "abcdddeeeeaabbbcd", Output: [[3, 5], [6, 9], [12, 14]]
    assert Solution.largeGroupPositions("abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]]


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")
