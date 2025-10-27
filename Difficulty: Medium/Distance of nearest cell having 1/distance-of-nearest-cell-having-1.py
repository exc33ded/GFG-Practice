from collections import deque
class Solution:
    def nearest(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
 
        # make a queue of all positions where it's 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0 #change it to 0
                    visited.add((r,c))
                    queue.append((r, c, 0)) #0 is the distance
                    
        while queue:
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            
            r, c, dist = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    queue.append((nr, nc, dist + 1))
                    grid[nr][nc] = dist + 1
                    visited.add((nr,nc))
        return grid