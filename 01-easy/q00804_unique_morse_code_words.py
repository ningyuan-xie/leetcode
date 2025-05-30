"""804. Unique Morse Code Words
Link: https://leetcode.com/problems/unique-morse-code-words/
Difficulty: Easy
Description: International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
• 'a' maps to ".-",
• 'b' maps to "-...",
• 'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
• For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have."""

from typing import List


class Solution:
    @staticmethod
    def uniqueMorseRepresentations(words: List[str]) -> int:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # Use a set to store unique Morse code transformations
        seen = set()
        for word in words:
            code = []
            for c in word:
                code.append(morse_codes[ord(c) - ord('a')])
            seen.add(''.join(code))
            
        return len(seen)


def unit_tests():
    # Input: words = ["gin", "zen", "gig", "msg"], Output: 2
    assert Solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2

    # Input: words = ["a"], Output: 1
    assert Solution.uniqueMorseRepresentations(["a"]) == 1

    # Input: words = ["b"], Output: 1
    assert Solution.uniqueMorseRepresentations(["b"]) == 1

    # Input: words = ["a", "b"], Output: 2
    assert Solution.uniqueMorseRepresentations(["a", "b"]) == 2


if __name__ == '__main__':
    unit_tests()
    print("All unit tests are passed.")
