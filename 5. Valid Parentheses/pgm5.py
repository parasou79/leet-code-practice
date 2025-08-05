class Solution:
    def isValid(self, str1: str) -> bool:
        h={'(':')', '{':'}', '[':']'}
        hm = '()[]{}'
        i=0
        j=len(str1)-1
        ans = True
        while(i<j) :
            print(i,j,str1[i],str1[j])
            if str1[j] not in hm:
                print(i,j,str1[i],str1[j])
                j-=1
                continue
            if not str1[i] in hm:
                print(i,j,str1[i],str1[j])
                i+=1
                continue
            if not str1[j]==h.get(str1[i]):
                print(i,j,str1[i],str1[j])
                ans = False
                break
                i+=1
                j-=1
        if i==j and str1[i] in hm:
            ans = False
        return ans
