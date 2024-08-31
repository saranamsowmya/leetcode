class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        csum=sum(nums)
        m=n-csum
        swap=cnt=sum(nums[0:m])
        for l in range(n):
            r=l+m 
            cnt+=nums[r%n]-nums[l]
            swap=min(swap,cnt)
        return swap