class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
            seen = {}
            res = []

            for ele in set(nums1):
                seen[ele] = seen.get(ele,0) + 1

            for ele in set(nums2):
                if ele in seen:
                    res.append(ele)
            return res

    """
    One linear solution for this problem
    Solution 1
    return [ele for ele in set(nums1) if ele in set(nums2)]
    
    Solution 2
    return list(set(nums1) & set(nums2))
    """

sol = Solution()
nums1 = [1,2,2,1]
nums2 = [1,2,2,1]
print(sol.intersection(nums1,nums2))

