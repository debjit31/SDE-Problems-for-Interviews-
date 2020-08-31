## Search in 2D matrix
##  Approaches :- 
## Naive : nested loop search
## Better : O(nlgm) : -perform binary search on each row
## Optimal - use virtual array concept and perform binary search on the 2d matrix

def searchInMatrix(mat,target):
	r = len(mat)
	c = len(mat[0])
	low, high = 0, r*c-1
	while low <= high:
		mid = (low+high)//2
		x_i, y_i = mid//c, mid%c
		if target == mat[x_i][y_i]:
			return True
		elif target < mat[x_i][y_i]:
			high = mid-1
		else:
			low = mid + 1
	if low > high:
		return False



if __name__ == "__main__":
	mat = []
	n = int(input())
	for i in range(n):
		mat.append(list(map(int, input().split())))
	target = int(input())
	if searchInMatrix(mat, target):
		print("Found!!")
	else:
		print("Not Found!!!")