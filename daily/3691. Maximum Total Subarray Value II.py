from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0

        log2 = [0] * (n + 1)
        for i in range(2, n + 1):
            log2[i] = log2[i // 2] + 1

        K = log2[n] + 1
        st_max = [nums[:]]
        st_min = [nums[:]]

        for i in range(1, K):
            step = 1 << (i - 1)
            prev_max = st_max[-1]
            prev_min = st_min[-1]
            cur_len = n - (1 << i) + 1
            if cur_len <= 0:
                break
            cur_max = [0] * cur_len
            cur_min = [0] * cur_len
            for j in range(cur_len):
                cur_max[j] = max(prev_max[j], prev_max[j + step])
                cur_min[j] = min(prev_min[j], prev_min[j + step])
            st_max.append(cur_max)
            st_min.append(cur_min)

        def range_max(l: int, r: int) -> int:
            length = r - l + 1
            k_idx = log2[length]
            return max(st_max[k_idx][l], st_max[k_idx][r - (1 << k_idx) + 1])

        def range_min(l: int, r: int) -> int:
            length = r - l + 1
            k_idx = log2[length]
            return min(st_min[k_idx][l], st_min[k_idx][r - (1 << k_idx) + 1])

        def value(l: int, r: int) -> int:
            return range_max(l, r) - range_min(l, r)

        heap = [(-value(0, n - 1), 0, n - 1)]
        visited = {(0, n - 1)}
        total = 0

        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)
            total -= neg_val  # actual value = -neg_val

            if l + 1 <= r:
                if (l + 1, r) not in visited:
                    visited.add((l + 1, r))
                    heapq.heappush(heap, (-value(l + 1, r), l + 1, r))
            if l <= r - 1:
                if (l, r - 1) not in visited:
                    visited.add((l, r - 1))
                    heapq.heappush(heap, (-value(l, r - 1), l, r - 1))

        return total