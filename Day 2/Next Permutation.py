## Next Permutation

nums = list(map(int, input().split()))
ind1, ind2 = -1, -1
n=len(nums)-1
for i in range(n-1,-1,-1):
    if nums[i] < nums[i+1]:
        ind1 = i
        break
if ind1 >= 0 and ind1 <= len(nums)-1:
    for j in range(len(nums)-1, -1, -1):
        if nums[j] > nums[ind1]:
            ind2 = j
            break
    t = nums[ind1]
    nums[ind1] = nums[ind2]
    nums[ind2] = t
    k=ind1+1
    l = len(nums)-1
    while k<=l:
    	t = nums[k]
    	nums[k] = nums[l]
    	nums[l] = t
    	k+=1
    	l-=1
else:
    nums.sort()
print(nums)