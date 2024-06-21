# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

s = "cbbd"

ans = []
count = 0
res = ""

for i in range(len(s)):
    res += s[i]
    if res == res[::-1] and len(res) > count:
        ans.append(res)

print(max(ans))