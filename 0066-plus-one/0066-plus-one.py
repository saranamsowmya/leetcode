class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        n=int(s)+1 
        n=str(n)
        nl=[]
        for i in n:
            nl.append(int(i))
        return nl