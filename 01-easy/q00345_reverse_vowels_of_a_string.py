"""345. Reverse Vowels of a String
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
Difficulty: Easy
Description: Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once."""


class Solution:
    @staticmethod
    def reverseVowels(s: str) -> str:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 344. Reverse String."""
        left, right = 0, len(s) - 1
        s_list = list(s)
        vowels = set("aeiouAEIOU")

        # Loop until left pointer >= right pointer
        while left < right:
            # Move the left pointer to the next vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move the right pointer to the previous vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap the vowels at the left and right pointers
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)


def unit_tests():
    # Input: s = "hello", Output: "holle"
    assert Solution.reverseVowels("hello") == "holle"

    # Input: s = "leetcode", Output: "leotcede"
    assert Solution.reverseVowels("leetcode") == "leotcede"

    # Input: s = "aA", Output: "Aa"
    assert Solution.reverseVowels("aA") == "Aa"

    # Input: s = "IceCreAm", Output: "AceCreIm"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
