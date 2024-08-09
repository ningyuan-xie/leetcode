"""705. Design HashSet
Link: https://leetcode.com/problems/design-hashset/
Difficulty: Easy
Description: Design a HashSet without using any built-in hash table libraries."""

from typing import List, Optional


class MyHashSet:
    """Optimal Solution: List of Buckets. Time Complexity: O(n), Space Complexity: O(n)"""

    def __init__(self):
        """Constructor: Initialize the instance variable"""
        # The number of buckets; each represents a portion of the range of possible keys
        self.buckets = 1000
        # Number of items each bucket can hold;
        # use prime number to spread out the bucket_item_index, reducing collisions within each bucket
        self.bucket_items: int = 1001
        # A list of buckets; each bucket is a list of booleans indicating whether a key is present
        self.hash_set: List[Optional[List[bool]]] = [None] * self.buckets

    def add(self, key: int) -> None:
        """Add the key to the hash set"""
        # bucket_index selects the bucket; bucket_item_index selects the position in the bucket
        bucket_index, bucket_item_index = key // self.bucket_items, key % self.bucket_items

        # If the bucket is empty (None), create a new list of False values
        if not self.hash_set[bucket_index]:
            self.hash_set[bucket_index] = [False] * self.bucket_items

        # Add the key to the hash set
        self.hash_set[bucket_index][bucket_item_index] = True

    def remove(self, key: int) -> None:
        """Remove the key from the hash set"""
        # Calculate the bucket index and the bucket item index
        bucket_index, bucket_item_index = key // self.bucket_items, key % self.bucket_items

        # If the bucket is not empty, remove the key
        if self.hash_set[bucket_index]:
            self.hash_set[bucket_index][bucket_item_index] = False

    def contains(self, key: int) -> bool:
        """Check if the key is in the hash set"""
        # Calculate the bucket index and the bucket item index
        bucket_index, bucket_item_index = key // self.bucket_items, key % self.bucket_items

        # Return True if the key is in the hash set
        return (self.hash_set[bucket_index]
                and self.hash_set[bucket_index][bucket_item_index])


# Unit Test:
# Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
# Output: [null, null, null, true, false, null, true, null, false]
hash_set = MyHashSet()
hash_set.add(1)  # bucket_index = 0, bucket_item_index = 1
hash_set.add(2)  # bucket_index = 0, bucket_item_index = 2
assert hash_set.contains(1)
assert not hash_set.contains(3)
hash_set.add(2)
assert hash_set.contains(2)
hash_set.remove(2)
assert not hash_set.contains(2)

print("All unit tests are passed")
