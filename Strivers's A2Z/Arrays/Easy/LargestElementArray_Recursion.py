lst = [1, 3, 6, 8, 3, 100, 2, 57, 9, 89]


def max_ele(start, maxi):

    """
    Time complexity : O(n)
    Space Complexity : O(n)
    """

    if start == len(lst):
        return maxi

    if maxi < lst[start]:
        maxi = lst[start]

    return max_ele(start + 1, maxi)


print(max_ele(0, 0))