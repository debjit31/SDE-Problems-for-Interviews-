## Find All Duplicates(Multiple Duplicates)

arr = list(map(int, input().split()))
for i in range(len(arr)):
	if arr[abs(arr[i])] >= 0:
		arr[abs(arr[i])] = -arr[abs(arr[i])]
	else:
		print(abs(arr[i]), end=' ')