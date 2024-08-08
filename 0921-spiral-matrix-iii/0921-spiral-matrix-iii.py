class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i,j=rStart,cStart
        i_dir , j_dir=0,1
        cnt=2
        ans=[]
        fm=1
        nm=2
        while(len(ans)<(rows*cols)):
            if(-1<i<rows) and (-1<j<cols):
                ans.append([i,j])
            i+=i_dir 
            j+=j_dir
            fm-=1
            if fm==0:
                i_dir,j_dir=j_dir,-i_dir
                cnt-=1
                if cnt==0:
                    cnt=2
                    fm=nm
                    nm+=1
                else:
                    fm=nm-1
        return ans