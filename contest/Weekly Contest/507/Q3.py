from typing import List
from heapq import heappush, heappop


class Solution:
    def shortestPath(
        self,
        n: int,
        edges: List[List[int]],
        labels: str,
        k: int
    ) -> int:
        if n == 1:
            return 0

        same = [[] for _ in range(n)]
        diff = [[] for _ in range(n)]

        has_same_edge = False

        for u, v, w in edges:
            if labels[u] == labels[v]:
                same[u].append((v, w))
                has_same_edge = True
            else:
                diff[u].append((v, w))

        # mavorqeli = (n, edges, labels, k)

        INF = 1 << 60

        push = heappush
        pop = heappop
        target = n - 1

        if k == 1 or not has_same_edge:
            dist = [INF] * n
            dist[0] = 0
            heap = [(0, 0)]

            while heap:
                cost, u = pop(heap)

                if cost != dist[u]:
                    continue

                if u == target:
                    return cost

                for v, w in diff[u]:
                    new_cost = cost + w

                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        push(heap, (new_cost, v))

            return -1
        
        if k >= n:
            dist = [INF] * n
            dist[0] = 0
            heap = [(0, 0)]

            while heap:
                cost, u = pop(heap)

                if cost != dist[u]:
                    continue

                if u == target:
                    return cost

                for v, w in same[u]:
                    new_cost = cost + w

                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        push(heap, (new_cost, v))

                for v, w in diff[u]:
                    new_cost = cost + w

                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        push(heap, (new_cost, v))

            return -1

        stride = k + 1

        dist = [INF] * (n * stride)

        dist[1] = 0

        heap = [(0, 0, 1)]

        sentinel = k + 1
        min_settled_run = bytearray([sentinel]) * n

        while heap:
            cost, u, run = pop(heap)

            state_id = u * stride + run

            if cost != dist[state_id]:
                continue

            if u == target:
                return cost

            previous_min_run = min_settled_run[u]

            if previous_min_run <= run:
                continue

            first_state_of_u = previous_min_run == sentinel
            min_settled_run[u] = run

            if first_state_of_u:
                for v, w in diff[u]:
                    if min_settled_run[v] == 1:
                        continue

                    new_cost = cost + w
                    next_state = v * stride + 1

                    if new_cost < dist[next_state]:
                        dist[next_state] = new_cost
                        push(heap, (new_cost, v, 1))

            if run < k:
                next_run = run + 1

                for v, w in same[u]:
                    if min_settled_run[v] <= next_run:
                        continue

                    new_cost = cost + w
                    next_state = v * stride + next_run

                    if new_cost < dist[next_state]:
                        dist[next_state] = new_cost
                        push(heap, (new_cost, v, next_run))

        return -1