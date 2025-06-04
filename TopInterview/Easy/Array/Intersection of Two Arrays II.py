class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        
        l, r1, r2 = 0, 0, 0
        
        while r1 < len(nums1) and r2 < len(nums2):
            if nums1[r1] < nums2[r2]: r1 += 1
            elif nums2[r2] < nums1[r1]: r2 += 1
            else: nums1[l] = nums1[r1]; r1 += 1; r2 += 1; l += 1
                
        return nums1[:l]
