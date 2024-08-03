"""374. Guess Number Higher or Lower
Link: https://leetcode.com/problems/guess-number-higher-or-lower/
Difficulty: Easy
Description: We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower."""


def guess(num: int) -> int:
    """Mock function for guessing the number: Assume the number that I picked is 6"""
    picked = 6
    if num == picked:
        return 0
    elif num < picked:
        return 1
    else:
        return -1


class Solution:
    @staticmethod
    def guessNumber(n: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1).
           Similar to 0069-Sqrt(x).py and 0367-Valid-Perfect-Square.py"""
        # Initialize the left and right pointers for binary search
        left, right = 1, n
        # Loop until left pointer > right pointer
        while left <= right:
            mid = (left + right) // 2
            # Make a guess
            result = guess(mid)
            if result == 0:
                return mid
            # The middle number is less than the number, so the number is on the right side
            elif result == 1:
                left = mid + 1
            # The middle number is greater than the number, so the number is on the left side
            else:
                right = mid - 1


# Unit Test: Input: n = 10, Output: 6. Explanation: The number that I picked is 6
assert Solution.guessNumber(10) == 6

# Unit Test: Input: n = 20, Output: 6. Explanation: The number that I picked is 6
assert Solution.guessNumber(20) == 6

print("All unit tests are passed")
