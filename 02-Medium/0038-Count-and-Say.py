# Link: https://leetcode.com/problems/count-and-say/
# Difficulty: Medium
# Description: The count-and-say sequence is a sequence of digit strings
# defined by the recursive formula: countAndSay(1) = "1", countAndSay(2) = "11",
# countAndSay(3) = "21", countAndSay(4) = "1211", ...
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1).

class Solution:
    # Optimal Solution: Iterative Approach. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def countAndSay(n: int) -> str:
        # Initialize the first digit string
        result = "1"
        for _ in range(n - 1):  # _ is a throwaway variable: 0 -> 1 -> 2, 3 loops to reach n = 4
            # Initialize the next digit string, the count, and the current digit
            next_result, current_digit, count = "", result[0], 1  # '1' -> '1' -> '2'
            # Read through the current digit but skip the first because it's already initialized
            for i in range(1, len(result)):
                # If the current digit is the same as the previous digit,
                if result[i] == current_digit:  # result: '1' -> '11' -> '21'
                    count += 1  # increment the count
                else:
                    # Otherwise, append the count and the current digit to the next digit string
                    next_result += str(count) + current_digit
                    # Move right to the next digit and reset the count
                    current_digit, count = result[i], 1
            # Append the final count and the current digit to the next digit string
            next_result += str(count) + current_digit  # '11' -> '21' -> '1211'
            # Update the result
            result = next_result  # '1' -> '11' -> '21' -> '1211'
        return result


# Unit Test: Input: n = 1, Output: "1"
assert Solution.countAndSay(1) == "1"

# Unit Test: Input: n = 4, Output: "1211"
assert Solution.countAndSay(4) == "1211"

print("All unit tests are passed")
