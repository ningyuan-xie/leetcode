"""541. Reverse String II
Link: https://leetcode.com/problems/reverse-string-ii/
Difficulty: Easy
Description: Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original."""


class Solution:
    @staticmethod
    def reverseStr(s: str, k: int) -> str:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1)."""
        # Convert string to list for in-place modification
        s_list = list(s)
        n = len(s_list)
        
        # Iterate over the string in steps of 2k
        for i in range(0, n, 2*k):
            # Determine the left and right pointers for reversal
            left = i
            right = min(i + k - 1, n - 1)  
            
            # Reverse the first k characters in current 2k block
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        return ''.join(s_list)


def unit_tests():
    # Input: s = "abcdefg", k = 2, Output: "bacdfeg"
    assert Solution.reverseStr("abcdefg", 2) == "bacdfeg"

    # Input: s = "abcd", k = 2, Output: "bacd"
    assert Solution.reverseStr("abcd", 2) == "bacd"


if __name__ == "__main__":
    unit_tests()
    print("All unit tests are passed.")
