"""
1903. Largest Odd Number in String

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string)
that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.


Constraints:

1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.
"""

# Solution 1

num = "35427"


class Solution:
    def largestOddNumber(self, num: str) -> str:

        for ind in range(len(num) - 1, -1, -1):
            if (int(num[ind]) % 2) != 0:
                return num[:ind + 1]

        return ""

print(Solution().largestOddNumber(num))

# Time Complexity : O(n)
# Space Complexity  : O(1)


# Solution 2
# Instead of converting to int using int() function, we directly checking the element is odd
class Solution:
    def largestOddNumber(self, num: str) -> str:

        for ind in range(len(num) - 1, -1, -1):
            if num[ind] in {'1', '3', '5', '7', '9'}:
                return num[:ind + 1]

        return ""

print(Solution().largestOddNumber(num))

# Time Complexity : O(n) But it's runtime is faster than 1st solution in leetcode.
# Space Complexity : O(1)

# Solution 3:
# Use ASCII code and convert the string to int using ord() function

class Solution:
    def largestOddNumber(self, num: str) -> str:

        for ind in range(len(num) - 1, -1, -1):
            if ((ord(num[ind]) - ord('0')) % 2) != 0:
                return num[:ind + 1]

        return ""

# Time Complexity : O(n) It is faster than 98% than other solutions in leetcode.
# Space Complexity : O(1)