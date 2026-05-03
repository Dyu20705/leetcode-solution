class Solution(object):
    def maximumScore(self, grid):
        # n = len(grid)
        # if n == 1:
        #     return 0

        # col_sum = [[0] * (n + 1) for _ in range(n)]
        # for c in range(n):
        #     for h in range(1, n + 1):
        #         col_sum[c][h] = col_sum[c][h - 1] + grid[h - 1][c]

        # dp_prev = [[0] * (n + 1) for _ in range(n + 1)]
        # dp_curr = [[0] * (n + 1) for _ in range(n + 1)]

        # prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        # prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]

        # for i in range(1, n):
        #     for a in range(n + 1):
        #         row = dp_curr[a]
        #         for b in range(n + 1):
        #             row[b] = 0

        #     for curr_h in range(n + 1):
        #         for prev_h in range(n + 1):

        #             if curr_h <= prev_h:
        #                 extra = col_sum[i][prev_h] - col_sum[i][curr_h]
        #                 val = prev_suffix_max[prev_h][0] + extra
        #             else:
        #                 extra = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]

        #                 # inline max (tránh gọi max())
        #                 v1 = prev_suffix_max[prev_h][curr_h]
        #                 v2 = prev_max[prev_h][curr_h] + extra

        #                 if v2 > v1:
        #                     val = v2
        #                 else:
        #                     val = v1

        #             dp_curr[curr_h][prev_h] = val

        #     for curr_h in range(n + 1):
        #         best = dp_curr[curr_h][0]
        #         prev_max[curr_h][0] = best

        #         for prev_h in range(1, n + 1):
        #             if prev_h > curr_h:
        #                 penalty = col_sum[i][prev_h] - col_sum[i][curr_h]
        #             else:
        #                 penalty = 0

        #             val = dp_curr[curr_h][prev_h] - penalty
        #             if val > best:
        #                 best = val

        #             prev_max[curr_h][prev_h] = best

        #     for curr_h in range(n + 1):
        #         best = dp_curr[curr_h][n]
        #         prev_suffix_max[curr_h][n] = best

        #         for prev_h in range(n - 1, -1, -1):
        #             val = dp_curr[curr_h][prev_h]
        #             if val > best:
        #                 best = val

        #             prev_suffix_max[curr_h][prev_h] = best

        #     dp_prev, dp_curr = dp_curr, dp_prev

        # res = 0
        # for i in range(n + 1):
        #     for j in range(n + 1):
        #         if dp_prev[i][j] > res:
        #             res = dp_prev[i][j]

        # return res
        n = len(grid)

        pf = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pf[j][i + 1] = pf[j][i] + grid[i][j]

        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            pref = [0] * (n + 1)
            best = float('-inf')
            for l in range(n + 1):
                val = dp0[l] - pf[i][l]
                if val > best:
                    best = val
                pref[l] = best

            suff = [0] * (n + 2)
            best = float('-inf')
            for l in range(n, -1, -1):
                if dp1[l] > best:
                    best = dp1[l]
                suff[l] = best

            suff2 = [0] * (n + 2)
            best = float('-inf')
            if i > 0:
                for l in range(n, -1, -1):
                    val = dp1[l] + pf[i - 1][l]
                    if val > best:
                        best = val
                    suff2[l] = best

            new0 = [0] * (n + 1)
            new1 = [0] * (n + 1)

            for last in range(n + 1):
                res = pref[last] + pf[i][last]
                if suff[last] > res:
                    res = suff[last]
                new0[last] = res
                res = pref[last] + pf[i][last]
                if suff[last] > res:
                    res = suff[last]

                if i > 0:
                    val = suff2[last + 1] - pf[i - 1][last]
                    if val > res:
                        res = val

                new1[last] = res

            dp0, dp1 = new0, new1

        return max(dp0[0], dp1[0])