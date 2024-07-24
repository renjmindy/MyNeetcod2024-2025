class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        return min(Counter(text)['b'], Counter(text)['a'], Counter(text)['l'] // 2, Counter(text)['o'] // 2)
