class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for r in range(len(flowerbed)):
            if (r == 0 or flowerbed[r - 1] == 0) and (r == len(flowerbed) - 1 or flowerbed[r + 1] == 0):
                if flowerbed[r] == 0 and n > 0: 
                    flowerbed[r] = 1
                    n -= 1
                    if n == 0: return True

        return n == 0

        
