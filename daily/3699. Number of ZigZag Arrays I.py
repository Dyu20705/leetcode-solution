class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        m = r - l + 1
        dp = list(range(m))
        for _ in range((n - 2) // 2):
            remaining = sum(dp)
            accumulated = 0

            for v in range(m):
                old = dp[v]
                dp[v] = accumulated
                remaining -= old
                accumulated = (accumulated + remaining) % MOD

        if n & 1:
            suffix = 0

            for v in range(m - 1, -1, -1):
                old = dp[v]
                dp[v] = suffix

                suffix += old
                if suffix >= MOD:
                    suffix -= MOD

        return (2 * sum(dp)) % MOD