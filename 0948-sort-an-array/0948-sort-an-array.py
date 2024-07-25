class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=[]
        right=[]
        for i in range(0,mid):
            left.append(nums[i])
        for i in range(mid,len(nums)):
            right.append(nums[i])
        left=self.sortArray(left)
        right=self.sortArray(right)
        return merge(left,right)
    def merge(left,right):
        ans=[]
        i=0
        j=0
        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                ans.append(left[i])
                i+=1
            else:
                ans.append(right[j])
                j+=1
        while(i<len(left)):
            ans.append(left[i])
            i+=1
        while(j<len(right)):
            ans.append(right[j])
            j+=1
        return ans