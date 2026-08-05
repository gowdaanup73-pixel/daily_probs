from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    queue.append(v)
        for a, b in invocations:
            if suspicious[b] and not suspicious[a]:
                return list(range(n))  
        return [i for i in range(n) if not suspicious[i]]