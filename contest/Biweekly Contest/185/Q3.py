class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        parent = [-1] * n
        remaining = [0] * n

        for u, v in edges:
            parent[v] = u
            remaining[u] += 1

        # torqavemi = (n, edges, baseTime)

        min_finish = [0] * n
        max_finish = [0] * n

        queue_node = [0] * n
        queue_value = [0] * n

        tail = 0

        for u in range(n):
            if remaining[u] == 0:
                queue_node[tail] = u
                queue_value[tail] = baseTime[u]
                tail += 1

        head = 0

        while head < tail:
            u = queue_node[head]
            finish_u = queue_value[head]
            head += 1

            p = parent[u]

            if p == -1:
                return finish_u

            current_min = min_finish[p]

            if current_min == 0 or finish_u < current_min:
                min_finish[p] = finish_u

            if finish_u > max_finish[p]:
                max_finish[p] = finish_u

            remaining[p] -= 1

            if remaining[p] == 0:
                finish_p = (
                    (max_finish[p] << 1)
                    - min_finish[p]
                    + baseTime[p]
                )

                queue_node[tail] = p
                queue_value[tail] = finish_p
                tail += 1

        raise ValueError("Invalid rooted tree")
'''
class Solution:
    def finishTime(
        self,
        n: int,
        edges: list[list[int]],
        b: list[int]
    ) -> int:
        parent = [-1] * n

        for u, v in edges:
            parent[v] = u

        minimum = [0] * n
        maximum = [None] * n

        for u in range(n - 1, -1, -1):
            current_max = maximum[u]

            if current_max is not None:
                b[u] += (current_max << 1) - minimum[u]

            p = parent[u]

            if p >= 0:
                value = b[u]
                parent_max = maximum[p]

                if parent_max is None:
                    minimum[p] = value
                    maximum[p] = value
                else:
                    if value > parent_max:
                        maximum[p] = value

                    if value < minimum[p]:
                        minimum[p] = value

        return b[0]'''