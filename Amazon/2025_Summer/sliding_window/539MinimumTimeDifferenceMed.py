class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        mins = [int(p[:2])*60 + int(p[3:]) for p in timePoints]
        mins.sort()

        mins.append(mins[0] + 1440)

        return min(map(sub, mins[1:], mins))
