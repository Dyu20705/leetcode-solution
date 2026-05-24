from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        offset = nums[0]

        normal = True
        for i in range(n):
            if nums[i] != (i + offset) % n:
                normal = False
                break
        if normal:
            return 0 if offset == 0 else min(n - offset, offset + 2)

        rev = True
        for i in range(n):
            if nums[i] != (offset - i) % n:
                rev = False
                break
        if rev:
            return min(offset + 2, n - offset)

        return -1