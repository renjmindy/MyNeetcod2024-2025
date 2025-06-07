class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winner_mp, loser_mp = defaultdict(int), defaultdict(int)
        
        for match in matches:
            winner_mp[match[0]] += 1
            loser_mp[match[1]] += 1
            
        w, l = list(), list()
        
        for k, v in winner_mp.items():
            if k not in loser_mp.keys(): w.append(k)
            
        for k, v in loser_mp.items():
            if v == 1: l.append(k)
                
        w.sort()
        l.sort()
        
        return [w, l]
