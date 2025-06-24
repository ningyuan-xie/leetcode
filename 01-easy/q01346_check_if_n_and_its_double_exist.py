"""1346. Check If N and Its Double Exist
Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
Difficulty: Easy
Description: Given an array arr of integers, check if there exists two integers N and M such that:
that:
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]"""

from typing import List


class Solution:
    @staticmethod
    def checkIfExist(arr: List[int]) -> bool:
        """Optimal Solution: Set. Time Complexity: O(n), Space Complexity: O(n)."""
        # Use set because it has O(1) lookup time
        elements = set()

        # Store the elements and check if the double or half of the element exists
        for num in arr:
            if num * 2 in elements or num / 2 in elements:
                return True

            elements.add(num)

        return False


# Input: arr = [10, 2, 5, 3], Output: True
assert Solution.checkIfExist([10, 2, 5, 3]) is True

# Input: arr = [7, 1, 14, 11], Output: True
assert Solution.checkIfExist([7, 1, 14, 11]) is True

# Input: arr = [3, 1, 7, 11], Output: False
assert Solution.checkIfExist([3, 1, 7, 11]) is False

print("All unit tests are passed.")
