"""
Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).

Floor of X is the largest element which is smaller than or equal to X. Floor of X doesn’t exist if X is smaller than smallest element of Arr[].

Example 1:

Input:
N = 7, x = 0
arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less
than 0 is found. So output
is "-1".
Example 2:

Input:
N = 7, x = 5
arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is
2 (i.e K = 2), whose index is 1(0-based
indexing).
Your Task:
The task is to complete the function findFloor() which returns an integer denoting the index value of K or return -1 if there isn't any such number.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ X ≤ arr[n-1]
"""

arr = [1,2,8,10,11,12,19]
x = 0

# Method 1

floor = -1

for ind in range(len(arr)):

    if arr[ind] <= x:
        print(ind)
        break

print(floor)

# Time Complexity : O(n)
# Space Complexity : O(1)

# Method 2 --> The above method time complexity is O(n) but expected is O(logn)
arr = [1,2,4,10,11,12,19]
x = 12

low = 0
high = len(arr)-1

floor = -1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] <= x:
        floor = mid
        low = mid + 1
    elif arr[mid] >= x:
        high = mid - 1

print(floor)

# Time Complexity : O(n logn)
# Space Complexity : O(1)


