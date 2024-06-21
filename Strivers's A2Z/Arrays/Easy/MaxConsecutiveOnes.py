nums = [1,10,1,1,1,1]

max_ones = cur = 0

for ele in nums:

    if ele == 1:
        cur += 1
        max_ones = max(max_ones, cur)
    else:
        cur = 0

print(max(max_ones, cur))

