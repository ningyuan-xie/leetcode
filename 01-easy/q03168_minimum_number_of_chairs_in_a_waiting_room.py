"""3168. Minimum Number of Chairs in a Waiting Room
Link: https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room
Difficulty: Easy
Description: You are given a string s. Simulate events at each second i:
- If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
- If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available for every person
who enters the waiting room given that it is initially empty."""


class Solution:
    @staticmethod
    def minimumChairs(s: str) -> int:
        """Optimal Solution: Stack. Time Complexity: O(n), Space Complexity: O(n)."""
        # Initialize a stack to keep track of chairs
        stack = []
        minimum_num_of_chairs = 0

        # Iterate through the string
        for char in s:
            # If a person enters ('E'), add a chair to the stack
            if char == 'E':
                stack.append(1)
            # If a person leaves ('L'), remove a chair from the stack if available
            elif char == 'L' and stack:
                stack.pop()
            minimum_num_of_chairs = max(minimum_num_of_chairs, len(stack))
        # Return the total number of chairs used
        return minimum_num_of_chairs


# Unit Test: s = "EEEEEEE", Output = 7
assert Solution.minimumChairs("EEEEEEE") == 7

# Unit Test: s = "ELELEEL", Output = 2
assert Solution.minimumChairs("ELELEEL") == 2

# Unit Test: s = "ELEELEELLL", Output = 3
assert Solution.minimumChairs("ELEELEELLL") == 3

print("All unit tests are passed.")
