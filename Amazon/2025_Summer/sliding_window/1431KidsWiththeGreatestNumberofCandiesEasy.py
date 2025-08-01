class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_candy = max(candies)

        ans = list()

        for candy in candies:
            if extraCandies + candy >= max_candy: ans.append(True)
            else: ans.append(False)

        return ans
