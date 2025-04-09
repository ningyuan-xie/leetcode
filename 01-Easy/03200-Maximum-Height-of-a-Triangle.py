"""3200. Maximum Height of a Triangle
Link: https://leetcode.com/problems/maximum-height-of-a-triangle
Difficulty: Easy
Description: You are given two integers red and blue representing the count of red and blue
colored balls. You have to arrange these balls to form a triangle such that the 1st row will
have 1 ball, the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.
All the balls in a particular row should be the same color, and adjacent rows should have
different colors.
Return the maximum height of the triangle that can be achieved."""


class Solution:
    @staticmethod
    def maxHeightOfTriangle(red: int, blue: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(logn), Space Complexity: O(1)"""

        def can_build(h: int) -> bool:
            """Helper function to determine if a triangle with height h can be built"""
            total = h * (h + 1) // 2
            if total > red + blue:
                return False

            # Determine number of rows for each color
            odd_rows = (h + 1) // 2  # odd rows: 1st, 3rd, ...
            even_rows = h // 2  # even rows: 2nd, 4th, ...

            odd_needed = odd_rows * odd_rows
            even_needed = even_rows * (even_rows + 1)

            return red >= odd_needed and blue >= even_needed or \
                blue >= odd_needed and red >= even_needed

        # Binary search over possible heights
        left, right = 1, 100000
        res = 0

        while left <= right:
            mid = (left + right) // 2
            if can_build(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


# Unit Test: red = 2, blue = 4, Output = 3
assert Solution.maxHeightOfTriangle(2, 4) == 3

# Unit Test: red = 2, blue = 1, Output = 2
assert Solution.maxHeightOfTriangle(2, 1) == 2

# Unit Test: red = 1, blue = 1, Output = 1
assert Solution.maxHeightOfTriangle(1, 1) == 1

# Unit Test: red = 10, blue = 1, Output = 2
assert Solution.maxHeightOfTriangle(10, 1) == 2

print("All unit tests are passed")
