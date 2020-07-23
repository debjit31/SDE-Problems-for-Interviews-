# Largest Sum Contiguous SubArray
ar = list(map(int, input().split()))
gsum, csum = ar[0], ar[0]
for i in range(1,len(ar)):
	csum = max(csum+ar[i], ar[i])
	gsum = max(gsum, csum)
print(gsum)
