from collections import deque
from typing import List

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0

        g = [[] for _ in range(n)]
        W = {0}
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
            W.add(w)
        W = sorted(W)

        def ok(x: int) -> bool:
            D = [k + 1] * n
            D[source] = 0
            q = deque([source])
            while q:
                u = q.popleft()
                if u == target:
                    return True
                du = D[u]
                for v, w in g[u]:
                    nd = du + (1 if w > x else 0)
                    if nd < D[v] and nd <= k:
                        D[v] = nd
                        if w <= x:
                            q.appendleft(v)
                        else:
                            q.append(v)
            return False

        if not ok(W[-1]):
            return -1

        lo, hi = 0, len(W) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(W[mid]):
                hi = mid
            else:
                lo = mid + 1
        return W[lo]