from typing import List
import numpy as np
class Solution:
    
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1

        data = np.asarray(restrictions, dtype=np.int64)

        x = data[:, 0]
        h = data[:, 1]

        right = x + h
        left = x - h

        order = np.argsort(right, kind="quicksort")
        right = right[order]
        left = left[order]

        count = len(right)

        # s_before[i] =
        # max(1, left[0], ..., left[i - 1])
        s_before = np.empty(count, dtype=np.int64)
        s_before[0] = 1

        if count > 1:
            np.maximum.accumulate(left[:-1], out=s_before[1:])
            np.maximum(s_before, 1, out=s_before)

        q = np.minimum(right, 2 * n - s_before)
        candidates = (q - s_before) // 2

        answer = int(candidates.max())
        tail = n - max(1, int(left.max()))

        return max(answer, tail)
'''
from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        m = len(restrictions)

        if m == 0:
            return n - 1

        if m == 1:
            x, h = restrictions[0]

            h = min(h, x - 1)

            left_peak = (x - 1 + h) >> 1

            right_peak = h + n - x

            return left_peak if left_peak > right_peak else right_peak

        SHIFT = 30
        MASK = (1 << SHIFT) - 1

        r = restrictions

        for i in range(m):
            x, h = r[i]
            r[i] = (x << SHIFT) | h

        r.sort()

        previous_x = 1
        previous_h = 0

        for i in range(m):
            packed = r[i]
            x = packed >> SHIFT
            h = packed & MASK

            maximum_from_left = previous_h + x - previous_x

            if h > maximum_from_left:
                h = maximum_from_left
                r[i] = (x << SHIFT) | h

            previous_x = x
            previous_h = h

        packed = r[m - 1]
        right_x = packed >> SHIFT
        right_h = packed & MASK

        answer = right_h + n - right_x

        for i in range(m - 2, -1, -1):
            packed = r[i]
            x = packed >> SHIFT
            h = packed & MASK

            maximum_from_right = right_h + right_x - x

            if h > maximum_from_right:
                h = maximum_from_right
                r[i] = (x << SHIFT) | h

            distance = right_x - x

            peak = (distance + h + right_h) >> 1

            if peak > answer:
                answer = peak

            right_x = x
            right_h = h

        first_peak = (right_x - 1 + right_h) >> 1

        return answer if answer > first_peak else first_peak
'''