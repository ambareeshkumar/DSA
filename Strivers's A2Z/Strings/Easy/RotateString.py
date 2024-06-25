"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false


Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

"""

s = "abcde"
goal = "cdeab"

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False

print(Solution().rotateString(s,goal))

# Time Complexity : O(n^2) The string manipulation and concatenation have O(n) and O(n) time which results in O(n^2) time complexity
# Space Complexity : O(n)

# Method 2

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        new_str = s + s

        if len(s) != len(goal):
            return False

        return goal in new_str

print(Solution().rotateString(s,goal))

# Time Complexity : O(n)
# Space Complexity : O(n)
