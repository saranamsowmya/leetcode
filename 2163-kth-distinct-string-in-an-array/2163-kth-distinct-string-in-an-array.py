class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm={}
        for i in arr:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        for i in hm:
            if hm[i]==1:
                k-=1
                if k==0:
                    return i
        return ''
