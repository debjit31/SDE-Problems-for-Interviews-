def setZeroes(m):
	## Better Approach
    r = len(m)
    c = len(m[0])
    rows = [None for _ in range(r)]
    cols = [None for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if m[i][j] == 0:
                rows[i] = 0
                cols[j] = 0
    for i in range(r):
        for j in range(c):
            if rows[i] == 0 or cols[j] == 0:
                m[i][j] = 0
    
m = []
for _ in range(int(input())):
	m.append(list(map(int, input().split())))
setZeroes(m)
print(m)

