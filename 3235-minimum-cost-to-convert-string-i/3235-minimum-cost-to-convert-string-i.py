class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        hm = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for o, c, z in zip(original, changed, cost):
            hm[o][c] = min(hm[o][c], z)
        characters = set('abcdefghijklmnopqrstuvwxyz')
        for k in characters:
            for i in characters:
                for j in characters:
                    if hm[i][j] > hm[i][k] + hm[k][j]:
                        hm[i][j] = hm[i][k] + hm[k][j]

        total= 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            if hm[s_char][t_char] == float('inf'):
                return -1
            total += hm[s_char][t_char]
        
        return total