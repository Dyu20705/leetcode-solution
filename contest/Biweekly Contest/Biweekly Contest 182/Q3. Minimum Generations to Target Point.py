from typing import List

SIZE = 343                  # 7 * 7 * 7
MULT = [i * SIZE for i in range(SIZE)]          # MULT[i] = i * 343
MID_TABLE = [0] * (SIZE * SIZE)

for a in range(SIZE):
    x1, yz1 = divmod(a, 49)
    y1, z1 = divmod(yz1, 7)
    base_a = MULT[a]
    for b in range(SIZE):
        x2, yz2 = divmod(b, 49)
        y2, z2 = divmod(yz2, 7)
        nx = (x1 + x2) >> 1
        ny = (y1 + y2) >> 1
        nz = (z1 + z2) >> 1
        MID_TABLE[base_a + b] = nx * 49 + ny * 7 + nz

class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        t_idx = target[0] * 49 + target[1] * 7 + target[2]

        known = bytearray(SIZE)

        new_pts = []
        for x, y, z in points:
            idx = x * 49 + y * 7 + z
            if not known[idx]:
                known[idx] = 1
                new_pts.append(idx)

        if known[t_idx]:
            return 0

        old_pts = []
        ans = 0

        while True:
            nxt_new = []
            n_len = len(new_pts)

            for i in range(n_len):
                i_idx = new_pts[i]
                base_i = MULT[i_idx]
                for j in range(i + 1, n_len):
                    mid = MID_TABLE[base_i + new_pts[j]]
                    if not known[mid]:
                        if mid == t_idx:
                            return ans + 1
                        known[mid] = 1
                        nxt_new.append(mid)

            for i_idx in new_pts:
                base_i = MULT[i_idx]
                for j_idx in old_pts:
                    mid = MID_TABLE[base_i + j_idx]
                    if not known[mid]:
                        if mid == t_idx:
                            return ans + 1
                        known[mid] = 1
                        nxt_new.append(mid)

            if not nxt_new:
                return -1

            ans += 1
            old_pts.extend(new_pts)
            new_pts = nxt_new