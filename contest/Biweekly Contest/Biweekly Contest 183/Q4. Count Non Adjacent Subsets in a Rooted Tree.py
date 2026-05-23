class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(parent)
        f = [[0]*k for _ in range(n)]
        g = [[0]*k for _ in range(n)]
        for i in range(n):
            f[i][0] = 1
            g[i][nums[i] % k] = 1

        for i in range(n - 1, 0, -1):
            p = parent[i]
            fp, gp = f[p], g[p]
            fi, gi = f[i], g[i]
            nz_fgi = [(r2, fi[r2] + gi[r2]) for r2 in range(k) if fi[r2] or gi[r2]]
            nz_fi = [(r2, v) for r2, v in enumerate(fi) if v]
            new_f = [0]*(2*k)
            new_g = [0]*(2*k)
            for r1, fp_v in enumerate(fp):
                if fp_v:
                    for r2, v in nz_fgi:
                        new_f[r1 + r2] += fp_v*v

            for r1, gp_v in enumerate(gp):
                if gp_v:
                    for r2, v in nz_fi:
                        new_g[r1 + r2] += gp_v*v

            for j in range(k):
                fp[j] = (new_f[j] + new_f[j + k]) % MOD
                gp[j] = (new_g[j] + new_g[j + k]) % MOD
        return (f[0][0] + g[0][0] - 1) % MOD
        