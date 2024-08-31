class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for i in details:
            n=i[11:13]
            n=int(n)
            if(n>60):
                cnt+=1 
        return cnt