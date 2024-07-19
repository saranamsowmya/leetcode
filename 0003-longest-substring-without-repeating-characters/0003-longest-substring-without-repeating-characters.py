class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        maxi=0
        start=0
        for i,j in enumerate(s):
            if j in d:
                start=max(start,d[j]+1)
            d[j]=i
            maxi=max(maxi,i-start+1)
        return maxi

        