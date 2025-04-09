"""2073. Time Needed to Buy Tickets
Link: https://leetcode.com/problems/Time-Needed-to-Buy-Tickets
Difficulty: Easy
Description: There are n people in a line queuing to buy tickets, where the 0th person is at the
front of the line and the (n - 1)th person is at the back of the line.
You are given a 0-indexed integer array tickets of length n where the number of tickets that the
ith person would like to buy is tickets[i].
Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and
has to go back to the end of the line (which happens instantaneously) in order to buy more tickets.
If a person does not have any tickets left to buy, the person will leave the line.
Return the time taken for the person initially at position k (0-indexed) to finish buying tickets."""

from typing import List


class Solution:
    @staticmethod
    def timeRequiredToBuy(tickets: List[int], k: int) -> int:
        """Optimal Solution: Simulation. Time Complexity: O(n), Space Complexity: O(1)"""
        time = 0
        # Continue until the person at index k has finished
        while tickets[k] > 0:
            # Iterate through the queue: E.g. [2, 3, 2]
            # -> [1, 3, 2] -> [1, 2, 2] -> [1, 2, 1]
            # -> [0, 2, 1] -> [0, 1, 1] -> [0, 1, 0]
            for i in range(len(tickets)):

                # If the person needs more tickets
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1

                    # Stop as soon as the person at index k finishes
                    if tickets[k] == 0:
                        return time


# Unit Test: Input: tickets = [2,3,2], k = 2, Output: 6
assert Solution.timeRequiredToBuy([2, 3, 2], 2) == 6

# Unit Test: Input: tickets = [5,1,1,1], k = 0, Output: 8
assert Solution.timeRequiredToBuy([5, 1, 1, 1], 0) == 8

print("All unit tests are passed")
