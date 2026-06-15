#nums = [3,2,2,3], val = 3
#k = 0
#i = 0, nums[0] = 3 == val, không gán, k vẫn là 0
#i = 1, nums[1] = 2 != val, gán nums[0] = 2, k = 1
#i = 2, nums[2] = 2 != val, gán nums[1] = 2, k = 2
#i = 3, nums[3] = 3 == val, không gán, k vẫn là 2
#Trả về k = 2, nums = [2, 2, 2, 3], phần tử hợp lệ là nums[0:2] = [2, 2]

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k