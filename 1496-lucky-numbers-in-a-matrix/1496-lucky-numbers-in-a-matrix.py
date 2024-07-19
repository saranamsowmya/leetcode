class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        col=set(map(max,zip(*matrix)))
        for i in matrix:
            val=min(i)
            if val in col:
                return [val]
    """
    zip can be used to take values as (3,9,15),(7,11,16),(8,13,17) from them we are forming a set of maximum elements such as (15,16,17) and the we are checking with a miimum element to print the result.
    """