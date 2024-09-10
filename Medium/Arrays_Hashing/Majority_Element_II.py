class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        avg = len(nums) // 3
        ans = list()

        cp = Counter(nums)

        for k, v in cp.items():
            if v > avg: ans.append(k)

        return sorted(ans)
