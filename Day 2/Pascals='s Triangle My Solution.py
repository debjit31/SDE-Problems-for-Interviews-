## Pascal's Triangle
n = int(input())
triangle = []
for i in range(n):
	if i == 0:
		triangle.append([1])
	elif i == 1:
		triangle.append([1,1])
	else:
		row = [1]
		for j in range(0, len(triangle[i-1])-1):
			row.append(triangle[i-1][j] + triangle[i-1][j+1])
		row.append(1)
		triangle.append(row)
print(triangle)
			
		
		