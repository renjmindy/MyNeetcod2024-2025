class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words.sort(key=len)
        ans = set()

        for i, word in enumerate(words):
            for j in range(i + 1, len(words)):
                if word in words[j]: ans.add(word)

        return list(ans)
