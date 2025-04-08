"""3300. Find the Original Typed String I
Link: https://leetcode.com/problems/find-the-original-typed-string-i/
Difficulty: Easy
Description: Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.
You are given a string word, which represents the final output displayed on Alice's screen.
Return the total number of possible original strings that Alice might have intended to type."""


class Solution:
    @staticmethod
    def possibleStringCount(word: str) -> int:
        """Optimal Solution: Count Consecutive Char. Time Complexity: O(n), Space Complexity: O(1)."""
        count = 0
        result = 1

        for i in range(1, len(word)):
            # If the current character is the same as the previous one
            if word[i] == word[i - 1]:
                count += 1
            # If the current character is different from the previous one
            else:
                result += count
                count = 0
        
        # Add the last count
        result += count
        return result


def unit_tests():
    # Unit Test: word = "abbcccc", Output: 5
    assert Solution.possibleStringCount("abbcccc") == 5

    # Unit Test: word = "abcd", Output: 1
    assert Solution.possibleStringCount("abcd") == 1

    # Unit Test: word = "aaaa", Output: 4
    assert Solution.possibleStringCount("aaaa") == 4

    # Unit Test: word = "ere", Output: 1
    assert Solution.possibleStringCount("ere") == 1


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed")
