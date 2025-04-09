"""2469. Convert the Temperature
Link: https://leetcode.com/problems/convert-the-temperature/
Difficulty: Easy
Description: You are given a non-negative floating point number rounded to two decimal places
celsius, that denotes the temperature in Celsius.
You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
Return the array ans. Answers within 10-5 of the actual answer will be accepted.
Note that:
- Kelvin = Celsius + 273.15
- Fahrenheit = Celsius * 1.80 + 32.00."""

from typing import List


class Solution:
    @staticmethod
    def convertTemperature(celsius: float) -> List[float]:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]


# Unit Test: celsius = 36.50, Output: [309.65000, 97.70000]
assert Solution.convertTemperature(36.50) == [309.65000, 97.70000]

# Unit Test: celsius = 122.11, Output: [395.26000, 251.79800]
assert Solution.convertTemperature(122.11) == [395.26000, 251.79800]

print("All unit tests are passed.")
