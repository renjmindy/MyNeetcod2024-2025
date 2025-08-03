class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        mp = [1] * len(ratings)

        ans = 0

        for l in range(1, len(ratings)):
            if ratings[l - 1] < ratings[l] and mp[l - 1] >= mp[l]: mp[l] = 1 + mp[l - 1]

        print(mp)

        for r in range(len(ratings) - 2, -1, -1):
            if ratings[r + 1] < ratings[r] and mp[r + 1] >= mp[r]: mp[r] = 1 + mp[r + 1]

        print(mp)

        return sum(mp)
