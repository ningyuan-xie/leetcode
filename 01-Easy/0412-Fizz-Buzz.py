# Link: https://leetcode.com/problems/fizz-buzz/
# Difficulty: Easy
# Description: Given an integer n, return a string array answer (1-indexed) where:
# - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# - answer[i] == "Fizz" if i is divisible by 3.
# - answer[i] == "Buzz" if i is divisible by 5.
# - answer[i] == i (as a string) if none of the above conditions are true.

from typing import List


class Solution:
    # Optimal Solution: Modulo Operator. Time Complexity: O(n), Space Complexity: O(1)
    @staticmethod
    def fizzBuzz(n: int) -> List[str]:
        # Initialize the output list
        output = []
        # Iterate from 1 to n (inclusive)
        for i in range(1, n + 1):
            # Check if the number is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            # Check if the number is divisible by 3
            elif i % 3 == 0:
                output.append("Fizz")
            # Check if the number is divisible by 5
            elif i % 5 == 0:
                output.append("Buzz")
            # If none of the above conditions are true, add the number as a string
            else:
                output.append(str(i))
        return output


# Unit Test: Input = 3, Output = ["1", "2", "Fizz"]
assert Solution.fizzBuzz(3) == ["1", "2", "Fizz"]

# Unit Test: Input = 5, Output = ["1", "2", "Fizz", "4", "Buzz"]
assert Solution.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

# Unit Test: Input = 15,
# Output = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
assert Solution.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz",
                                 "Fizz", "7", "8", "Fizz", "Buzz",
                                 "11", "Fizz", "13", "14", "FizzBuzz"]

print("All unit tests are passed")
