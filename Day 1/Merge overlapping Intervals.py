intervals = []
for _ in range(int(input())):
	intervals.append(list(map(int, input().split())))
intervals.sort()
# print(intervals)
p = intervals[0]
ans = []
for i in range(len(intervals)):
	if intervals[i][0] <= p[1] and intervals[i][0] >= p[0]:
		p[1] = max(p[1], intervals[i][1]) 
	else:
		ans.append(p)
		p = intervals[i]
if len(p) != 0:
	ans.append(p)
print(ans)