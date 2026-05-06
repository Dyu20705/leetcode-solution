class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        left = nums[:n]
        right = nums[n:]
        for i in range (0,n):
            result.append(left[i])
            result.append(right[i])
        return result
