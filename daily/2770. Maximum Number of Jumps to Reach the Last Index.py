from bisect import bisect_left, bisect_right

class Solution:
    def maximumJumps(self, nums, target):
        s = sorted(set(nums))
        m = len(s)
        bit = [-1] * (m + 1)

        def upd(i, v):
            i += 1
            while i <= m:
                if v > bit[i]:
                    bit[i] = v
                i += i & -i

        def qry(i):
            r = -1
            while i:
                if bit[i] > r:
                    r = bit[i]
                i -= i & -i
            return r

        rev = [-1] * (m + 1)

        def range_max(l, r):
            a = qry(r + 1)
            b = qry(l)
            if b == -1:
                return a
            if a == b:
                for i in range(l, r + 1):
                    v = rev[i]
                    if v > b:
                        b = v
                return b
            return a

        idx = {v: i for i, v in enumerate(s)}

        n = len(nums)
        dp = [-1] * n

        p = idx[nums[-1]]
        upd(p, 0)
        rev[p + 1] = 0
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            x = nums[i]
            l = bisect_left(s, x - target)
            r = bisect_right(s, x + target) - 1

            if l <= r:
                best = -1
                for j in range(l + 1, r + 2):
                    v = rev[j]
                    if v > best:
                        best = v
                if best != -1:
                    dp[i] = best + 1
                    p = idx[x]
                    if dp[i] > rev[p + 1]:
                        rev[p + 1] = dp[i]
                        upd(p, dp[i])

        return dp[0]