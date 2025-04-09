"""1694. Reformat Phone Number
Link: https://leetcode.com/problems/reformat-phone-number/
Difficulty: Easy
Description: You are given a phone number as a string number. number consists of digits, spaces ' ',
and/or dashes '-'.
You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes.
Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
The final digits are then grouped as follows:
- 2 digits: A single block of length 2.
- 3 digits: A single block of length 3.
- 4 digits: Two blocks of length 2 each.
The blocks are then joined by dashes. Notice that the reformatting process should never produce any
blocks of length 1 and produce at most two blocks of length 2.
Return the phone number after formatting."""


class Solution:
    @staticmethod
    def reformat_number(number: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)"""
        # Remove all spaces and hyphens
        number = number.replace(" ", "").replace("-", "")

        # Initialize result and a pointer
        result = []
        i = 0

        # Process the number in blocks of 3 as much as possible
        while len(number) - i > 4:
            result.append(number[i:i + 3])
            i += 3

        # Handle the last 2-4 digits
        remaining = len(number) - i
        if remaining == 4:
            # If 4 digits are left, split them into two blocks of 2
            result.append(number[i:i + 2])
            result.append(number[i + 2:i + 4])
        else:
            # If 2-3 digits are left, add them as a single block
            result.append(number[i:])

        # Join blocks with hyphens and return
        return "-".join(result)


# Unit Test: number = "1-23-45 6", Output: "123-456"
assert Solution.reformat_number("1-23-45 6") == "123-456"

# Unit Test: number = "123 4-567", Output: "123-45-67"
assert Solution.reformat_number("123 4-567") == "123-45-67"

# Unit Test: number = "123 4-5678", Output: "123-456-78"
assert Solution.reformat_number("123 4-5678") == "123-456-78"

# Unit Test: number = "12", Output: "12"
assert Solution.reformat_number("12") == "12"

print("All unit tests are passed.")
