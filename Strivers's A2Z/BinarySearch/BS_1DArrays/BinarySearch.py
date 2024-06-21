nums = [-1,0,3,5,9,12]

target = 2


low = 0
high = len(nums) - 1

while low <= high:

    mid = (low + high) // 2

    if nums[mid] == target:
        print(nums[mid])
        break
    elif target > nums[mid]:
        low = mid + 1
    elif target < nums[mid]:
        high = mid - 1



