"""2582. Pass the Pillow
Link: https://leetcode.com/problems/pass-the-pillow/
Difficulty: Easy
Description: There are n people standing in a line labeled from 1 to n. The first person in the line
is holding a pillow initially. Every second, the person holding the pillow passes it to the next
person standing in the line. Once the pillow reaches the end of the line, the direction changes,
and people continue passing the pillow in the opposite direction.
- For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the
n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after
time seconds."""


class Solution:
    @staticmethod
    def passThePillow(n: int, time: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)"""
        # Calculate the number of complete rounds
        rounds = time // (n - 1)  # 5 // 3 = 1

        # Calculate the remaining time after complete rounds
        remaining_time = time % (n - 1)  # 5 % 3 = 2

        # Determine the final player based on the number of complete rounds and remaining time:
        # If rounds is even, the pillow is passed in the same direction as the start
        if rounds % 2 == 0:
            return remaining_time + 1
        # If rounds is odd, the pillow is passed in the opposite direction
        else:
            return n - remaining_time


# Unit Test: n = 4, time = 5, Output: 2
assert Solution.passThePillow(4, 5) == 2

# Unit Test: n = 3, time = 2, Output: 3
assert Solution.passThePillow(3, 2) == 3

print("All unit tests are passed.")
