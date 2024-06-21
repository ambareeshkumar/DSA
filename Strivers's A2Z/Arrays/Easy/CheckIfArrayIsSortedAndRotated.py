nums = [3,4,5,1,2]


# nums = [1,2,3,4,5]
def CheckArr(nums,res):
    ans = sorted(nums)
    l = len(nums) - 1

    if res == nums:
        return True
    else:
        for ind in range(l, -1, -1):
            return CheckArr(nums, [ans[ind]] + nums[(l - ind) + 1:])






print(CheckArr(nums,[]))