def repeatMissing(ar):
	n = len(ar)
	count = [0 for i in range(1, n+1)]
	for i in ar:
		count[i-1] += 1
		
	missing, repeat = 0, 0
	for i in range(n):
		if count[i] == 0:
			missing = i+1
		if count[i] > 1:
			repeat = i+1
	return (missing, repeat)
			


ar = list(map(int, input().split()))
m,r = repeatMissing(ar)
print("Missing = {} , Repeat = {}".format(m,r))