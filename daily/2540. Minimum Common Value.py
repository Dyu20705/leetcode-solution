class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] == nums2[p2]:
                return nums1[p1]
        
        return -1
        