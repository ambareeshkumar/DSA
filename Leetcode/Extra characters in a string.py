import re
paragraph = "..Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

para = re.split(r'\W+', paragraph.lower())

seen = {}

for ele in para:
    if ele not in banned and ele != '':
        seen[ele] = seen.get(ele,0) + 1

print(seen)
print(max(seen, key = seen.get))