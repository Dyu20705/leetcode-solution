from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        start_damage = grid[0][0]
        if start_damage >= health:
            return False

        if health > m + n - 1:
            return True

        width = n + 2
        size = (m + 2) * width

        costs = [2] * size

        for r in range(m):
            base = (r + 1) * width + 1
            costs[base:base + n] = grid[r]

        start = width + 1
        target = m * width + n

        dist = [health] * size
        dist[start] = start_damage

        queue = deque([start])

        popleft = queue.popleft
        append = queue.append
        appendleft = queue.appendleft

        while queue:
            current = popleft()
            current_damage = dist[current]

            if current == target:
                return True

            nxt = current - 1
            cost = costs[nxt]

            if cost < 2:
                new_damage = current_damage + cost

                if new_damage < dist[nxt] and new_damage < health:
                    dist[nxt] = new_damage

                    if cost:
                        append(nxt)
                    else:
                        appendleft(nxt)

            nxt = current + 1
            cost = costs[nxt]

            if cost < 2:
                new_damage = current_damage + cost

                if new_damage < dist[nxt] and new_damage < health:
                    dist[nxt] = new_damage

                    if cost:
                        append(nxt)
                    else:
                        appendleft(nxt)

            nxt = current - width
            cost = costs[nxt]

            if cost < 2:
                new_damage = current_damage + cost

                if new_damage < dist[nxt] and new_damage < health:
                    dist[nxt] = new_damage

                    if cost:
                        append(nxt)
                    else:
                        appendleft(nxt)

            nxt = current + width
            cost = costs[nxt]

            if cost < 2:
                new_damage = current_damage + cost

                if new_damage < dist[nxt] and new_damage < health:
                    dist[nxt] = new_damage

                    if cost:
                        append(nxt)
                    else:
                        appendleft(nxt)

        return False