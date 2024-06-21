# nums = [2,2,2,2,4,4,4,4,1,4]


# Brute Force
# TIME COMPLEXITY --> O(n^2)
# SPACE COMPLEXITY --> O(1)

# maxi = 0
# ele = 0
# for i in range(0,len(nums)):
#
#     cnt = 0
#     for j in range(i,len(nums)):
#         if nums[i] == nums[j]:
#             cnt += 1
#     if cnt > maxi:
#         maxi = cnt
#         ele = nums[i]
#
# print(ele)

# Method 2 --> HASH MAP
"""
TIME COMPLEXITY:
O(n) beacuse we are using python dict is unordered map here insertion opetation 
is O(n) where as in ordermap is O(n logn)

SPACE COMPLEXITY:
O(n) beacuse we are using python dict      
"""
# res = {}
#
# for ele in nums:
#     if ele in res:
#         res[ele] += 1
#     else:
#         res[ele] = 1
# print(max(res, key = lambda x : res[x]))

# Method 3 --> Moore's voting Algorithm (optimal implementation)

nums = [2,2,2,2,4,4,4,4,1,2]
count = 0
ele = None

for ind in range(0,len(nums)):

    if count == 0:
        count = 1
        ele = nums[ind]
    elif ele == nums[ind]:
        count += 1
    elif ele != nums[ind]:
        count -= 1

print(ele)

cnt = 0
for res in nums:
    if res == ele:
        cnt += 1
if cnt > (len(nums) / 2):
    print(ele)
else:
    print(-1)