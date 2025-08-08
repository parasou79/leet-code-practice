def longestSubArray(arr, targetSum):
	minLen = len(arr)
	wStart = 0
	wSum = 0

	for wEnd in range(len(arr)):
		wSum += arr[wEnd]

		while wSum >= targetSum and wStart <= wEnd:
			minLen = min(minLen, wEnd-wStart+1)
			wSum -= arr[wStart]
			wStart+=1
	return minLen, arr, targetSum

def testMe(arr, targetSum, exp):
	ans = longestSubArray(arr, targetSum)
	print(ans, ans[0]==exp)
	return ans[0]

testMe([2,1,5,2,3,2], 7, 2)
testMe([2,1,5,2,8], 7, 1)
testMe([1,2,3], 3, 1)
testMe([], 1, 0)
testMe([3,4,1,1,6], 8, 3)