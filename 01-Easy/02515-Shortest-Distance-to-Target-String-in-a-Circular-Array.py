"""2515. Shortest Distance to Target String in a Circular Array
Link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
Difficulty: Easy
Description: You are given a 0-indexed circular string array words and a string target. A circular
array means that the array's end connects to the array's beginning.
- Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i]
is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.
Return the shortest distance needed to reach the string target. If the string target does not exist in
words, return -1."""

from typing import List


class Solution:
    @staticmethod
    def closetTarget(words: List[str], target: str, startIndex: int) -> int:
        """Optimal Solution: Circular Distance. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(words)
        min_distance = float('inf')  # Initialize to a very large number

        for i in range(n):
            if words[i] == target:
                # Compute circular distance
                distance = min(abs(i - startIndex), n - abs(i - startIndex))
                min_distance = min(min_distance, distance)

                # Early stopping: if we find distance = 0, it's the minimum
                if min_distance == 0:
                    return 0

        # If the target is not found, return -1
        return min_distance if min_distance != float('inf') else -1


# Unit Test: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1, Output: 1
assert (Solution.closetTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1)
        == 1)

# Unit Test: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0, Output: 1
assert Solution.closetTarget(["a", "b", "leetcode"], "leetcode", 0) == 1

# Unit Test: words = ["i","eat","leetcode"], target = "ate", startIndex = 0, Output: -1
assert Solution.closetTarget(["i", "eat", "leetcode"], "ate", 0) == -1

print("All unit tests are passed.")
