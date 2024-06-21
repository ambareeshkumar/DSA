nums = [-2,1,-3,4,-1,2,1,-5,4]


# Method --> BruteForce

def bruteForce(nums):
    maxi_sum = 0
    lst = []
    for i in range(0,len(nums)):
        cur = nums[i]
        for j in range(i+1, len(nums)):
            cur += nums[j]
            if cur > maxi_sum:
                maxi_sum = cur
                lst.clear()
                lst = nums[i:j+1]
    return maxi_sum, lst

# Time Complexity : O(n^2)
# Space Complexity : O(n)
print(f'--------------------BRUTEFORCE SOLUTIONS ---------------------------')
print(bruteForce(nums))

# Method 2 --> Better Approach
# nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums) -> int:

    max_sum = nums[0]
    cur_sum = nums[0]

    for ind in range(1, len(nums)):
        cur_sum = max(nums[ind], cur_sum + nums[ind])
        max_sum = max(cur_sum, max_sum)

    return max_sum
print(f"----------------------KADEN'S ALOGRITHM---------------------------")
print(maxSubArray(nums))


#Modified Kadens algorithm with Start and end of Subarray

maxi_sum = 0
cur = 0
start = 0
end = 0

for ind in range(len(nums)):

    cur += nums[ind]

    if cur >= maxi_sum:
        maxi_sum = cur
        end = ind

    elif cur < 0:
        cur = 0
        start = ind + 1

# Time Complexity : O(n)
# Space Complexity : O(1)
print(f"-------------------MODIFIED KADEN'S ALGO-----------------------------")
print(maxi_sum)
print(f'Start :{start}, End :{end}')