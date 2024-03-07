class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}

        for i in range(0,len(strs)):
            if "".join(sorted(strs[i])) in seen:
                seen["".join(sorted(strs[i]))].append(strs[i])
                continue
            seen["".join(sorted(strs[i]))] = [strs[i]]

        ans = [val for val in seen.values()]
        return ans

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))