class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        res = 0
        for i in range(len(source)):
            if i not in visited:
                stack = [i]
                visited.add(i)
                indices = []
                while stack:
                    node = stack.pop()
                    indices.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                count = defaultdict(int)
                for idx in indices:
                    count[source[idx]] += 1
                for idx in indices:
                    if count[target[idx]] > 0:
                        count[target[idx]] -= 1
                    else:
                        res += 1

        return res