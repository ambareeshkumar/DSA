class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strs = set(list1) & set(list2)

        index_sum = {}

        for ind, ele in enumerate(list1):
            if ele in common_strs:
                index_sum[ele] = ind

        for ind, ele in enumerate(list2):
            if ele in common_strs:
                index_sum[ele] = index_sum[ele] + ind

        res = [ele for ele, ind in index_sum.items() if ind == min(index_sum.values())]

        return res
