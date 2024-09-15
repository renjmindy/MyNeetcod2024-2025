class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        cnts, best = 0, 0

        for i, customer in enumerate(customers):
            if customer == 'Y': cnts -= 1
            else: cnts += 1
            if cnts < 0:
                cnts = 0
                best = i + 1

        return best
