class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        pairs = n >> 1

        diff = [0] * (2 * limit + 2)

        for i in range(pairs):
            a = nums[i]
            b = nums[n - 1 - i]

            if a > b:
                a, b = b, a

            low = a + 1
            high = b + limit
            s = a + b

            diff[2] += 2

            diff[low] -= 1
            diff[high + 1] += 1

            diff[s] -= 1
            diff[s + 1] += 1

        ans = float('inf')
        curr = 0

        for target in range(2, 2 * limit + 1):
            curr += diff[target]

            if curr < ans:
                ans = curr

        return ans