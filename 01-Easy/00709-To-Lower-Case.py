"""709. To Lower Case
Link: https://leetcode.com/problems/to-lower-case/
Difficulty: Easy
Description: Implement function ToLowerCase() that has a string parameter str, and returns the
same string in lowercase."""


class Solution:
    @staticmethod
    def to_lower_case(s: str) -> str:
        """Optimal Solution: Convert to Lowercase. Time Complexity: O(n), Space Complexity: O(n)"""
        return s.lower()


# Input: "Hello", Output: "hello"
assert Solution.to_lower_case("Hello") == "hello"

# Input: "here", Output: "here"
assert Solution.to_lower_case("here") == "here"

# Input: "LOVELY", Output: "lovely"
assert Solution.to_lower_case("LOVELY") == "lovely"

print("All unit tests are passed.")
