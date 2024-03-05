class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        maxi = float('inf')

        for i in range(0, len(list1)):
            for j in range(0, len(list2)):
                cur = 0
                if list1[i] == list2[j]:
                    cur = i + j
                    if cur < maxi:
                        maxi = cur
                        res = [list1[i]]
                    elif cur == maxi:
                        res.append(list1[i])
        return res
