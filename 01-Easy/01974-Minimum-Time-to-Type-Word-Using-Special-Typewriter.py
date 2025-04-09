"""1974. Minimum Time to Type Word Using Special Typewriter
Link: https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
Difficulty: Easy
Description: There is a special typewriter with lowercase English letters 'a' to 'z' arranged in
a circle with a pointer. A character can only be typed if the pointer is pointing to that character.
The pointer is initially pointing to the character 'a'.
Each second, you may perform one of the following operations:
- Move the pointer one character counterclockwise or clockwise.
- Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word."""


class Solution:
    @staticmethod
    def minTimeToType(word: str) -> int:
        """Optimal Solution: Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1)"""
        # Start at 'a'
        current_pos = 'a'
        total_time = 0

        # Greedy approach: calculate the distance between the current and the next char on the fly
        for char in word:
            # Calculate clockwise and counterclockwise distances
            clockwise_distance = abs(ord(char) - ord(current_pos))
            counterclockwise_distance = 26 - clockwise_distance

            # Add the minimum distance and 1 second for typing the character
            total_time += min(clockwise_distance, counterclockwise_distance) + 1

            # Move to the new character
            current_pos = char

        return total_time


# Unit Test: word = "abc", Output: 5
assert Solution.minTimeToType("abc") == 5

# Unit Test: word = "bza", Output: 7
assert Solution.minTimeToType("bza") == 7

# Unit Test: word = "z", Output: 2
assert Solution.minTimeToType("z") == 2

print("All unit tests are passed.")
