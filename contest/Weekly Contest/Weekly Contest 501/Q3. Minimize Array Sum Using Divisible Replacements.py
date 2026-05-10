class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if 1 in nums:
            return len(nums)

        def seive(MAX, nums):
            lpf = [0]*(MAX+1)
            lpf[1] = 1
            nums.sort()
            
            for i in range(len(nums)):
                num = nums[i]
                if lpf[num] == 0:
                    lpf[num] = num
        
                    for j in range(num * 2, MAX + 1, num):
                        if lpf[j] == 0:
                            lpf[j] = num
        
            return lpf

        lpf = seive(max(nums), nums)
        # print(lpf)
        for i in range(len(nums)):
            nums[i] = lpf[nums[i]]

        # print(nums)
        return sum(nums)