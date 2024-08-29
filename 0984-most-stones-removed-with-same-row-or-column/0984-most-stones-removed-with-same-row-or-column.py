class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        g={}
        for i,j in stones:
            if i not in g:
                g[i]=[]
            if ~j not in g:
                g[~j]=[]
            g[i].append(~j)
            g[~j].append(i)
        visited=set()
        def dfs(node):
            st=[node]
            while st:
                curr=st.pop()
                if curr not in visited:
                    visited.add(curr)
                    for n in g[curr]:
                        if n not in visited:
                            st.append(n)
        cnt=0
        for i,j in stones:
            if i not in visited:
                dfs(i)
                cnt+=1 
        return len(stones)-cnt