class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        
        n = len(merged)
        mid = n // 2
        
        if n % 2 == 1:
            return float(merged[mid])
        else:
            return (merged[mid - 1] + merged[mid]) / 2
