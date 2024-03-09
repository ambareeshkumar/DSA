class Solution:
    def findWords(self, words: list[str]) -> list[str]:

        key = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        def getCurRow(ind):
            for i in range(0, len(key)):
                if ind.lower() in key[i]:
                    return i
            return -1

        res = []
        for word in words:
            cur = getCurRow(word[0])
            found = True

            for j in range(0, len(word)):
                if word[j].lower() not in key[cur]:
                    found = False

            if found:
                res.append(word)

        return res

sol = Solution()
words = ["Hello","Alaska","Dad","Peace"]
print(sol.findWords(words))