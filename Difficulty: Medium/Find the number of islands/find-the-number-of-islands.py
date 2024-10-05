#User function Template for python3

from collections import deque
import sys

# Increase the recursion limit to handle deep recursion in case of large grids
sys.setrecursionlimit(10**8)

class Solution:
    def numIslands(self, grid):
        # Get the dimensions of the grid
        n = len(grid)
        m = len(grid[0])
        
        # Initialize the island count
        count = 0
        
        # Initialize a queue for BFS
        q = deque()
        
        # Create a visited grid initialized to 0 (meaning not visited)
        visited = [[0 for i in range(m)] for i in range(n)]
        
        # Iterate through each cell in the grid
        for i in range(n):
            for j in range(m):
                # If the cell is land (1) and has not been visited
                if grid[i][j] == 1 and visited[i][j] == 0:
                    # Increment the island count
                    count += 1
                    
                    # Start BFS from this cell
                    q.append([i, j])
                    visited[i][j] = 1
                    
                    # Perform BFS to mark all connected land cells
                    while q:
                        x = q.popleft()
                        r = x[0]
                        c = x[1]
                        
                        # Check all 8 possible directions (up, down, left, right, and diagonals)
                        for dr in range(-1, 2):
                            for dc in range(-1, 2):
                                nr = r + dr
                                nc = c + dc
                                
                                # Ensure the new cell is within grid bounds, is land, and not yet visited
                                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                                    q.append([nr, nc])
                                    visited[nr][nc] = 1
        
        # Return the total number of islands found
        return count

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends