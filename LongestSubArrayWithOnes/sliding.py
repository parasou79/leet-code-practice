def longestSubArrayWithOnesByReplacement(arr, k):
	wStart = 0
	maxLen = 0
	repCnt = 0
	for wEnd in range(len(arr)):		
		print('\tNext',wEnd, repCnt, arr[wStart:wEnd+1])
		ch=arr[wEnd]
		if ch==0:
			repCnt+=1

		while repCnt > k:
			if arr[wStart]==0:
				repCnt-=1
			wStart+=1
			print('\t\tLoop', repCnt, arr[wStart:wEnd+1])
		maxLen = max(maxLen, wEnd-wStart+1)

	return maxLen, arr
def test(exp, arr, k):
	print(arr)
	ans = longestSubArrayWithOnesByReplacement(arr, k)
	print(ans, ans[0]==exp)
	return ans[0]

test(6, [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
test(9, [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)
#test(4, 'aaaa', 1)
#test(4, 'abbcb', 1)
#test(3, 'abccde', 1)
