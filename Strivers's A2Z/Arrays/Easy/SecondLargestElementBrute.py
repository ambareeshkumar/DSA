lst = [1,1,12,4,1]

maxi = lst[0]
sec_maxi = float('-inf')

mini = lst[0]
sec_mini = float('inf')

for ele in lst[1:]:

    if ele > maxi:
        sec_maxi = maxi
        maxi = ele
    elif ele > sec_maxi and ele != maxi:
        sec_maxi = ele

    if ele < mini:
        sec_mini = mini
        mini = ele
    elif ele < sec_mini and ele != mini:
        sec_mini = ele

print(sec_mini)
print(sec_maxi)