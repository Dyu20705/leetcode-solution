class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n = nums[-1]
        if n != len(nums) - 1:
            return False
        if len(nums) != n + 1:
            return False
        return nums == list(range(1, n + 1)) + [n]