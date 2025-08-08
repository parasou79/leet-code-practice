def longestSubstr(str, k):
	maxLen = wStart = 0
	chrFreq = {}

	for wEnd in range(len(str)):
		ch = str[wEnd]
		if ch not in chrFreq:
			chrFreq[ch]=0
		chrFreq[ch]+=1
		while len(chrFreq.keys()) > k:
			sch = str[wStart]
			chrFreq[sch]-=1
			if chrFreq[sch] == 0:
				del chrFreq[sch]
			wStart+=1
			#print(sch, chrFreq, maxLen, wStart, wEnd)

		maxLen = max(maxLen, wEnd-wStart+1)
	return maxLen, str, k, chrFreq

print(longestSubstr('paaaarachute', 3))
print(longestSubstr('', 0))
print(longestSubstr('paaaarachute', 2))