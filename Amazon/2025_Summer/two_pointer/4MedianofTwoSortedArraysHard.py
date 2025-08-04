class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        num = nums1 + nums2
        num.sort()

        return num[len(num) // 2] if len(num) % 2 else ((num[len(num) // 2 - 1] + num[len(num) // 2])) / 2
