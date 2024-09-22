class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0

        pivot = 2 ** (n - 2)

        if k <= pivot: return self.kthGrammar(n - 1, k)
        else: return 1 - self.kthGrammar(n - 1, k - pivot)
