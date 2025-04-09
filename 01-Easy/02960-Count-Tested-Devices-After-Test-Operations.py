"""2960. Count Tested Devices After Test Operations
Link: https://leetcode.com/problems/count-tested-devices-after-test-operations/
Difficulty: Easy
Description: You are given a 0-indexed integer array batteryPercentages having length n, denoting
the battery percentages of n 0-indexed devices.
Your task is to test each device i in order from 0 to n - 1, by performing the following test
operations:
- If batteryPercentages[i] is greater than 0:
-- Increment the count of tested devices.
-- Decrease the battery percentage of all devices with indices j in the range [i + 1, n - 1] by 1,
ensuring their battery percentage never goes below 0, i.e, batteryPercentages[j] = max(0,
batteryPercentages[j] - 1).
-- Move to the next device.
- Otherwise, move to the next device without performing any test.
Return an integer denoting the number of devices that will be tested after performing the test
operations in order."""

from typing import List


class Solution:
    @staticmethod
    def countTestedDevices(batteryPercentages: List[int]) -> int:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        n = len(batteryPercentages)
        testedDevices = 0

        # Iterate through each device in the batteryPercentages array
        for i in range(n):
            if batteryPercentages[i] > 0:
                testedDevices += 1
                # Decrease the battery of all devices with indices j in [i + 1, n - 1] by 1
                for j in range(i + 1, n):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)

        return testedDevices


# Unit Test: batteryPercentages = [1,1,2,1,3], Output: 3
assert Solution.countTestedDevices([1, 1, 2, 1, 3]) == 3

# Unit Test: batteryPercentages = [0,1,2], Output: 2
assert Solution.countTestedDevices([0, 1, 2]) == 2

print("All unit tests are passed.")
