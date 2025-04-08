"""3318. Find X-Sum of All K-Long Subarrays I
Link: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
Difficulty: Easy
Description: You are given an array nums of n integers and two integers k and x.
The x-sum of an array is calculated by the following procedure:
- Count the occurrences of all elements in the array.
- Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
- Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1]."""

from typing import List


class Solution:
    @staticmethod
    def findXSum(nums: List[int], k: int, x: int) -> List[int]:
        """Optimal Solution: Sliding Window. Time Complexity: O(n * logk), Space Complexity: O(k)."""
        n = len(nums)
        result = []

        # Initialize the frequency dictionary
        freq = {}
        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        # E.g. [1, 1, 2, 2, 3, 4, 2, 3] -> freq = {1: 2, 2: 3, 3: 2, 4: 1}

        def get_x_sum(freq_map: dict) -> int:
            """Helper function to calculate the x-sum of the frequency map."""
            # Sort by (-frequency, -value)
            top_items = sorted(freq_map.items(), key=lambda item: (-item[1], -item[0]))
            # Sum all occurrences of the top-x most frequent elements
            return sum(val * freq_map[val] for val, _ in top_items[:x])
        
        # Calculate the x-sum for the first window
        result.append(get_x_sum(freq))

        # Sliding window with subarray length k
        for i in range(k, n):
            left = nums[i - k]
            right = nums[i]

            # Move the window to the right by 1 and update the frequency map
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            freq[right] = freq.get(right, 0) + 1

            result.append(get_x_sum(freq))

        return result
    

def unit_tests():
    # Unit Test: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2, Output: [6,10,12]
    assert Solution.findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2) == [6, 10, 12]

    # Unit Test: nums = [3,8,7,8,7,5], k = 2, x = 2, Output: [11,15,15,15,12]
    assert Solution.findXSum([3, 8, 7, 8, 7, 5], 2, 2) == [11, 15, 15, 15, 12]


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed")
