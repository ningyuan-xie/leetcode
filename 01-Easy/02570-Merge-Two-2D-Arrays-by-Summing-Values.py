"""2570. Merge Two 2D Arrays by Summing Values
Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
Difficulty: Easy
Description: You are given two 2D integer arrays nums1 and nums2.
- nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
- nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.
Merge the two arrays into one array that is sorted in ascending order by id, respecting the following
conditions:
- Only ids that appear in at least one of the two arrays should be included in the resulting array.
- Each id should be included only once and its value should be the sum of the values of this id in
the two arrays. If the id does not exist in one of the two arrays then its value in that array is
considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id."""

from typing import List


class Solution:
    @staticmethod
    def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """Optimal Solution: Hash Table. Time Complexity: O(n), Space Complexity: O(n)"""
        # Create a dictionary to store the sum of values for each id
        merged_dict = {}

        # Iterate through nums1 and add values to the dictionary
        for id1, val1 in nums1:
            merged_dict[id1] = merged_dict.get(id1, 0) + val1
        # E.g. {1: 2, 2: 3, 4: 5}

        # Iterate through nums2 and add values to the dictionary
        for id2, val2 in nums2:
            merged_dict[id2] = merged_dict.get(id2, 0) + val2
        # E.g. {1: 6, 2: 3, 4: 6, 3: 2}

        # Convert the dictionary to a sorted list of lists
        merged_list = [[id_, val] for id_, val in merged_dict.items()]
        merged_list.sort(key=lambda x: x[0])
        return merged_list


# Unit Test: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]], Output: [[1,6],[2,3],[3,2],[4,6]]
assert (Solution.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]])
        == [[1, 6], [2, 3], [3, 2], [4, 6]])

# Unit Test: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]], Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
assert (Solution.mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]])
        == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]])

print("All unit tests are passed")
