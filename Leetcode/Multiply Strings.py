class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        if num1 == "0" or num2 == "0":
            return "0"

        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                tmp = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0")) + carry
                carry = (res[i + j + 1] + tmp) // 10
                res[i + j + 1] = (res[i + j + 1] + tmp) % 10
            res[i] = carry

        ans = ''.join(map(str, res[i:]))

        return ans.lstrip("0")
