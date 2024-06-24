"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""
# Method 1 Brute Force Solution

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        base = strs[0]
        pref = 0
        for i in range(len(base)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or base[i] != strs[j][i]:
                    break
            else:
                pref += 1
                continue
            break


        return base[:pref]

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

# Time Complexity  : O(n * m)
# Space Complexity : O(1)

# Method 2 Using Sorting
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        new_strs = sorted(strs)

        fst_word = new_strs[0]
        lst_word = new_strs[-1]

        pref = ""

        for ind in range(min(len(fst_word), len(lst_word))):

            if fst_word[ind] != lst_word[ind]:
                return pref

            pref += fst_word[ind]

        return pref

print(Solution().longestCommonPrefix(strs))

# Time Complexity  : O(n logn + m)
# Space Complexity : O(n + m)