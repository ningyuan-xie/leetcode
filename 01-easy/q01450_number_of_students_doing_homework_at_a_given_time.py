"""1450. Number of Students Doing Homework at a Given Time
Link: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
Difficulty: Easy
Description: Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started doing their homework at the time startTime[i] and finished it at time
endTime[i].
Return the number of students doing their homework at time queryTime. More formally, return the
number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive."""

from typing import List


class Solution:
    @staticmethod
    def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the count of students doing homework at the query time
        count = 0

        # Iterate through the start and end times to find the students doing homework at the query time
        for (start, end) in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1

        return count


# Input: startTime = [1, 2, 3], endTime = [3, 2, 7], queryTime = 4, Output: 1
assert Solution.busyStudent([1, 2, 3], [3, 2, 7], 4) == 1

# Input: startTime = [4], endTime = [4], queryTime = 4, Output: 1
assert Solution.busyStudent([4], [4], 4) == 1

# Input: startTime = [4], endTime = [4], queryTime = 5, Output: 0
assert Solution.busyStudent([4], [4], 5) == 0

# Input: startTime = [1, 1, 1, 1], endTime = [1, 3, 2, 4], queryTime = 7, Output: 0
assert Solution.busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7) == 0

print("All unit tests are passed.")
