def setZeroes(m):
	## Optimal Approach
    r = len(m)
    c = len(m[0])
    c0=1
    for i in range(r):
    	if m[i][0] == 0:
    		c0=0
    	for j in range(1,c):
    		if m[i][j] == 0:
    			m[i][0]=0
    			m[0][j] = 0
    for i in range(r-1,-1,-1):
    	for j in range(c-1, 0, -1):
    		if m[i][0] == 0 or m[0][j] == 0:
    			m[i][j] = 0
    	if c0 == 0:
    		m[i][0] = 0
    
m = []
for _ in range(int(input())):
	m.append(list(map(int, input().split())))
setZeroes(m)
print(m)

