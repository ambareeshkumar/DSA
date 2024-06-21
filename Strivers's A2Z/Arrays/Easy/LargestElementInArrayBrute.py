# Brute force Approach -> Sort the array and return the last element

lst = [1,3,6,200,500,500,8,3,100,2,57,9,89]

# Implementing Merge Sort
def largest_ele(lst):
    """
    Time Complexity : O(n logn)
    Space Complexity : O(n)
    """
    if len(lst) > 1:

        mid = len(lst)//2

        left_arr = lst[:mid]
        right_arr = lst[mid:]

        largest_ele(left_arr)
        largest_ele(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):

            if left_arr[i] < right_arr[j]:
                lst[k] = left_arr[i]
                i += 1
            else:
                lst[k] = right_arr[j]
                j += 1

            k += 1

        while i < len(left_arr):
            lst[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):

            lst[k] = right_arr[j]
            j += 1
            k += 1

    return lst[-1]


print(largest_ele(lst))


