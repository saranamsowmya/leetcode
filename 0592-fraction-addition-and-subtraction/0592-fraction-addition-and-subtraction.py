class Solution:
    def fractionAddition(self, expression: str) -> str:
        lt=list(map(int,re.findall(r'[+-]?\d+',expression)))
        num=0
        den=1 
        for i in range(0,len(lt),2):
            n,d=lt[i],lt[i+1]
            num=num*d+n*den 
            den*=d 
        cd=gcd(num,den)
        return f"{num//cd}/{den//cd}"