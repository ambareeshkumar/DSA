intervals = [[1,3],[2,6],[8,10],[15,18]]

res = []

def merge_int(intervals):

    intervals.sort()

    if len(res) == 0:
        res.append(intervals[0])

    start = 1

    while start < len(intervals):

        if res[-1][1] >= intervals[start][0]:
            res[-1][1] = max(res[-1][1], intervals[start][1])
            del intervals[start]
        else:
            res.append(intervals[start])
            start += 1

    return intervals


print(merge_int(intervals))
