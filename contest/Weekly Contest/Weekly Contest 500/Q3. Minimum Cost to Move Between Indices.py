class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        diff = nums[1] - nums[0]
        left[1] = 1
        for i in range(1, n - 1):
            nxt = nums[i + 1] - nums[i]
            if nxt < diff:
                left[i + 1] = left[i] + 1
                right[i] = right[i - 1] + diff
            else:
                left[i + 1] = left[i] + nxt
                right[i] = right[i - 1] + 1
            diff = nxt
        right[n-1] = right[n-2] + 1
        
        ans = []
        for l, r in queries:
            if l <= r:
                ans.append(left[r] - left[l])
            else:
                ans.append(right[l] - right[r])
        return ans
