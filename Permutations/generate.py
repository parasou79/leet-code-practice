def permutate(curr, arr, i):
	# how to use DFS - stack?
	print (curr)
	ans = [ [*curr, x] for x in arr[i:]]
	print(ans)
	#permutate(ans, arr, i+1)

def permutate2(arr):
	# BFS - queue used
	subset=[ [] ]
	print("="*30)
	print(len(subset), subset)

	# sort the list to handle duplicate
	arr = sorted(arr)
	prev=0


	for x in arr:
		if prev!=x:
			ans = [[*y, x] for y in subset]
		else:
			ans = [[*y, x] for y in ans]
		print('\t', ans)
		subset = [*subset, *ans]
		prev=x
	print(len(subset), subset)

permutate2([1,5,3, 4]) 
permutate2([1,5,3, 1]) 