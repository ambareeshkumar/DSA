class Solution:
    def customSortString(self, order: str, s: str) -> str:
        seen = {}
        res = ""

        for ele in s:
            if ele in seen:
                seen[ele] += 1
            else:
                seen[ele] = 1

        for i in order:
            if i in seen:
                res += i * seen[i]

        for key in seen.keys():
            if key not in res:
                res += key * seen[key]

        return res

sol = Solution()
order = "cba"
s = "abcd"
print(sol.customSortString(order,s))