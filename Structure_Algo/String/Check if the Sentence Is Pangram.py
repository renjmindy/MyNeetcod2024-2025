class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        mp = Counter(sentence)
        print(len(mp))
        
        return len(mp) == 26
