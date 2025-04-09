"""3340. Check Balanced String
Link: https://leetcode.com/problems/check-balanced-string/
Difficulty: Easy
Description: You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.
Return true if num is balanced, otherwise return false."""


class Solution:
    @staticmethod
    def isBalanced(num: str) -> bool:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        # Initialize the sum of even and odd indices
        even_sum = 0
        odd_sum = 0

        # Iterate through the string and calculate the sums
        for i in range(len(num)):
            if i % 2 == 0:
                even_sum += int(num[i])
            else:
                odd_sum += int(num[i])

        # Check if the sums are equal
        return even_sum == odd_sum


def unit_tests():
    # Input: num = "1234", Output: False
    assert Solution.isBalanced("1234") is False

    # Input: num = "24123", Output: True
    assert Solution.isBalanced("24123") is True


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
