# O(n/2)   o(1)
def medianOfTwoSortedArrays(sa1, sa2):
	size = len(sa1)+len(sa2)
	mid = size // 2
	curr = prev = 0
	pos1 = 0
	pos2 = 0
	for i in range(mid+1):
		prev = curr
		if sa1[pos1] > sa2[pos2]:
			curr = sa2[pos2]
			pos2+=1
		else:
			curr = sa1[pos1]
			pos1+=1
		print(curr)
	return curr if size%2==1 else (prev+curr)/2

def test(exp, sa1, sa2):
	print(sa1)
	print(sa2)
	ans = medianOfTwoSortedArrays(sa1, sa2)
	print('ans', ans, ans==exp)
	return ans

test(5, [1,3,5,7], [2,6,9])
test(2, [1,3], [2])
test(2.5, [1,3], [2,5])