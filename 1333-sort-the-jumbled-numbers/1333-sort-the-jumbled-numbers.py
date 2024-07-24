class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nl=[]
        for i in nums:
            i=str(i)
            ans=0
            for j in range(len(i)):
                ans=ans*10+mapping[int(i[j])]
            nl.append(ans)
        hm={}
        for i in range(len(nums)):
            hm[nums[i]]=nl[i]
        return sorted(nums , key=lambda x : hm[x])
        