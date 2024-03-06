class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        alph = {chr(ind + 97): ele for ind, ele in enumerate(widths)}
        cur = 0
        lines = 1

        for ele in s:
            if cur + alph[ele] <= 100:
                cur += alph[ele]
            else:
                cur = 0
                cur += alph[ele]
                lines += 1

        return [lines, cur]


sol = Solution()
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = ""
result = sol.numberOfLines(widths, s)

print(result)

# Time Complexity - O(n)
# Space Complexity - O(1)