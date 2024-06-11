# Link: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Description: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.


class Solution:
    @staticmethod
    def merge(nums1, m, nums2, n):  # merge nums2 into nums1
        # Initialize the pointers for nums1 and nums2
        p1 = m - 1  # last index of current nums1
        p2 = n - 1  # last index of nums2
        last = m + n - 1  # last index of the merged array nums1

        # Iterate the merged array in reverse order
        for p in range(last, -1, -1):
            # If there are no more elements in nums2, break
            if p2 < 0:
                break
            # If nums1's element is greater, put in nums1's element
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            # If nums2's element is greater, put in nums2's element
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        return nums1

    # Helper function to print the merged array
    @staticmethod
    def printMergedArray(nums1, m, nums2, n):
        print(Solution.merge(nums1, m, nums2, n))


# Unit Test: Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3, Output: [1,2,2,3,5,6]
Solution.printMergedArray([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

# Unit Test: Input: nums1 = [2,2,3,0,0,0], m = 3, nums2 = [1,5,6], n = 3, Output: [1,2,2,3,5,6]
Solution.printMergedArray([2, 2, 3, 0, 0, 0], 3, [1, 5, 6], 3)

# Unit Test: Input: nums1 = [1], m = 1, nums2 = [], n = 0, Output: [1]
Solution.printMergedArray([1], 1, [], 0)

# Unit Test: Input: nums1 = [0], m = 0, nums2 = [1], n = 1, Output: [1]
Solution.printMergedArray([0], 0, [1], 1)
print("All unit tests are passed")
