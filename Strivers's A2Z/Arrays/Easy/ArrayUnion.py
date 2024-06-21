arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]

s = {}

for ele in arr1:
    if ele in s:
        s[ele] += 1
    else:
        s[ele] = 1

for ele in arr2:
    if ele in s:
        s[ele] += 1
    else:
        s[ele] = 1
print(list(s.keys()))