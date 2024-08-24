class Solution:
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        cand = {str(c:=pow(10,k)+1), str((c-1)//10-1)}
        pre = (str(int(n[:(k + 1)//2])+i) for i in (-1,0,1)) 
        for l in pre:
            r = l[-2::-1] if k%2 else l[::-1]         
            cand.add(l + r)
        cand.discard(n)
        return min(cand, key=lambda x:(abs(int(x) - int(n)), int(x)))