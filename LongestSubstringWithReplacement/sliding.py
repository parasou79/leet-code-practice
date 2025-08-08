def longestSubstringWithReplacement(str, k):
	wStart = 0
	maxLen = 0
	chMap = {}
	for wEnd in range(len(str)):		
		ch=str[wEnd]
		if ch in chMap:
			chMap[ch]+=1
		else:
			chMap[ch]=1

		while len(chMap) > k+1:
			ch=str[wStart]
			print(chMap, ch)
			if chMap[ch]==1:
				del chMap[ch]
			else:
				chMap[ch]-=1
			wStart+=1
		maxLen = max(maxLen, wEnd-wStart+1)

	return maxLen, str
def test(exp, str, k):
	ans = longestSubstringWithReplacement(str, k)
	print(ans, ans[0]==exp)
	return ans[0]

test(5, 'aabccbb', 2)
test(4, 'aaaa', 1)
test(4, 'abbcb', 1)
test(3, 'abccde', 1)
