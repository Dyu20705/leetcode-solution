#Runtime N^2 Memory N^2
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        width = n + 2
        total_size = width * width

        dist = [-2] * total_size

        queue = [0] * (n * n)
        tail = 0

        empty_row = [-1] * n

        for r, row in enumerate(grid, 1):
            base = r * width + 1
            dist[base:base + n] = empty_row

            for c, value in enumerate(row):
                if value:
                    position = base + c
                    dist[position] = 0
                    queue[tail] = position
                    tail += 1

        start = width + 1
        target = n * width + n

        if dist[start] == 0 or dist[target] == 0:
            return 0
        
        head = 0

        while head < tail:
            position = queue[head]
            head += 1

            next_distance = dist[position] + 1

            neighbor = position - width
            if dist[neighbor] == -1:
                dist[neighbor] = next_distance
                queue[tail] = neighbor
                tail += 1

            neighbor = position + width
            if dist[neighbor] == -1:
                dist[neighbor] = next_distance
                queue[tail] = neighbor
                tail += 1

            neighbor = position - 1
            if dist[neighbor] == -1:
                dist[neighbor] = next_distance
                queue[tail] = neighbor
                tail += 1

            neighbor = position + 1
            if dist[neighbor] == -1:
                dist[neighbor] = next_distance
                queue[tail] = neighbor
                tail += 1

        level = min(dist[start], dist[target])

        start_distance = dist[start]
        dist[start] = ~start_distance

        current = [start]
        lower = []

        while True:
            while current:
                position = current.pop()

                if position == target:
                    return level

                neighbor = position - width
                distance = dist[neighbor]

                if distance >= 0:
                    dist[neighbor] = ~distance

                    if distance >= level:
                        current.append(neighbor)
                    else:
                        lower.append(neighbor)

                neighbor = position + width
                distance = dist[neighbor]

                if distance >= 0:
                    dist[neighbor] = ~distance

                    if distance >= level:
                        current.append(neighbor)
                    else:
                        lower.append(neighbor)

                neighbor = position - 1
                distance = dist[neighbor]

                if distance >= 0:
                    dist[neighbor] = ~distance

                    if distance >= level:
                        current.append(neighbor)
                    else:
                        lower.append(neighbor)

                neighbor = position + 1
                distance = dist[neighbor]

                if distance >= 0:
                    dist[neighbor] = ~distance

                    if distance >= level:
                        current.append(neighbor)
                    else:
                        lower.append(neighbor)

            level -= 1
            current, lower = lower, current