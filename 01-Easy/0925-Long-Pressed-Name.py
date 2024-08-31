"""925. Long Pressed Name
Link: https://leetcode.com/problems/long-pressed-name/
Difficulty: Easy
Description: Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. Return True if it is possible that it was your
friends name, with some characters (possibly none) being long pressed."""


class Solution:
    @staticmethod
    def isLongPressedName(name: str, typed: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
           Similar to 0922-Sort-Array-By-Parity-II.py"""
        # Initialize the two pointers
        name_pointer, typed_pointer = 0, 0

        # Compare the chars of the name and typed strings
        while typed_pointer < len(typed):
            # If name_pointer is within bounds and the characters at the two pointers are the same
            if name_pointer < len(name) and name[name_pointer] == typed[typed_pointer]:
                name_pointer += 1
                typed_pointer += 1
            # If the chars at the two pointers are different, but the typed char is the same as the
            # previous typed char, only move the typed pointer to the right
            elif typed_pointer > 0 and typed[typed_pointer] == typed[typed_pointer - 1]:
                typed_pointer += 1
            # Otherwise, return False
            else:
                return False

        # Return True if both pointers are at the end of the name and typed strings
        return name_pointer == len(name) and typed_pointer == len(typed)


# Unit Test: Input: name = "alex", typed = "aaleex", Output: True
assert Solution.isLongPressedName("alex", "aaleex") is True

# Unit Test: Input: name = "saeed", typed = "ssaaedd", Output: False
assert Solution.isLongPressedName("saeed", "ssaaedd") is False

# Unit Test: Input: name = "leelee", typed = "lleeelee", Output: True
assert Solution.isLongPressedName("leelee", "lleeelee") is True

# Unit Test: Input: name = "laiden", typed = "laiden", Output: True
assert Solution.isLongPressedName("laiden", "laiden") is True

# Unit Test: Input: name = "vtkgn", typed = "vttkgnn", Output: True
assert Solution.isLongPressedName("vtkgn", "vttkgnn") is True

print("All unit tests are passed")

