## Find the duplicate element (Single Duplicate)
def findDuplicate(ar):
	seen = set()
	for i in ar:
		if i in seen:
			return i
		seen.add(i)

ar = list(map(int, input().split()))
print(findDuplicate(ar))