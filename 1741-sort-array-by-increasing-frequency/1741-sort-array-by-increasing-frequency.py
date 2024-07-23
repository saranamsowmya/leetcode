class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm={}
        for i in nums:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        return sorted(nums,key=lambda x:(hm[x],-x))
