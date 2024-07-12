#User function Template for python3
from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        V = n
        S = 1
        destination = V
        parent = [i for i in range(V + 1)]
        path = []
        q = []
        distance = [float('inf')] * (V + 1)
        distance[S] = 0
        parent[S] = S
        heapq.heappush(q, (0, S))

        while q:
            dis, node = heapq.heappop(q)
            for neighbor, wt in adj[node]:
                if dis + wt < distance[neighbor]:
                    distance[neighbor] = dis + wt
                    heapq.heappush(q, (distance[neighbor], neighbor))
                    parent[neighbor] = node

        node = destination
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        if distance[destination]==float('inf'):
            return [-1]
        path.append(S)
        total_distance = distance[destination]
        return [total_distance] + path[::-1]



#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends