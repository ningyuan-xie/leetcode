"""557. Reverse Words in a String III
Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
Difficulty: Easy
Description: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order."""


class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)."""
        # Split the string into words
        words = s.split()
        # Reverse each word in the list
        reversed_words = [word[::-1] for word in words]
        # Join the reversed words into a single string separated by space
        return ' '.join(reversed_words)


def unit_tests():
    # Input: s = "Let's take LeetCode contest", Output: "s'teL ekat edoCteeL tsetnoc"
    assert Solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"

    # Input: s = "God Ding", Output: "doG gniD"
    assert Solution.reverseWords("God Ding") == "doG gniD"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
