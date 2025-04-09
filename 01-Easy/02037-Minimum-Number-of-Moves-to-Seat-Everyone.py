"""2037. Minimum Number of Moves to Seat Everyone
Link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone
Difficulty: Easy
Description: There are n availabe seats and n students standing in a room. You are given an array
seats of length n, where seats[i] is the position of the ith seat. You are also given the array
students of length n, where students[j] is the position of the jth student.
You may perform the following move any number of times:
- Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from
position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students
are in the same seat.
Note that there may be multiple seats or students in the same position at the beginning."""

from typing import List


class Solution:
    @staticmethod
    def minMovesToSeat(seats: List[int], students: List[int]) -> int:
        """Optimal Solution: Sort and Calculate. Time Complexity: O(nlog(n)), Space Complexity: O(1)."""
        # Sort the seats and students
        seats.sort()  # E.g. seats = [3, 1, 5] -> seats = [1, 3, 5]
        students.sort()  # E.g. students = [2, 7, 4] -> students = [2, 4, 7]

        # Initialize the number of moves required to seat everyone
        moves = 0

        # Calculate the number of moves required to seat each student
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])

        return moves


# Unit Test: seats = [3, 1, 5], students = [2, 7, 4], Output: 4
assert Solution.minMovesToSeat([3, 1, 5], [2, 7, 4]) == 4

# Unit Test: seats = [4, 1, 5, 9], students = [1, 3, 2, 6], Output: 7
assert Solution.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]) == 7

# Unit Test: seats = [2, 2, 6, 6], students = [1, 3, 2, 6], Output: 4
assert Solution.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]) == 4

print("All unit tests are passed.")
