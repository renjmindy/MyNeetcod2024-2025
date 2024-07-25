class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
    
        ans = 0

        for word in words:
            if Counter(word) <= Counter(chars): ans += len(word)

        return ans
