"""374. Guess Number Higher or Lower
Link: https://leetcode.com/problems/guess-number-higher-or-lower/
Difficulty: Easy
Description: We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
• -1: Your guess is higher than the number I picked (i.e. num > pick).
• 1: Your guess is lower than the number I picked (i.e. num < pick).
• 0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked."""


class Solution:
    @staticmethod
    def guessNumber(n: int) -> int:
        """Optimal Solution: Binary Search. Time Complexity: O(log(n)), Space Complexity: O(1).
        Similar to 278. First Bad Version."""
        
        def guess(num: int) -> int:
            """Mock function for guessing the number: Assume the number that I picked is 6."""
            picked = 6
            if num == picked:
                return 0
            elif num < picked:
                return 1
            else:
                return -1

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1


def unit_tests():
    # Input: n = 10, Output: 6.
    assert Solution.guessNumber(10) == 6

    # Input: n = 20, Output: 6.
    assert Solution.guessNumber(20) == 6


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
