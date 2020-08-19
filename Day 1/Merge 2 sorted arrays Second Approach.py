## Approach 2:- Using Insertion sort technique in O(1) space complexity
import bisect as bi
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(a)):
	if a[i] > b[0]:
		a[i], b[0] = b[0] , a[i]
		fr = b.pop(0)
		bi.insort(b,fr)
print(a)
print(b)