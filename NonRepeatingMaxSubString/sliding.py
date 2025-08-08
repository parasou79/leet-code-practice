def findNonRepeatingSubStrMax(str):
	wStart = 0
	maxLen = 0
	chMap = {}
	for wEnd in range(len(str)):		
		ch=str[wEnd]
		if ch not in chMap:
			chMap[ch]=ch
			maxLen = max(maxLen, wEnd-wStart+1)
		else:
			wStart = wEnd
	return maxLen, str
def test(exp, str):
	ans = findNonRepeatingSubStrMax(str)
	print(ans, ans[0]==exp)
	return ans[0]

test(4, 'abcd')
test(1, 'aaaa')
test(3, 'aabccbb')
test(2, 'abbbb')
test(3, 'abccde')
test(0, '')