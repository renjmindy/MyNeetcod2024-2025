class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles) 

        while l <= r:
            pivot = l + (r - l) // 2 # eating speed (bananas / per hour)

            time = sum([math.ceil(pile * 1.0 / pivot) for pile in piles])

            if time > h: l = pivot + 1
            else: r = pivot - 1

        return max(l, r)
