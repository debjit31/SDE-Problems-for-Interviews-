## Rotate a matrix by 90 degrees
def rotate(mat, n):
	for i in range(0, n):
		for j in range(i, n):
			t = mat[i][j]
			mat[i][j] = mat[j][i]
			mat[j][i] = t
			
			
	for i in range(n):
		t,j = 0, len(mat[i])-1
		while t<=j:
			tmp = mat[i][t]
			mat[i][t] = mat[i][j]
			mat[i][j] = tmp
			t+=1
			j-=1
	display(mat)
			
def display(mat):
	for i in range(n):
		for j in range(n):
			print(mat[i][j], end=' ')
		print('\t')

mat = []
n =int(input()) 
for i in range(n):
	mat.append(list(map(int, input().split())))
rotate(mat, n)
