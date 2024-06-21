nums = [2,7,11,15,1]

target = 16


res = {}
pref = 0

for ind in range(len(nums)):

    if target - nums[ind] in res:
        print(res.get(target-nums[ind]), ind)

    res[nums[ind]] = ind

