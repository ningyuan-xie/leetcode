"""2379. Minimum Recolors to Get K Consecutive Black Blocks
Link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
Difficulty: Easy
Description: You are given a 0-indexed string blocks of length n, where blocks[i] is either
'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors
white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k
consecutive black blocks."""


class Solution:
    @staticmethod
    def minimumRecolors(blocks: str, k: int) -> int:
        """Optimal Solution: Sliding Window. Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize the number of white blocks in the first window of size k
        white_count = sum(1 for i in range(k) if blocks[i] == 'W')
        min_recolors = white_count  # E.g. "WWBWWBBWBW" -> white_count = min_count = 3

        # Slide the window across the string
        for i in range(k, len(blocks)):
            # If the block that is sliding out is 'W', decrease the count
            if blocks[i - k] == 'W':
                white_count -= 1
            # If the new block that is sliding in is 'W', increase the count
            if blocks[i] == 'W':
                white_count += 1
            # Update the minimum recolors needed
            min_recolors = min(min_recolors, white_count)

        return min_recolors


# Unit Test: blocks = "WBBWWBBWBW", k = 7, Output: 3
assert Solution.minimumRecolors("WBBWWBBWBW", 7) == 3

# Unit Test: blocks = "WBWBBBW", k = 2, Output: 0
assert Solution.minimumRecolors("WBWBBBW", 2) == 0

print("All unit tests are passed")
