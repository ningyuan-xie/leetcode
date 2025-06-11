"""917. Reverse Only Letters
Link: https://leetcode.com/problems/reverse-only-letters/
Difficulty: Easy
Description: Given a string s, reverse the string according to the following rules:
• All the characters that are not English letters remain in the same position.
• All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it."""


class Solution:
    @staticmethod
    def reverseOnlyLetters(s: str) -> str:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n).
        Similar to 345. Reverse Vowels of a String."""
        # Convert the string to a list for easy manipulation
        s = list(s)
        left, right = 0, len(s) - 1

        # Swap the characters at the left and right pointers until they meet
        while left < right:
            # If the left character is not an English letter, move the left pointer to the right
            if not s[left].isalpha():
                left += 1
            # If the right character is not an English letter, move the right pointer to the left
            elif not s[right].isalpha():
                right -= 1
            # If both characters are English letters, swap them
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)


def unit_tests():
    # Input: s = "ab-cd", Output: "dc-ba"
    assert Solution.reverseOnlyLetters("ab-cd") == "dc-ba"

    # Input: s = "a-bC-dEf-ghIj", Output: "j-Ih-gfE-dCba"
    assert Solution.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"

    # Input: s = "Test1ng-Leet=code-Q!", Output: "Qedo1ct-eeLg=ntse-T!"
    assert Solution.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
