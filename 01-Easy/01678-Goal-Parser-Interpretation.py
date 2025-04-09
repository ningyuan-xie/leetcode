"""1678. Goal Parser Interpretation
Link: https://leetcode.com/problems/goal-parser-interpretation/
Difficulty: Easy
Description: You own a Goal Parser that can interpret a string command. The command consists of an
alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the
string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are
then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command."""


class Solution:
    @staticmethod
    def interpret(command: str) -> str:
        """Optimal Solution: String Manipulation. Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize the result string
        result = ""

        # Traverse the command string and interpret the command
        i = 0
        while i < len(command):
            # Case 1: "G" -> "G"
            if command[i] == "G":
                result += "G"
                i += 1

            # Case 2: "(al)" -> "al"
            elif command[i:i + 4] == "(al)":
                result += "al"
                i += 4

            # Case 3: "()" -> "o"
            else:
                result += "o"
                i += 2

        return result


# Unit Test: command = "G()(al)", Output: "Goal"
assert Solution.interpret("G()(al)") == "Goal"

# Unit Test: command = "G()()()()(al)", Output: "Gooooal"
assert Solution.interpret("G()()()()(al)") == "Gooooal"

# Unit Test: command = "(al)G(al)()()G", Output: "alGalooG"
assert Solution.interpret("(al)G(al)()()G") == "alGalooG"

print("All unit tests are passed.")
