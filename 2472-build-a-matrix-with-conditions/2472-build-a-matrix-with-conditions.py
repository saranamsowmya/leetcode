class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        o1=self.topological_sort(rowConditions,k)
        o2=self.topological_sort(colConditions,k)
        if len(o1)<k or len(o2)<k:
            return []
        n= {o2[i]: i for i in range(k)}
        res=[[0]*k for j in range(k)]
        for i in range(k):
            res[i][n[o1[i]]]=o1[i]
        return res 
    def topological_sort(self, arr : List[List[int]] , k:int):
        d=[0]*k 
        o=[]
        g=defaultdict(list)
        que=deque()
        for i in arr:
            g[i[0]-1].append(i[1]-1)
            d[i[1]-1]+=1
        for i in range(k):
            if d[i]==0:
               que.append(i)
        while que:
            val = que.popleft()
            o.append(val+1)
            for i in g[val]:
                d[i]-=1
                if d[i]==0:
                    que.append(i)
        return o