class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rlen,clen=len(rowSum),len(colSum)
        lt = [[0]*clen for i in range(rlen)]
        i,j=0,0
        while i<rlen and j<clen:
            val=min(rowSum[i],colSum[j])
            lt[i][j]=val
            rowSum[i]-=val
            colSum[j]-=val
            if rowSum[i]==0:
                i+=1
            if colSum[j]==0:
                j+=1
        return lt
