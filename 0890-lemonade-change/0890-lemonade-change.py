class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        b5,b10,b20=0,0,0
        for i in bills:
            if(i==5):
                b5+=1
            elif(i==10):
                b10+=1
                if(b5>0):
                    b5-=1 
                else:
                    return False 
            else:
                b20+=1
                if(b5>0 and b10>0):
                    b5-=1 
                    b10-=1
                elif(b5>=3):
                    b5-=3
                else:
                    return False

        return True