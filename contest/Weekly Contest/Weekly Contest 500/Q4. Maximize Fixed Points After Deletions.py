from bisect import bisect_left

class Solution(object):
    def maxFixedPoints(self, nums: list[int]) -> int:
        # List comprehension
        valid = [((i-v) << 20) | v for i, v in enumerate(nums) if i >= v]
        valid.sort()
        
        ans = []
        ans_append = ans.append
        
        for val in valid:
            v = val & 0xFFFFF
            pos = bisect_left(ans, v)

            if pos == len(ans):
                ans_append(v)
            else:
                ans[pos] = v
                
        return len(ans)