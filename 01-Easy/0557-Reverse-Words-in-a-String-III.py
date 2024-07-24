# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Difficulty: Easy
# Description: Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

class Solution:
    # Optimal Solution: Split, Reverse, and Join. Time Complexity: O(n), Space Complexity: O(n)
    @staticmethod
    def reverseWords(s: str) -> str:
        # Split the string into words
        words = s.split()
        # Reverse each word in the list
        reversed_words = [word[::-1] for word in words]
        # Join the reversed words into a single string separated by space
        return ' '.join(reversed_words)

    # Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(n)
    # Similar to 0344-Reverse-String.py and 0541-Reverse-String-II.py
    @staticmethod
    def reverseWordsTwoPointers(s: str) -> str:
        # Convert the string into a list of characters
        s = list(s)
        # Initialize the left and right pointers
        left, right = 0, 0
        # Iterate through the characters in the string
        while right < len(s):
            # Move the right pointer if the current char is a word
            if s[right] != ' ':
                right += 1
            # If the current char is a space, reverse the char excluding the space
            else:
                s[left:right] = reversed(s[left:right])  # skip the space
                # Move the left and right pointers to the next word
                left, right = right + 1, left  # left skips the space here
        # When the loop ends, there is still one word left to reverse
        # because there is no space at the end
        s[left:right] = reversed(s[left:right])
        # Convert the list of characters back into a string without spaces
        # because the spaces were untouched during the iteration
        return ''.join(s)


# Unit Test: Input: s = "Let's take LeetCode contest", Output: "s'teL ekat edoCteeL tsetnoc"
assert Solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"

# Unit Test: Input: s = "God Ding", Output: "doG gniD"
assert Solution.reverseWordsTwoPointers("God Ding") == "doG gniD"

print("All unit tests are passed")
