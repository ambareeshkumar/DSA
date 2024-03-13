class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:

        seen = {}

        # for ele in words:
        #     if "".join(sorted((ele))) in seen:
        #         seen["".join(sorted(ele))] += 1
        #     else:
        #         seen["".join(sorted(ele))] = 1

        for ele in words:
            seen["".join((sorted(ele)))] = seen.get("".join(sorted(ele)), 0) + 1

        return sum(val // 2 for val in seen.values())

sol = Solution()
words = ["ab","ba","ba"]
print(sol.maximumNumberOfStringPairs(words))