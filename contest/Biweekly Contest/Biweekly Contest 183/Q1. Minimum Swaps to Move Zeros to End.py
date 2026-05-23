class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        swaps = 0
        while left < right:
            while left < right and nums[left] != 0:
                left += 1
            while left < right and nums[right] ==0:
                right -= 1
            if left < right:
                swaps += 1
                left += 1
                right -= 1
        return swaps