"""3304. Find the K-th Character in String Game I
Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
Difficulty: Easy
Description: Alice and Bob are playing a game. Initially, Alice has a string word = "a".
You are given a positive integer k.
Now Bob will ask Alice to perform the following operation forever:
Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
Note that the character 'z' can be changed to 'a' in the operation."""


class Solution:
    @staticmethod
    def kthCharacter(k: int) -> str:
        """Optimal Solution: Simulation. Time Complexity: O(k), Space Complexity: O(1)"""
        # Initialize the string with the first character 'a'
        word = 'a'

        # Perform the operation until the length of word is at least k
        while len(word) < k:
            # Initialize an empty string for the new characters
            next_word = ''
            # Generate the next character for each character in word
            for char in word:
                # Calculate the next character in the alphabet
                next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
                # Append the next character to the new string
                next_word += next_char
            # Append the new string to the original word
            word += next_word

        # Return the k-th character (1-indexed)
        return word[k - 1]


# Unit Test: k = 5, Output: 'b'
assert Solution.kthCharacter(5) == 'b'

# Unit Test: k = 10, Output: 'c'
assert Solution.kthCharacter(10) == 'c'

print("All unit tests are passed")
