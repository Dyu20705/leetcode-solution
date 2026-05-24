import math

class Solution(object):
    def numberOfPairs(self, nums1, nums2, queries):
        n = len(nums2)
        B = int(math.sqrt(n)) + 1
        num_blocks = (n + B - 1) // B

        vals = nums2[:]
        block_lazy = [0] * num_blocks
        block_cnt = [{} for _ in range(num_blocks)]

        for i, v in enumerate(vals):
            b = i // B
            d = block_cnt[b]
            d[v] = d.get(v, 0) + 1

        ans = []
        nums1_list = nums1
        m = len(nums1_list)

        for q in queries:
            if q[0] == 1:
                _, x, y, val = q
                bx, by = x // B, y // B

                if bx == by:
                    d = block_cnt[bx]
                    for i in range(x, y + 1):
                        old = vals[i]
                        new = old + val
                        vals[i] = new
                        cnt_old = d[old] - 1
                        if cnt_old:
                            d[old] = cnt_old
                        else:
                            del d[old]
                        d[new] = d.get(new, 0) + 1
                else:
                    d_left = block_cnt[bx]
                    end_left = (bx + 1) * B
                    for i in range(x, end_left):
                        old = vals[i]
                        new = old + val
                        vals[i] = new
                        cnt_old = d_left[old] - 1
                        if cnt_old:
                            d_left[old] = cnt_old
                        else:
                            del d_left[old]
                        d_left[new] = d_left.get(new, 0) + 1

                    for b in range(bx + 1, by):
                        block_lazy[b] += val

                    d_right = block_cnt[by]
                    start_right = by * B
                    for i in range(start_right, y + 1):
                        old = vals[i]
                        new = old + val
                        vals[i] = new
                        cnt_old = d_right[old] - 1
                        if cnt_old:
                            d_right[old] = cnt_old
                        else:
                            del d_right[old]
                        d_right[new] = d_right.get(new, 0) + 1

            else:
                _, tot = q
                res = 0
                targets = [tot - x for x in nums1_list]
                for b in range(num_blocks):
                    lazy = block_lazy[b]
                    d = block_cnt[b]
                    for t in targets:
                        key = t - lazy
                        if key > 0:
                            res += d.get(key, 0)
                ans.append(res)

        return ans