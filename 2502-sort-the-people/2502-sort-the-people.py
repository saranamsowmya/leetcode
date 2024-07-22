class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm={}
        for i in range(len(names)):
            hm[heights[i]]=names[i]
        heights.sort(reverse=True)
        nl=[]
        for i in range(len(heights)):
            nl.append(hm[heights[i]])
        return nl

