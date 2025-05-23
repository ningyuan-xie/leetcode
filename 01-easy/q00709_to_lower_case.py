"""709. To Lower Case
Link: https://leetcode.com/problems/to-lower-case/
Difficulty: Easy
Description: Given a string s, return the string after replacing every uppercase letter with the same lowercase letter."""


class Solution:
    @staticmethod
    def to_lower_case(s: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)."""
        result = []
        for char in s:
            if 'A' <= char <= 'Z':
                # Convert uppercase to lowercase by adding 32 to the ASCII value
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)


def unit_tests():
    # Input: "Hello", Output: "hello"
    assert Solution.to_lower_case("Hello") == "hello"

    # Input: "here", Output: "here"
    assert Solution.to_lower_case("here") == "here"

    # Input: "LOVELY", Output: "lovely"
    assert Solution.to_lower_case("LOVELY") == "lovely"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
