class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        return words == sorted(words, key=lambda x: [order.index(w) for w in x])
