class Solution:
    def maxPathScore(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        dp = [{} for _ in range(n)]
        dp[0][k] = 0
        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                left = dp[j - 1].copy() if j > 0 else {}
                upper = dp[j].copy()
                res = {}
                for k, v in upper.items():
                    if (k in left and left[k] < v) or (k not in left):
                        left[k] = v
                
                if curr != 0:
                    for k, v in left.items():
                        if k >= 1:
                            res[k - 1] = v + curr
                else:
                    res = left
                dp[j] = res
        return max(dp[n - 1].values()) if len(dp[n - 1]) != 0 else -1