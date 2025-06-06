class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        ans = 0
        
        for num in arr:
            if num + 1 in arr: ans += 1
                
        return ans
