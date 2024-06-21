# nums = [2,0,2,1,1,0]

# Method 1 using sorting

# def Merge_sort(nums):
#
#     if len(nums) > 1:
#
#         mid = len(nums) // 2
#
#         left_arr = nums[:mid]
#         right_arr = nums[mid:]
#
#         Merge_sort(left_arr)
#         Merge_sort(right_arr)
#
#         i = j = k = 0
#
#         while i < len(left_arr) and j < len(right_arr):
#
#             if left_arr[i] < right_arr[j]:
#                 nums[k] = left_arr[i]
#                 i += 1
#             else:
#                 nums[k] = right_arr[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_arr):
#             nums[k] = left_arr[i]
#             i += 1
#             k += 1
#         while j < len(right_arr):
#             nums[k] = right_arr[j]
#             j += 1
#             k += 1
#
# Merge_sort(nums)
# print(nums)

# Second Method

nums = [2,0,1]
low = 0
mid = 0
high = len(nums)-1

while mid <= high:

    if nums[mid] == 2:
        nums[high],nums[mid] = nums[mid],nums[high]
        high -= 1
    elif nums[mid] == 0:
        nums[mid],nums[low] = nums[low], nums[mid]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1

print(nums)


