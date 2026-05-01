class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_ = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_ = f
        for i in range(n - 1, 0, -1):
            f += sum_ - n * nums[i]
            max_ = max(max_, f)
        return max_