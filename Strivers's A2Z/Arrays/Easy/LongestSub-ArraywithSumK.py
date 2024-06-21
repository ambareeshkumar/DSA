# Given an array of integers and a target sum K, find the maximum index i such that the sum of elements from the start to i (inclusive) equals K.

# Initialize the array, target sum, and variables to store the prefix sum, prefix sum to target difference map, and maximum index.
arr = [10, 5, 2, 7, 1, 9]
K = 15
pref_map = {}
pref_sum = 0
maxi = 0

# Iterate over the array elements.
for ind in range(len(arr)):

    # Update the prefix sum.
    pref_sum += arr[ind]

    # If the prefix sum equals the target sum, update the maximum index.
    if pref_sum == K:
        maxi = ind + 1

    # If the prefix sum minus the target sum is not in the prefix sum to target difference map, add it with its current index.
    if pref_sum - K not in pref_map:
        pref_map[pref_sum - K] = ind
    # If it is in the map, update the maximum index by comparing it with the difference between the current index and the stored index.
    else:
        maxi = max(maxi, ind - pref_map.get(pref_sum-K))

# Print the maximum index.
print(maxi)


# Time Complexity: O(n)
# Space Complexity: O(n)