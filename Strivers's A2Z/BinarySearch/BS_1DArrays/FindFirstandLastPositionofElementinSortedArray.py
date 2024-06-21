"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

nums = [5,7,7,8,8,10]
target = 8

low = 0
high = len(nums) - 1

ans = []
start = 0
end = len(nums)

while low <= high:

    mid = (low + high) // 2

    if target == nums[mid]:
        ans.append(mid)
        high = high - 1
    elif target > nums[mid]:
        low = mid + 1
    elif target < nums[mid]:
        high = mid - 1

if ans:
    print([min(ans),max(ans)])
else:
    print([-1,-1])