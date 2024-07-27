class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        tmp1 = [num for num in nums1 if num not in nums2]
        tmp2 = [num for num in nums2 if num not in nums1]

        return [set(tmp1), set(tmp2)]
