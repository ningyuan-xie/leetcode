# Link: https://leetcode.com/problems/add-binary/
# Difficulty: Easy
# Description: Given two binary strings a and b, return their sum as a binary string.

class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        # Initialize carry and result
        carry = 0
        result = []
        # Loop through the maximum length of a and b
        for i in range(max(len(a), len(b))):
            # Get the sum of the last element of a and b
            total = carry
            if i < len(a):
                total += int(a[-1 - i])
            if i < len(b):
                total += int(b[-1 - i])
            # Append the remainder of the total divided by 2 to the result
            result.append(str(total % 2))
            # Update the carry
            carry = total // 2
        # If carry is not 0, append it to the result
        if carry:
            result.append(str(carry))
        # Reverse the result and join the elements
        return "".join(result[::-1])


# Unit Test: Input: a = "11", b = "1", Output: "100"
assert Solution.addBinary("11", "1") == "100"

# Unit Test: Input: a = "1010", b = "1011", Output: "10101"
assert Solution.addBinary("1010", "1011") == "10101"

# Unit Test: Input: a = "1", b = "0", Output: "1"
assert Solution.addBinary("1", "0") == "1"
print("All unit tests are passed")
