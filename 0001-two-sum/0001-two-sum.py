class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track={}
        for i in range(len(nums)):
            track[nums[i]]=i
        for i in range(len(nums)):
            val=target-nums[i]
            if val in track and i!=track[val]:
                return[track[val],i]
        return []
                