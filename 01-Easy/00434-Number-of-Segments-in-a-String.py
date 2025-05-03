"""434. Number of Segments in a String
Link: https://leetcode.com/problems/number-of-segments-in-a-string/
Difficulty: Easy
Description: Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters."""


class Solution:
    @staticmethod
    def countSegments(s: str) -> int:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(1)."""
        return len(s.split()) if s else 0


def unit_tests():
    # Input: s = "Hello, my name is John", Output: 5
    assert Solution.countSegments("Hello, my name is John") == 5

    # Input: s = "Hello", Output: 1
    assert Solution.countSegments("Hello") == 1

    # Input: s = "love live! mu'sic forever", Output: 4
    assert Solution.countSegments("love live! mu'sic forever") == 4


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
