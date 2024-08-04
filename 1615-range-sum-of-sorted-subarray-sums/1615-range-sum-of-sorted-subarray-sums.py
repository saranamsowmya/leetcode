class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod=10**9+7
        lt=[]
        for i in range(len(nums)+1):
            for j in range(i+1,len(nums)+1):
                tot=sum(nums[i:j])
                lt.append(tot)
        lt.sort()
        res=sum(lt[left-1:right])
        return res%mod