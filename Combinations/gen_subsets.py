def subsets(arr):
	# BFS - queue used
	# sort the list to handle duplicate
	arr = sorted(arr)
	prev=0

	subset=[ [] ]
	print(len(subset), subset)


	for x in arr:
		if prev!=x:
			ans = [[*y, x] for y in subset]
		else:
			ans = [[*y, x] for y in ans]
		print('\t', ans)
		subset = [*subset, *ans]
		prev=x
	return subset

def test(arr):
	print("="*30)
	print(arr)
	ans = subsets(arr)
	print(ans)

	print("-"*30)
	ans3 = [ s for s in ans if len(s)==3 ]
	print(len(ans3), ans3)
	print("-"*30)
	return len(ans)


print(test([1,5,3, 4]))
print(test([1,5,3, 1]))
print(test([1,5,3, 4, 2]))