class Solution:
    def findWords(self, words: list[str]) -> list[str]:

        """
        converted to set in order to decrease the time complexity as set
        searches elements in O(1) as it uses hash table.
        """
        key = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

        def getCurRow(ind):
            for i in range(0, len(key)):
                if ind.lower() in key[i]:
                    return i
            return -1

        res = []
        for word in words:
            cur = getCurRow(word[0])
            # all() will return true if all elements are present in key[cur] else false
            found = all(chr.lower() in key[cur] for chr in word)

            if found:
                res.append(word)

        return res

sol = Solution()
words = ["Hello","Alaska","Dad","Peace"]
print(sol.findWords(words))