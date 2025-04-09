"""1629. Slowest Key
Link: https://leetcode.com/problems/slowest-key/
Difficulty: Easy
Description: A newly designed keypad was tested, where a tester pressed a sequence of n keys,
one at a time.
You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in
the testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the ith
key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and every
subsequent key was pressed at the exact time the previous key was released.
The tester wants to know the key of the keypress that had the longest duration. The ith keypress
had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of
releaseTimes[0].
Note that the same key could have been pressed multiple times during the test, and these multiple
presses of the same key may not have had the same duration.
Return the key of the keypress that had the longest duration. If there are multiple such keypresses,
return the lexicographically largest key of the keypresses."""

from typing import List


class Solution:
    @staticmethod
    def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the slowest key and the longest duration
        slowest_key, longest_duration = keysPressed[0], releaseTimes[0]

        # Iterate through the remaining keys and release times
        for i in range(1, len(keysPressed)):
            # Calculate the duration of the current key
            duration = releaseTimes[i] - releaseTimes[i - 1]

            # Update the slowest key and the longest duration
            if (duration > longest_duration
                    or (duration == longest_duration and keysPressed[i] > slowest_key)):
                slowest_key, longest_duration = keysPressed[i], duration

        return slowest_key


# Unit Test: releaseTimes = [9, 29, 49, 50], keys = "cbcd", Output: "c"
assert Solution.slowestKey([9, 29, 49, 50], "cbcd") == "c"

# Unit Test: releaseTimes = [12, 23, 36, 46, 62], keys = "spuda", Output: "a"
assert Solution.slowestKey([12, 23, 36, 46, 62], "spuda") == "a"

print("All unit tests are passed.")
