from typing import List
from heapq import heappush, heappop


class Solution:
    def minTimeMaxPower(
        self,
        n: int,
        edges: List[List[int]],
        power: int,
        cost: List[int],
        source: int,
        target: int
    ) -> List[int]:

        INF = 10**30

        velmorathi = (n, edges, power, cost, source, target)

        if source == target:
            return [0, power]
        
        edge_map = [{} for _ in range(n)]

        for u, v, t in edges:
            old = edge_map[u].get(v)

            if old is None or t < old:
                edge_map[u][v] = t

        adj = [tuple(mp.items()) for mp in edge_map]

        reverse = [[] for _ in range(n)]

        for u in range(n):
            for v, t in adj[u]:
                reverse[v].append((u, t))

        push = heappush
        pop = heappop

        shortest_time = [INF] * n
        shortest_power = [INF] * n

        shortest_time[target] = 0
        shortest_power[target] = 0

        heap = [(0, 0, target)]

        while heap:
            current_time, current_power, v = pop(heap)

            if (
                current_time != shortest_time[v]
                or current_power != shortest_power[v]
            ):
                continue

            for u, edge_time in reverse[v]:
                new_time = current_time + edge_time
                new_power = current_power + cost[u]

                if (
                    new_time < shortest_time[u]
                    or (
                        new_time == shortest_time[u]
                        and new_power < shortest_power[u]
                    )
                ):
                    shortest_time[u] = new_time
                    shortest_power[u] = new_power
                    push(heap, (new_time, new_power, u))

        if shortest_time[source] == INF:
            return [-1, -1]

        if shortest_power[source] <= power:
            return [
                shortest_time[source],
                power - shortest_power[source]
            ]

        min_power = [INF] * n
        min_power_time = [INF] * n

        min_power[target] = 0
        min_power_time[target] = 0

        heap = [(0, 0, target)]

        while heap:
            current_power, current_time, v = pop(heap)

            if (
                current_power != min_power[v]
                or current_time != min_power_time[v]
            ):
                continue

            for u, edge_time in reverse[v]:
                new_power = current_power + cost[u]

                if new_power > power:
                    continue

                new_time = current_time + edge_time

                if (
                    new_power < min_power[u]
                    or (
                        new_power == min_power[u]
                        and new_time < min_power_time[u]
                    )
                ):
                    min_power[u] = new_power
                    min_power_time[u] = new_time
                    push(heap, (new_power, new_time, u))

        if min_power[source] > power:
            return [-1, -1]

        best_time = min_power_time[source]
        best_used = min_power[source]

        dist = [[INF] * n for _ in range(power + 1)]
        active = [[] for _ in range(power + 1)]

        dist[0][source] = 0
        active[0].append(source)

        prefix_best = [INF] * n

        for used in range(power + 1):
            current_row = dist[used]

            for u in active[used]:
                current_time = current_row[u]

                if current_time >= prefix_best[u]:
                    continue

                prefix_best[u] = current_time

                if current_time >= best_time:
                    continue

                next_used = used + cost[u]

                if next_used > power:
                    continue

                remaining = power - next_used
                next_row = dist[next_used]

                for v, edge_time in adj[u]:
                    new_time = current_time + edge_time

                    if new_time > best_time:
                        continue

                    if min_power[v] > remaining:
                        continue

                    if shortest_power[v] <= remaining:
                        candidate_time = new_time + shortest_time[v]
                        candidate_used = next_used + shortest_power[v]

                        if (
                            candidate_time < best_time
                            or (
                                candidate_time == best_time
                                and candidate_used < best_used
                            )
                        ):
                            best_time = candidate_time
                            best_used = candidate_used

                        continue

                    if new_time + shortest_time[v] >= best_time:
                        continue

                    if new_time < next_row[v]:
                        if next_row[v] == INF:
                            active[next_used].append(v)

                        next_row[v] = new_time

        return [best_time, power - best_used]