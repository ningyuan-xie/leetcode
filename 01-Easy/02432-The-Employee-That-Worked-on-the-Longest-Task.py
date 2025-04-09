"""2432. The Employee That Worked on the Longest Task
Link: https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
Difficulty: Easy
Description: There are n employees, each with a unique id from 0 to n - 1.
You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:
- idi is the id of the employee that worked on the ith task, and
- leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei
are unique.
Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts
at time 0.
Return the id of the employee that worked the task with the longest time. If there is a tie between
two or more employees, return the smallest id among them."""

from typing import List


class Solution:
    @staticmethod
    def hardestWorker(logs: List[List[int]]) -> int:
        """Optimal Solution: One Pass. Time Complexity: O(n), Space Complexity: O(n)."""
        max_duration, employee_id, prev_end_time = 0, 0, 0

        # Find the employee with the longest task duration
        for (emp_id, end_time) in logs:  # E.g. [0, 3], [2, 5], [0, 9], [1, 15]
            duration = end_time - prev_end_time

            if duration > max_duration or (duration == max_duration and emp_id < employee_id):
                max_duration = duration
                employee_id = emp_id

            prev_end_time = end_time

        return employee_id


# Unit Test: n = 10, logs = [[0,3],[2,5],[0,9],[1,15]], Output: 1
assert Solution.hardestWorker([[0, 3], [2, 5], [0, 9], [1, 15]]) == 1

# Unit Test: n = 26, logs = [[1,1],[3,7],[2,12],[7,17]], Output: 3
assert Solution.hardestWorker([[1, 1], [3, 7], [2, 12], [7, 17]]) == 3

# Unit Test: n = 2, logs = [[0,10],[1,20]], Output: 0
assert Solution.hardestWorker([[0, 10], [1, 20]]) == 0

print("All unit tests are passed.")
