class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        for i in range(len(nums)):
            nums[i] = digit_sum(nums[i])

        return min(nums)