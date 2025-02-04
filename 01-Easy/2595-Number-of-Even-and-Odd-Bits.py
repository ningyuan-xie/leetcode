"""2595. Number of Even and Odd Bits
Link: https://leetcode.com/problems/number-of-even-and-odd-bits/
Difficulty: Easy
Description: You are given a positive integer n.
Let even denote the number of even indices in the binary representation of n with value 1.
Let odd denote the number of odd indices in the binary representation of n with value 1.
Note that bits are indexed from right to left in the binary representation of a number.
Return the array [even, odd]."""


class Solution:
    @staticmethod
    def evenOddBit(n: int) -> list[int]:
        """Optimal Solution: Bit Manipulation. Time Complexity: O(log(n)), Space Complexity: O(1)"""
        # Initialize counters for even and odd bits
        even_count = 0
        odd_count = 0
        bit_len = n.bit_length()  # n = 50, bin(50) = 110010, bit_len = 6

        # Iterate through the bits of n, which is why time complxity is log2(n)
        for i in range(bit_len):
            # Shift 1 to the left by the number of i, to check if n has 1 on that index
            # 1 << i: i = 0, 1 << 0 = 1; i = 1, 1 << 1 = 10; i = 2, 1 << 2 = 100
            if n & (1 << i):
                # Increment the appropriate counter based on the bit's position
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

        return [even_count, odd_count]


# Unit Test: n = 50, Output: [1, 2]
# Explanation: Binary representation of 50 is 110010. It contains 1 on indices 1, 4, and 5.
assert Solution.evenOddBit(50) == [1, 2]

# Unit Test: n = 2, Output: [0, 1]
# Explanation: Binary representation of 2 is 10. It contains 1 on index 1.
assert Solution.evenOddBit(2) == [0, 1]

print("All unit tests are passed")
