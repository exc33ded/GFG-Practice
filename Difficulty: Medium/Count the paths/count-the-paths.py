class Solution:
    def countPaths(self, edges, V, src, dest):
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(10000)  # Ensure we don't hit recursion depth limit

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        dp = [-1] * V

        def dfs(node):
            if node == dest:
                return 1
            if dp[node] != -1:
                return dp[node]

            total_paths = 0
            for neighbor in graph[node]:
                total_paths += dfs(neighbor)

            dp[node] = total_paths
            return total_paths

        return dfs(src)