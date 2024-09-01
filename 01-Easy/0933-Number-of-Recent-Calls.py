"""933. Number of Recent Calls
Link: https://leetcode.com/problems/number-of-recent-calls/
Difficulty: Easy
Description: You have a RecentCounter class which counts the number of recent requests within a
certain time frame.
Implement the RecentCounter class:
RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
and returns the number of requests that has happened in the past 3000 milliseconds (including the
new request). Specifically, return the number of requests that have happened in the inclusive
range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call."""

from collections import deque


class RecentCounter:
    """Optimal Solution: Sliding Window with Deque.
       Time Complexity: O(n), Space Complexity: O(n)"""

    def __init__(self):
        """Constructor: Initialize the instance variable"""
        # Initialize a queue to store the recent requests
        self.requests = deque()

    def ping(self, t: int) -> int:
        """Ping: Add a new request at time t and return the number of requests in the past 3000 ms"""
        # Add the current request to the queue
        self.requests.append(t)

        # Remove the outdated requests from the queue
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of recent requests
        return len(self.requests)


# Unit Test: Input: ["RecentCounter","ping","ping","ping","ping"], [[],[1],[100],[3001],[3002]]
# Output: [null,1,2,3,3]
recent_counter = RecentCounter()
assert recent_counter.ping(1) == 1
assert recent_counter.ping(100) == 2
assert recent_counter.ping(3001) == 3
assert recent_counter.ping(3002) == 3

print("All unit tests are passed")
