from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):

        #Best runtime - Thuần toán học
        n = len(nums)
        act_total= n * (n + 1) // 2
        total = sum(set(nums))
        return [sum(nums) - total, act_total - total]
    
        # #Best memory - Bit manipulation
        # xor = 0
        # n = len(nums)
        
        # for i, num in enumerate(nums, 1):
        #     xor ^= num ^ i
        
        # diff = xor & -xor
        
        # x = 0
        # y = 0
        
        # for i, num in enumerate(nums, 1):
        #     if i & diff:
        #         x ^= i
        #     else:
        #         y ^= i
            
        #     if num & diff:
        #         x ^= num
        #     else:
        #         y ^= num

        # for num in nums:
        #     if num == x:
        #         return [x, y]
        # return [y, x]