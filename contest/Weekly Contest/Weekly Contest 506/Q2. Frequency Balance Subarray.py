class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        mp = {v: i for i, v in enumerate(sorted(set(nums)))}
        m = len(mp)
        if m == 1:
            return n
        if m == n:
            return 1
        ans = 1
        for l in range(n):
            cnt = [0] * m
            mf = 0
            mf_g = 0
            dis = 0
            g_cnt = defaultdict(int)
            for r in range(l, n):
                idx = mp[nums[r]]
                cnt[idx] += 1
                f = cnt[idx]
                if f == 1:
                    dis += 1
                if f > mf:
                    mf = cnt[idx]
                    mf_g = 1
                elif f == mf:
                    mf_g += 1
                g_cnt[f] += 1
                if f > 1:
                    g_cnt[f-1] -= 1
                if dis == 1 or (mf % 2 == 0 and g_cnt[mf//2] != 0 and g_cnt[mf//2] * (mf // 2) == r - l + 1 - mf * mf_g):
                    ans = max(ans, r - l + 1)
                    #print(l, r)
        return ans
                