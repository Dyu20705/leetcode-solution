from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        depth = [-1] * (n + 1)
        depth[1] = 0
        
        q = [0] * n
        q[0] = 1
        head = 0
        tail = 1
        
        while head < tail:
            u = q[head]
            head += 1
            next_d = depth[u] + 1
            for v in adj[u]:
                if depth[v] == -1:
                    depth[v] = next_d
                    q[tail] = v
                    tail += 1
                    
        max_depth = depth[q[tail - 1]]
        
        MOD = 1_000_000_007
        return pow(2, max_depth - 1, MOD)