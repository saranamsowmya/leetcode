class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm1={}
        hm2={}
        for i in nums1:
            if i not in hm1:
                hm1[i]=1
            else:
                hm1[i]+=1
        for i in nums2:
            if i not in hm2:
                hm2[i]=1
            else:
                hm2[i]+=1
        ans=[]
        for i in hm1.keys():
            if i in hm2:
                ans.append(i)
        return ans

