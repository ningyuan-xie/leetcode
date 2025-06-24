"""2269. Find the K-Beauty of a Number
Link: https://leetcode.com/problems/find-the-kth-beauty-of-a-number/
Difficulty: Easy
Description: The k-beauty of an integer num is defined as the number of substrings of num when
it is read as a string that meet the following conditions:
- It has a length of k.
- It is a divisor of num.
Given integers num and k, return the k-beauty of num.
Note:
- Leading zeros are allowed.
- 0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string."""


class Solution:
    @staticmethod
    def divisorSubstrings(num: int, k: int) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)."""
        # Convert the integer to a string
        num_str = str(num)  # 240 -> "240"
        # Initialize the window size and the number of substrings
        window_size = k
        num_substrings = 0

        # Iterate through the string
        for i in range(len(num_str) - window_size + 1):
            # Extract the substring of length k
            sub_str = num_str[i:i + window_size]
            # Convert the substring to an integer
            sub_int = int(sub_str)
            # Check if the substring is a divisor of the number
            if sub_int != 0 and num % sub_int == 0:
                # Increment the number of substrings
                num_substrings += 1

        return num_substrings


# Input: num = 240, k = 2, Output: 2
assert Solution.divisorSubstrings(240, 2) == 2

# Input: num = 430043, k = 2, Output: 2
assert Solution.divisorSubstrings(430043, 2) == 2

print("All unit tests are passed.")
