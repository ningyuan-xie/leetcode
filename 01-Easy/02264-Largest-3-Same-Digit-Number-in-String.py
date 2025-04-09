"""2264. Largest 3 Same Digit Number in String
Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
Difficulty: Easy
Description: You are given a string num representing a large integer. An integer is good if it
meets the following conditions:
- It is a substring of num with length 3.
- It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.
Note:
- A substring is a contiguous sequence of characters within a string.
- There may be leading zeroes in num or a good integer."""


class Solution:
    @staticmethod
    def largestGoodInteger(num: str) -> str:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the window size and the maximum good integer
        window_size = 3
        max_good_integer = ""

        # Iterate through the string
        for i in range(len(num) - window_size + 1):
            # Extract the substring of length 3
            sub_str = num[i:i + window_size]
            # Check if the substring is a good integer
            if len(set(sub_str)) == 1:
                # Update the maximum good integer
                max_good_integer = max(max_good_integer, sub_str)

        return max_good_integer


# Unit Test: num = "6777133339", Output: "777"
assert Solution.largestGoodInteger("6777133339") == "777"

# Unit Test: num = "2300019", Output: "000"
assert Solution.largestGoodInteger("2300019") == "000"

# Unit Test: num = "42352338", Output: ""
assert Solution.largestGoodInteger("42352338") == ""

print("All unit tests are passed.")
