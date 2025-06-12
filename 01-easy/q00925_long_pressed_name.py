"""925. Long Pressed Name
Link: https://leetcode.com/problems/long-pressed-name/
Difficulty: Easy
Description: Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed."""


class Solution:
    @staticmethod
    def isLongPressedName(name: str, typed: str) -> bool:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
        Similar to 922. Sort Array By Parity II."""
        # Initialize the two pointers
        name_pointer, typed_pointer = 0, 0

        # Loop through the typed string because it is the longer string
        while typed_pointer < len(typed):
            # If name_pointer is within bounds and name char == typed char
            if name_pointer < len(name) and name[name_pointer] == typed[typed_pointer]:
                name_pointer += 1
                typed_pointer += 1
            # If name char != typed char, but typed char == previous typed char
            elif typed_pointer > 0 and typed[typed_pointer] == typed[typed_pointer - 1]:
                typed_pointer += 1
            # Otherwise, name char != typed char, and typed char != previous typed char
            else:
                return False

        # Return True if both pointers are at the end of strings
        return name_pointer == len(name) and typed_pointer == len(typed)


def unit_tests():
    # Input: name = "alex", typed = "aaleex", Output: True
    assert Solution.isLongPressedName("alex", "aaleex") is True

    # Input: name = "saeed", typed = "ssaaedd", Output: False
    assert Solution.isLongPressedName("saeed", "ssaaedd") is False

    # Input: name = "leelee", typed = "lleeelee", Output: True
    assert Solution.isLongPressedName("leelee", "lleeelee") is True

    # Input: name = "laiden", typed = "laiden", Output: True
    assert Solution.isLongPressedName("laiden", "laiden") is True

    # Input: name = "vtkgn", typed = "vttkgnn", Output: True
    assert Solution.isLongPressedName("vtkgn", "vttkgnn") is True

    # Input: name = "alex", typed = "aaleexa", Output: False
    assert Solution.isLongPressedName("alex", "aaleexa") is False


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
