#runtime O(n + Q), space O(n + Q)
#runtime 697ms, memory 76.8MB
from typing import List
from array import array

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        MOD = 1_000_000_007

        m = 2 * (n - 1)
        head = array('i', [-1]) * n
        to = array('i', [0]) * m
        nxt = array('i', [0]) * m
        e_cnt = 0
        for u, v in edges:
            u -= 1
            v -= 1
            to[e_cnt] = v
            nxt[e_cnt] = head[u]
            head[u] = e_cnt
            e_cnt += 1
            to[e_cnt] = u
            nxt[e_cnt] = head[v]
            head[v] = e_cnt
            e_cnt += 1

        Q = len(queries)
        q_head = array('i', [-1]) * n
        q_to = array('i', [0]) * (2 * Q)
        q_idx = array('i', [0]) * (2 * Q)
        q_nxt = array('i', [0]) * (2 * Q)
        q_edge = 0
        for i, (u, v) in enumerate(queries):
            u -= 1
            v -= 1
            q_to[q_edge] = v
            q_idx[q_edge] = i
            q_nxt[q_edge] = q_head[u]
            q_head[u] = q_edge
            q_edge += 1
            q_to[q_edge] = u
            q_idx[q_edge] = i
            q_nxt[q_edge] = q_head[v]
            q_head[v] = q_edge
            q_edge += 1

        depth = [0] * n
        vis = bytearray(n)
        parent_tree = array('i', [-1]) * n
        parent_dsu = array('i', list(range(n)))

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] << 1) % MOD

        res = [0] * Q

        stack = [0]
        vis[0] = 1

        while stack:
            u = stack[-1]
            e = head[u]
            while e != -1 and to[e] == parent_tree[u]:
                e = nxt[e]

            if e != -1:
                v = to[e]
                head[u] = nxt[e]
                parent_tree[v] = u
                depth[v] = depth[u] + 1
                vis[v] = 1
                stack.append(v)
            else:
                stack.pop()

                qe = q_head[u]
                while qe != -1:
                    v = q_to[qe]
                    idx = q_idx[qe]
                    if vis[v]:
                        x = v
                        while parent_dsu[x] != x:
                            parent_dsu[x] = parent_dsu[parent_dsu[x]]
                            x = parent_dsu[x]
                        lca = x
                        L = depth[u] + depth[v] - (depth[lca] << 1)
                        res[idx] = pow2[L - 1] if L else 0
                    qe = q_nxt[qe]

                p = parent_tree[u]
                if p != -1:
                    parent_dsu[u] = p

        return res
#version2: runtime 676ms memory 103.42MB
# from typing import List

# class Solution:
#     def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
#         n = len(edges) + 1

#         E = 2 * (n - 1)
#         head = [-1] * n
#         to = [0] * E
#         nxt = [0] * E
#         e_cnt = 0
#         for u, v in edges:
#             u -= 1
#             v -= 1
#             to[e_cnt] = v
#             nxt[e_cnt] = head[u]
#             head[u] = e_cnt
#             e_cnt += 1
#             to[e_cnt] = u
#             nxt[e_cnt] = head[v]
#             head[v] = e_cnt
#             e_cnt += 1

#         Q = len(queries)
#         q_head = [-1] * n
#         q_to = [0] * (2 * Q)
#         q_idx = [0] * (2 * Q)
#         q_nxt = [0] * (2 * Q)
#         q_edge = 0
#         for i, (u, v) in enumerate(queries):
#             u -= 1
#             v -= 1
#             q_to[q_edge] = v
#             q_idx[q_edge] = i
#             q_nxt[q_edge] = q_head[u]
#             q_head[u] = q_edge
#             q_edge += 1
#             q_to[q_edge] = u
#             q_idx[q_edge] = i
#             q_nxt[q_edge] = q_head[v]
#             q_head[v] = q_edge
#             q_edge += 1

#         MOD = 1_000_000_007
#         pow2 = [1] * (n + 1)
#         for i in range(1, n + 1):
#             pow2[i] = (pow2[i - 1] << 1) % MOD

#         depth = [0] * n
#         vis = [False] * n
#         parent_tree = [-1] * n
#         parent_dsu = list(range(n))
#         ptr = head[:]
#         res = [0] * Q

#         stack = [0]
#         vis[0] = True

#         while stack:
#             u = stack[-1]
#             e = ptr[u]
#             while e != -1 and to[e] == parent_tree[u]:
#                 e = nxt[e]

#             if e != -1:
#                 v = to[e]
#                 ptr[u] = nxt[e]
#                 parent_tree[v] = u
#                 depth[v] = depth[u] + 1
#                 vis[v] = True
#                 stack.append(v)
#             else:
#                 stack.pop()

#                 qe = q_head[u]
#                 while qe != -1:
#                     v = q_to[qe]
#                     idx = q_idx[qe]
#                     if vis[v]:
#                         x = v
#                         while parent_dsu[x] != x:
#                             parent_dsu[x] = parent_dsu[parent_dsu[x]]
#                             x = parent_dsu[x]
#                         lca = x
#                         L = depth[u] + depth[v] - (depth[lca] << 1)
#                         res[idx] = pow2[L - 1] if L else 0
#                     qe = q_nxt[qe]

#                 p = parent_tree[u]
#                 if p != -1:
#                     parent_dsu[u] = p

#         return res