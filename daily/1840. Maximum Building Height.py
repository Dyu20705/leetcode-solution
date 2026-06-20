from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1

        r = restrictions
        r.sort()

        prev_x, prev_h = 1, 0
        for b in r:
            x, h = b
            max_h = prev_h + x - prev_x
            if h > max_h:
                h = max_h
                b[1] = h
            prev_x, prev_h = x, h

        m = len(r)
        i = m - 1
        b = r[i]
        right_x, right_h = b
        ans = right_h + n - right_x
        i -= 1

        while i >= 0:
            b = r[i]
            x, h = b
            max_h = right_h + right_x - x
            if h > max_h:
                h = max_h
                b[1] = h
            peak = (right_x - x + right_h + h) >> 1
            if peak > ans:
                ans = peak
            right_x, right_h = x, h
            i -= 1

        first_peak = (right_x - 1 + right_h) >> 1
        if first_peak > ans:
            ans = first_peak

        return ans