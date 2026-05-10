import heapq
from typing import List

class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, c, t in roads:
            ct = c * t
            adj[u].append((v, c, ct))
            adj[v].append((u, c, ct))

        upper = prices[:]
        pq = [(prices[i], i) for i in range(n)]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d > upper[u]:
                continue
            for v, c, ct in adj[u]:
                nd = d + c + ct
                if nd < upper[v]:
                    upper[v] = nd
                    heapq.heappush(pq, (nd, v))

        INF = 10**18
        dist0 = [INF] * n
        dist1 = [INF] * n
        vis0  = [-1] * n
        vis1  = [-1] * n
        ans   = [0] * n

        for i in range(n):
            best = upper[i]
            dist0[i] = 0
            vis0[i] = i
            heap = [(0, i, 0)]

            while heap:
                d, u, ph = heapq.heappop(heap)
                if d >= best:
                    break

                if ph == 0:
                    cand = d + prices[u]
                    if cand < best:
                        if vis1[u] != i or cand < dist1[u]:
                            dist1[u] = cand
                            vis1[u] = i
                            heapq.heappush(heap, (cand, u, 1))
                    for v, c, ct in adj[u]:
                        nd = d + c
                        if nd < best and (vis0[v] != i or nd < dist0[v]):
                            dist0[v] = nd
                            vis0[v] = i
                            heapq.heappush(heap, (nd, v, 0))
                else:
                    if u == i:
                        if d < best:
                            best = d
                        continue
                    for v, c, ct in adj[u]:
                        nd = d + ct
                        if nd < best and (vis1[v] != i or nd < dist1[v]):
                            dist1[v] = nd
                            vis1[v] = i
                            heapq.heappush(heap, (nd, v, 1))

            ans[i] = best

        return ans