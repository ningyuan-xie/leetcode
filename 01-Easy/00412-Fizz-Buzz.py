"""412. Fizz Buzz
Link: https://leetcode.com/problems/fizz-buzz/
Difficulty: Easy
Description: Given an integer n, return a string array answer (1-indexed) where:
• answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
• answer[i] == "Fizz" if i is divisible by 3.
• answer[i] == "Buzz" if i is divisible by 5.
• answer[i] == i (as a string) if none of the above conditions are true."""

from typing import List


class Solution:
    @staticmethod
    def fizzBuzz(n: int) -> List[str]:
        """Optimal Solution: Linear Scan. Time Complexity: O(n), Space Complexity: O(1)."""
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


def unit_tests():
    # Input = 3, Output = ["1", "2", "Fizz"]
    assert Solution.fizzBuzz(3) == ["1", "2", "Fizz"]

    # Input = 5, Output = ["1", "2", "Fizz", "4", "Buzz"]
    assert Solution.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    # Input = 15, Output = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    assert Solution.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
