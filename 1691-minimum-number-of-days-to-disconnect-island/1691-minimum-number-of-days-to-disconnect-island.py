class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count():
            s=set()
            def dfs(r,c):
                st=[(r,c)]
                while st:
                    x,y=st.pop()
                    for nx,ny in[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                        if 0<=nx<len(grid) and 0<= ny<len(grid[0]) and grid[nx][ny]==1 and (nx,ny) not in s:
                            s.add((nx,ny))
                            st.append((nx,ny))
            istrue=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and (i,j) not in s:
                        istrue+=1
                        s.add((i,j))
                        dfs(i,j)
            return istrue
        if count()!=1:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if count()!=1:
                        return 1
                    grid[i][j]=1
        return 2