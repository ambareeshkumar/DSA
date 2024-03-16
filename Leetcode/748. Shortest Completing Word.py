class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:

        seen = {}
        res = []

        for ele in licensePlate.lower():
            if ele.isalpha():
                seen[ele] = seen.get(ele,0) + 1

        for ele in words:
            Found = True
            for key,val in seen.items():
                if ele.count(key) < val:
                    Found = False
            if Found:
                res.append(ele)

        res = sorted(res,key = len)
        return res[0]

sol = Solution()
licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
print(sol.shortestCompletingWord(licensePlate,words))