class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = list()

        for l in range(len(nums1)):
            if max(nums2[nums2.index(nums1[l]):]) > nums1[l]:
                for r in range(nums2.index(nums1[l]), len(nums2)):
                    if nums2[r] > nums1[l]: ans.append(nums2[r]); break
            else: ans.append(-1)

        return ans
