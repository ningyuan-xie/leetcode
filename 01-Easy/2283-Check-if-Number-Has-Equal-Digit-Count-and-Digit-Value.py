"""2283. Check if Number Has Equal Digit Count and Digit Value
Link: https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
Difficulty: Easy
Description: You are given a 0-indexed string num of length n consisting of digits.
Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num,
otherwise return false."""


class Solution:
    @staticmethod
    def digitCount(num: str) -> bool:
        """Optimal Solution: Linear Search. Time Complexity: O(n), Space Complexity: O(1)"""
        # Iterate through the string
        for index in range(len(num)):
            # Check if the digit index occurs num[index] times in num
            if num.count(str(index)) != int(num[index]):
                return False

        return True


# Unit Test: num = "1210", Output: True
assert Solution.digitCount("1210") is True

# Unit Test: num = "030", Output: False
assert Solution.digitCount("030") is False

print("All unit tests are passed")
