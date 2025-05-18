"""3386. Button with Longest Push Time
Link: https://leetcode.com/problems/button-with-longest-push-time/
Difficulty: Easy
Description: You are given a 2D array events which represents a sequence of events where a child pushes a series of buttons on a keyboard.
Each events[i] = [indexi, timei] indicates that the button at index indexi was pressed at time timei.
• The array is sorted in increasing order of time.
• The time taken to press a button is the difference in time between consecutive button presses. The time for the first button is simply the time at which it was pressed.
Return the index of the button that took the longest time to push. If multiple buttons have the same longest time, return the button with the smallest index."""

from typing import List


class Solution:
    @staticmethod
    def buttonWithLongestTime(events: List[List[int]]) -> int:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        max_time = 0
        max_index = -1

        # Iterate through the events to find the maximum time taken for each button
        for i in range(len(events)):
            # For the first button, time is simply the time at which it was pressed
            if i == 0:
                time = events[i][1]
            # For subsequent buttons, time is the difference between consecutive button presses
            else:
                time = events[i][1] - events[i - 1][1]

            if time > max_time:
                max_time = time
                max_index = events[i][0]
            elif time == max_time:
                max_index = min(max_index, events[i][0])

        return max_index


def unit_tests():
    # Input: events = [[1,2],[2,5],[3,9],[1,15]], Output: 1
    assert Solution.buttonWithLongestTime([[1, 2], [2, 5], [3, 9], [1, 15]]) == 1

    # Input: events = [[10,5],[1,7]], Output: 10
    assert Solution.buttonWithLongestTime([[10, 5], [1, 7]]) == 10


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
