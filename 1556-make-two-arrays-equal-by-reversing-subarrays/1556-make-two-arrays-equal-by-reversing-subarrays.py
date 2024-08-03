class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        for i in target:
            if i not in arr:
                return False 
            else:
                arr.remove(i)
        return True
