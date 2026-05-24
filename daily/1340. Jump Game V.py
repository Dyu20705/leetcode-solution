from collections import deque

class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        left_block = [-1] * n
        dq = deque()
        for i in range(n):
            while dq and dq[0] < i - d:
                dq.popleft()
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            left_block[i] = dq[-1] if dq else -1
            dq.append(i)

        right_block = [-1] * n
        dq.clear()
        for i in range(n - 1, -1, -1):
            while dq and dq[0] > i + d:
                dq.popleft()
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            right_block[i] = dq[-1] if dq else -1
            dq.append(i)

        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2 * size)

        def update(pos, val):
            idx = pos + size
            seg[idx] = val
            idx >>= 1
            while idx:
                seg[idx] = max(seg[idx << 1], seg[idx << 1 | 1])
                idx >>= 1

        def query(l, r):
            if l > r:
                return 0
            l += size
            r += size
            res = 0
            while l <= r:
                if l & 1:
                    res = max(res, seg[l])
                    l += 1
                if not (r & 1):
                    res = max(res, seg[r])
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        indices = sorted(range(n), key=lambda i: arr[i])
        ans = 0
        for i in indices:
            left_start = max(0, i - d)
            if left_block[i] != -1:
                l_left = left_block[i] + 1
            else:
                l_left = left_start
            r_left = i - 1
            max_left = query(l_left, r_left) if l_left <= r_left else 0

            right_end = min(n - 1, i + d)
            if right_block[i] != -1:
                r_right = right_block[i] - 1
            else:
                r_right = right_end
            l_right = i + 1
            max_right = query(l_right, r_right) if l_right <= r_right else 0

            dp_i = 1 + max(max_left, max_right)
            update(i, dp_i)
            if dp_i > ans:
                ans = dp_i

        return ans