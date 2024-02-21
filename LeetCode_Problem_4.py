class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array_mid = []
        array_mid = nums1 + nums2
        array_mid.sort()
        
        s=int(len(array_mid)/2)
        if len(array_mid)%2 ==0:
            return float(array_mid[s]+array_mid[s-1])/2
        else:
            return array_mid[s]