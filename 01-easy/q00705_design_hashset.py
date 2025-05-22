"""705. Design HashSet
Link: https://leetcode.com/problems/design-hashset/
Difficulty: Easy
Description: Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
• void add(key) Inserts the value key into the HashSet.
• bool contains(key) Returns whether the value key exists in the HashSet or not.
• void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing."""


class MyHashSet:
    """Optimal Solution: List of Buckets. Time Complexity: O(n), Space Complexity: O(n)."""

    def __init__(self):
        """Constructor: a list of buckets [[]]."""
        # Initialize the size of the hash set with a prime number to reduce collisions
        self.size = 1001
        # Create a huge list of 1001 empty buckets (lists) to store the keys
        self.buckets = [[] for _ in range(self.size)]

    def __hash_and_bucket(self, key):
        """Helper function to compute the hash value and find the bucket, a private method not to be called outside the class (encapsulation)."""
        # Compute the hash value using modulo operation with a prime size
        hash_value = key % self.size
        # Find the bucket at the computed hash value
        return self.buckets[hash_value]

    def add(self, key: int) -> None:
        """Add the key to the hash set."""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # If the key is not present in the bucket, add it
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        """Remove the key from the hash set."""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # If the key is present in the bucket, remove it
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        """Check if the key is in the hash set."""
        # Get the hash value and find the bucket
        bucket = self.__hash_and_bucket(key)

        # Return True if the key is found in the bucket
        return key in bucket


def unit_tests():
    # Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"] [[], [1], [2], [1], [3], [2], [2], [2], [2]], Output: [null, null, null, true, false, null, true, null, false]
    hash_set = MyHashSet()  # [[], [], [], ..., []]
    hash_set.add(1)  # [[], [1], [], ..., []]
    hash_set.add(2)  # [[], [1], [2], ..., []]
    assert hash_set.contains(1)
    assert not hash_set.contains(3)
    hash_set.add(2)
    assert hash_set.contains(2)
    hash_set.remove(2)
    assert not hash_set.contains(2)


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
