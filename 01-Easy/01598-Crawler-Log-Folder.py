"""1598. Crawler Log Folder
Link: https://leetcode.com/problems/crawler-log-folder/
Difficulty: Easy
Description: The Leetcode file system keeps a log each time some user performs a change folder
operation.
The operations are described below:
- "../" : Move to the parent folder of the current folder. (If you are already in the main folder,
remain in the same folder).
- "./" : Remain in the same folder.
- "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the
ith step.
The file system starts in the main folder, then the operations in logs are performed.
Return the minimum number of operations needed to go back to the main folder after the change folder
operations."""

from typing import List


class Solution:
    @staticmethod
    def minOperations(logs: List[str]) -> int:
        """Optimal Solution: Depth Tracking. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the depth of the current folder
        depth = 0

        # Iterate through each log in the list
        for log in logs:
            # If the log is '../', move up one level
            if log == '../':
                depth = max(0, depth - 1)
            # If the log is './', stay at the same level
            elif log == './':
                continue
            # If the log is a folder name, move down one level
            else:
                depth += 1

        return depth


# Unit Test: logs = ["d1/", "d2/", "../", "d21/", "./"], Output: 2
assert Solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]) == 2

# Unit Test: logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"], Output: 3
assert Solution.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3

# Unit Test: logs = ["d1/", "../", "../", "../"], Output: 0
assert Solution.minOperations(["d1/", "../", "../", "../"]) == 0

print("All unit tests are passed.")
