"""3516. Find Closest Person
Link: https://leetcode.com/problems/find-closest-person/
Difficulty: Easy
Description: You are given three integers x, y, and z, representing the positions of three people on a number line:
• x is the position of Person 1.
• y is the position of Person 2.
• z is the position of Person 3, who does not move.
Both Person 1 and Person 2 move toward Person 3 at the same speed.
Determine which person reaches Person 3 first:
• Return 1 if Person 1 arrives first.
• Return 2 if Person 2 arrives first.
• Return 0 if both arrive at the same time.
• Return the result accordingly."""


class Solution:
    def findClosest(x: int, y: int, z: int) -> int:
        """Optimal Solution: Math. Time Complexity: O(1), Space Complexity: O(1)."""
        # Calculate the absolute distances of Person 1 and Person 2 from Person 3
        dist_x = abs(x - z)
        dist_y = abs(y - z)

        # Compare the distances and return the result
        if dist_x < dist_y:
            return 1
        elif dist_y < dist_x:
            return 2
        else:
            return 0


def unit_tests():
    # Input: x = 2, y = 7, z = 4, Output: 1
    assert Solution.findClosest(2, 7, 4) == 1

    # Input: x = 2, y = 5, z = 6, Output: 2
    assert Solution.findClosest(2, 5, 6) == 2

    # Input: x = 1, y = 5, z = 3, Output: 0
    assert Solution.findClosest(1, 5, 3) == 0


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
