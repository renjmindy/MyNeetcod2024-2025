class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        pre, cur = -1, -1

        for r in range(len(arr) - 1, -1, -1):
            pre, cur = cur, max(arr[r], cur)
            arr[r] = pre

        arr[-1] = -1

        return arr
