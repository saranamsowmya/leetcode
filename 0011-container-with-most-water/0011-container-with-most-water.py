class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        l=0
        r=len(height)-1
        while(l<r):
            maxi=max(maxi,(r-l)*min(height[l],height[r]))
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1 
        return maxi