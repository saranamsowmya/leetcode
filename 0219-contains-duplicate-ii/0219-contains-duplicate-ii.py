class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm={}
        for i,n in enumerate(nums):
            if n in hm and abs(i-hm[n])<=k:
                return True 
            hm[n]=i
        return False
