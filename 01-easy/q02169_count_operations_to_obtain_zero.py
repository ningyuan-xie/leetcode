"""2169. Count Operations to Obtain Zero
Link: https://leetcode.com/problems/count-operations-to-obtain-zero/
Difficulty: Easy
Description: You are given two non-negative integers num1 and num2.
In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract
num1 from num2.
- For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1
and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or num2 = 0."""


class Solution:
    @staticmethod
    def countOperations(num1: int, num2: int) -> int:
        """Optimal Solution: While Loop. Time Complexity: O(1), Space Complexity: O(1)."""
        count = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count


# Input: num1 = 2, num2 = 3, Output: 3
assert Solution.countOperations(2, 3) == 3

# Input: num1 = 10, num2 = 10, Output: 1
assert Solution.countOperations(10, 10) == 1

print("All unit tests are passed.")
